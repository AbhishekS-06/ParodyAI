# Audio separation and mixing utilities
import os
import shutil
from pydub import AudioSegment

def extract_audio_demucs(input_song, output_folder="separated"):
    """
    Uses Facebook AI's Demucs to separate vocals and instrumentals.

    Parameters:
    - input_song (str): Path to the song file (e.g., 'song.mp3').
    - output_folder (str): Folder where extracted files will be saved.

    Returns:
    - bool: True if successful, False otherwise
    """
    try:
        import subprocess
        command = f"/usr/bin/python3 -m demucs {input_song}"
        result = subprocess.run(command.split(), capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error running demucs: {result.stderr}")
            return False
            
        print(f"Audio separation completed. Output saved in '{output_folder}'")
        return True
    except Exception as e:
        print(f"Error running demucs: {str(e)}")
        return False

def lower_instrumental_volume(input_file="instrumental.wav", output_file="instrumental.wav", volume_reduction_db=20):
    """
    Lowers the volume of the instrumental track.

    Parameters:
    - input_file (str): Path to the input instrumental file.
    - output_file (str): Path to save the lowered volume instrumental file.
    - volume_reduction_db (int): Amount of volume reduction in decibels (dB).
    """
    instrumental = AudioSegment.from_file(input_file)
    lowered_instrumental = instrumental - volume_reduction_db
    lowered_instrumental.export(output_file, format="wav")
    print(f"Instrumental volume adjusted and saved as {output_file}")

def merge_instrumental_stems(output_folder="separated/htdemucs/original", output_file="instrumental.wav"):
    """
    Merges 'drums.wav', 'bass.wav', and 'other.wav' into a single instrumental track.

    Parameters:
    - output_folder (str): The directory where Demucs saves the separated stems.
    - output_file (str): The final merged instrumental file.
    """
    try:
        drums = AudioSegment.from_file(f"{output_folder}/drums.wav")
        bass = AudioSegment.from_file(f"{output_folder}/bass.wav")
        other = AudioSegment.from_file(f"{output_folder}/other.wav")

        instrumental = drums.overlay(bass).overlay(other)
        instrumental.export(output_file, format="wav")
        print(f"Instrumental tracks merged and saved as {output_file}")

        lower_instrumental_volume(input_file=output_file, output_file=output_file)

    except FileNotFoundError as e:
        print(f"Error: {e}. Required stem files not found in {output_folder}")
    except Exception as e:
        print(f"Error during instrumental merging: {e}")

def mix_audio(vocal_file, instrumental_file, output_file="output.mp3"):
    """
    Mixes vocals and instrumental into a single audio file.

    Parameters:
    - vocal_file (str): Path to the vocal file.
    - instrumental_file (str): Path to the instrumental file.
    - output_file (str): Path to save the mixed audio file.
    """
    vocals = AudioSegment.from_file(vocal_file)
    instrumental = AudioSegment.from_file(instrumental_file)
    combined = instrumental.overlay(vocals, position=0)
    combined.export(output_file, format="mp3")
    print(f"Final mix completed and saved as {output_file}")

def main():
    # Extract audio using demucs
    if not extract_audio_demucs("original.mp3"):
        shutil.copy("original.mp3", "instrumental.wav")
        print("Audio separation failed, using original as instrumental")
    else:
        merge_instrumental_stems()

    # Mix the audio
    mix_audio("output_speed.mp3", "instrumental.wav")

    # Cleanup temporary files and folders
    folder_to_delete = 'demucs_output/htdemucs'
    if os.path.exists(folder_to_delete):
        try:
            shutil.rmtree(folder_to_delete)
            print(f"Cleaned up temporary folder: {folder_to_delete}")
        except OSError as e:
            print(f"Error cleaning up folder {folder_to_delete}: {e}")

    # Clean up temporary files
    files_to_delete = ["original.mp3", "output_speed.mp3", "instrumental.wav", "parody_lyrics.mp3"]
    for file in files_to_delete:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"Removed temporary file: {file}")
            except OSError as e:
                print(f"Error removing file {file}: {e}")

if __name__ == "__main__":
    main()

