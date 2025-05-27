import yt_dlp

def main(song_name, output_path="original"):
    song_name = song_name + " lyrics"
    print(f"\nSearching and downloading '{song_name}' from YouTube...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': False,
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([f"ytsearch1:{song_name}"])
            print(f"Download complete. Saved as {output_path}")
            return output_path
        except Exception as e:
            print(f"Error downloading song: {e}")
            return None

if __name__ == "__main__":
    song = input("Enter the song title to download: ")
    main(song)
