import os
import pychromecast
import soco
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, render_template, redirect, url_for
import asyncio
from devices import DeviceManager
from playback import PlaybackManager

# Flask app setup
app = Flask(__name__)

# Spotify setup
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = 'http://localhost:5000/callback'

# Initialize Spotify client
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope='user-library-read,user-read-playback-state,user-modify-playback-state'
))

# Device and Playback Manager Instances
device_manager = DeviceManager()
playback_manager = PlaybackManager()

# Discover devices at the start
device_manager.discover_devices()

@app.route('/')
def index():
    devices = device_manager.get_all_devices()
    return render_template('index.html', devices=[d['name'] for d in devices])

@app.route('/play', methods=['POST'])
def play():
    device_name = request.form['device_name']
    file_path = request.form['file_path']
    track_uri = request.form['track_uri']

    device_info = next((d for d in device_manager.get_all_devices() if d['name'] == device_name), None)
    if device_info:
        playback_manager.play_on_device(device_info, file_path, track_uri)
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'device not found'}), 404

@app.route('/stop', methods=['POST'])
def stop():
    device_name = request.form['device_name']
    device_info = next((d for d in device_manager.get_all_devices() if d['name'] == device_name), None)
    if device_info:
        playback_manager.stop_device(device_info)
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'device not found'}), 404

def configure_vb_cable():
    # Placeholder function for configuring VB Cable (if applicable)
    pass

configure_vb_cable()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
