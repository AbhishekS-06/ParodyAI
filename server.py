from flask import Flask, request, jsonify, render_template, send_file
import asyncio
import download_song_as_mp3
import parody_generator
import edge
import main
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_parody", methods=["POST"])
def generate_parody():
    data = request.json
    song_name = data.get("song_name")
    topic = data.get("topic")
    voice = data.get("voice")
    speed = data.get("speed")
    
    if not song_name or not topic or not voice or not speed:
        return jsonify({"error": "Missing required parameters: song_name, topic, voice, or speed"}), 400

    speed_map = {
        "normal": "1.0x",
        "slow": "0.75x",
        "fast": "1.5x"
    }
    playback_speed = speed_map.get(speed, "1.0x")

    result_file = parody_generator.generate_parody_song(song_name, topic)
    if result_file:
        try:
            download_song_as_mp3.main(song_name)
            edge.main(voice=voice, speed=playback_speed)
            main.main()
            return jsonify({
                "parody_lyrics": open(result_file).read(),
                "audio_file_url": "/download_audio"
            })
        except Exception as e:
            return jsonify({"error": f"Error during audio processing: {str(e)}"}), 500
    return jsonify({"error": "Failed to generate parody lyrics"}), 500

@app.route("/download_audio")
def download_audio():
    audio_path = "output.mp3"
    if os.path.exists(audio_path):
        return send_file(audio_path, mimetype="audio/mpeg", as_attachment=False)
    return jsonify({"error": "Audio file not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
