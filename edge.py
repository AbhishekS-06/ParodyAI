import edge_tts
import asyncio

async def generate_speech_from_file(input_file, output_filename, rate="+0%", voice="en-US-BrianNeural"):
    with open(input_file, 'r', encoding="utf-8") as file:
        text = file.read()

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate
    )

    await communicate.save(output_filename)
    print(f"Audio generation complete. Saved as {output_filename} (Rate: {rate})")

def main(voice="en-US-BrianNeural", speed="1.0x"):
    input_file = "parody_lyrics.txt"
    output_filename = "output_speed.mp3"

    speed_map = {
        "1.5x": "+50%",
        "1.0x": "+0%",
        "0.75x": "-25%"
    }
    rate = speed_map.get(speed, "+0%")

    asyncio.run(generate_speech_from_file(input_file, output_filename, rate=rate, voice=voice))

if __name__ == "__main__":
    main()