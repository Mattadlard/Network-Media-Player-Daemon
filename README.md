# Network-Media-Player-Daemon
Network Media Player Daemon

# Music Daemon

Welcome to the Music Daemon project! This is an idea for mainly a handy little daemon thsy is designed to live in a Docker container, listen for music requests, and play your favorite tunes either from local files or Spotify. It supports playback on Chromecast, Sonos devices, or through a VB-CABLE audio device..

## Features

- **Local and Spotify Music Playback**: Check for local music files first. If not found, play from Spotify.
- 
- **Device Support**: Play music on Chromecast, Sonos devices, or through VB-CABLE.
- 
- **Simple Web Interface**: Control playback with a user-friendly web interface.

## Prerequisites

Before you begin, make sure you have the following:

- Docker installed on your system.
- A Spotify Developer account to get your client ID and client secret.
- Chromecast or Sonos devices on your network.
- VB-CABLE installed and configured on your system if you want to use it.

- patience as thus eas done quickly and late at night after too little coffee.

## Setup Guide

1. **Clone the Repository**: Start by cloning this repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/music-daemon.git
    cd music-daemon
    ```

2. **Create Environment Variables**: Create a `.env` file in the root directory and add your Spotify credentials.

    ```
    SPOTIPY_CLIENT_ID=your_spotify_client_id
    SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
    ```

3. **Build the Docker Image**: Use the following command to build the Docker image.

    ```bash
    docker build -t music-daemon .
    ```

4. **Run the Docker Container**: Start the container with the environment variables for Spotify.

    ```bash
    docker run -d -p 5000:5000 --env-file .env music-daemon
    ```

## Usage

Once your Docker container is up and running, follow these steps to control your music playback:

1. **Open the Web Interface**: Navigate to `http://localhost:5000` in your web browser.

2. **Select a Device**: Choose your playback device from the dropdown menu. This can be a Chromecast, a Sonos device, or any other supported device.

3. **Enter File Path or Spotify URI**:
    - **Local File**: Provide the path to the local music file you want to play.
    - **Spotify**: Enter the Spotify track URI.

4. **Play Music**: Click the "Play" button to start playing music on your selected device.

5. **Stop Music**: To stop playback, select the device and click the "Stop" button obviously.

## Additional Configuration

### VB-CABLE Setup

To use VB-CABLE, ensure it is installed and configured on your system. 

i guess follow these steps:

1. **Install VB-CABLE**: Download and install VB-CABLE from the [official website](https://www.vb-audio.com/Cable/).

2. **Configure Audio Settings**: Set your audio source (e.g., music player) to output to 'VB-CABLE Input' and your audio sink (e.g., speakers) to receive from 'VB-CABLE Output'.

### Extending Device Support

Currently, this daemon supports Chromecast and Sonos devices. If you want to add support for other network audio receivers, you can extend the code accordingly.

## Contributing

Feel free to fork this project. i am just dumping here  
