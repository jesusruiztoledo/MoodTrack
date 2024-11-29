from flask import Flask, render_template, request, jsonify
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from transformers import pipeline
import requests
import re
import os

app = Flask(__name__)

# Configuración de API de Spotify
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "5d32087181b644f695c4ea5ac242f131")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "544e3f9f0cec40a8a2347bd4c70101bb")
sp = Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# Cargar modelo de análisis de sentimientos
classifier = pipeline("sentiment-analysis")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user", methods=["POST"])
def user():
    user_id = request.form.get("user_id")
    if not user_id:
        return jsonify({"error": "No se proporcionó un ID de playlist"}), 400
    user_list = sp.user_playlists(user_id)
    results = []
    for playlist in user_list['items']:
        results.append({'Nombre': playlist['name'], 'ID': playlist['id']})
    return render_template("user.html", results=results)

@app.route("/analyze", methods=["POST"])
def analyze():
    playlist_id = request.form.get("playlist_id")
    if not playlist_id:
        return jsonify({"error": "No se proporcionó un ID de playlist"}), 400

    # Obtener canciones de la playlist
    try:
        results = sp.playlist_tracks(playlist_id)
        playlist = [
            {"name": track["track"]["name"], "artist": track["track"]["artists"][0]["name"]}
            for track in results["items"]
        ]
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Obtener letras de canciones
    lyrics_url = "https://api.lyrics.ovh/v1/"
    clean_lyrics = []
    for song in playlist:
        response = requests.get(lyrics_url + f"{song['artist']}/{song['name']}")
        if response.status_code == 200:
            lyrics = response.json().get("lyrics", "")
            lyrics = re.sub(r"[\n\r]", " ", lyrics)
            clean_lyrics.append(lyrics[:512])

    # Análisis de sentimientos
    sentiments = [classifier(lyric)[0] for lyric in clean_lyrics]
    results = [
        {
            "song": song["name"], 
            "artist": song["artist"], 
            "sentiment": "Triste" if sentiment["label"] == "NEGATIVE" else "Feliz", 
            "score": sentiment["score"]
        }
        for song, sentiment in zip(playlist, sentiments)
    ]

    return render_template("result.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
