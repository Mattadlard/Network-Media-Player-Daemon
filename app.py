import os
import time
import pychromecast
import soco
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Spotify setup
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = 'http://localhost:5000/callback'

# Initialize Spotify client
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                    client_secret=SPOTIPY_CLIENT_SECRET,
                                                    redirect_uri=SPOTIPY_REDIRECT_URI,
                                                    scope='user-library-read,user-read-playback-state,user-modify-playback-state'))

def discover_devices():
    chromecasts, _ = pychromecast.get_chromecasts()
    sonos_devices = soco.discover()
    devices = [cc.device.friendly_name for cc in chromecasts]
    if sonos_devices:
        devices.extend([device.player_name for device in sonos_devices])
    return devices

def play_music(device_name, track_uri=None, file_path=None):
    if file_path:
        if 'chromecast' in device_name.lower():
            play_music_chromecast(device_name, file_path)
        else:
            play_music_sonos(device_name, file_path)
    elif track_uri:
        play_music_spotify(device_name, track_uri)

def play_music_chromecast(device_name, file_path):
    chromecasts, _ = pychromecast.get_chromecasts()
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == device_name)
    cast.wait()
    mc = cast.media_controller
    mc.play_media(file_path, "audio/mp3")
    mc.block_until_active()
    while mc.status.player_state == "PLAYING":
        time.sleep(1)
    mc.stop()
    cast.disconnect()

def play_music_sonos(device_name, file_path):
    sonos_devices = soco.discover()
    if sonos_devices:
        device = next(dev for dev in sonos_devices if dev.player_name == device_name)
        device.play_uri(file_path)

def play_music_spotify(device_name, track_uri):
    if 'chromecast' in device_name.lower():
        # Implement Spotify playback on Chromecast
        pass
    else:
        # Implement Spotify playback on other devices
        pass

@app.route('/')
def index():
    devices = discover_devices()
    return render_template('index.html', devices=devices)

@app.route('/play', methods=['POST'])
def play():
    device_name = request.form['device_name']
    file_path = request.form['file_path']
    track_uri = request.form['track_uri']
    play_music(device_name, track_uri, file_path)
    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop():
    device_name = request.form['device_name']
    if 'chromecast' in device_name.lower():
        stop_music_chromecast(device_name)
    else:
        stop_music_sonos(device_name)
    return redirect(url_for('index'))

# Placeholder for functions to be implemented
def get_music_metadata():
    pass

def get_album_images():
    pass

def configure_vb_cable():
    pass

configure_vb_cable()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
