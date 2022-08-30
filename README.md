# Spotify-bot

## Introduction

This project aims to create Spotify's playlists based on the user's liked tracks and liked artists. This project uses the Spotify API and the Spotify Web API to do so.

## Installation

To install the project, you need to install the dependencies written in the `requirements.txt` file. To do so, you can use the following command:

```bash
pip install -r requirements.txt
```

> It is required to have Python and `pip` installed on your device.

## Usage

To use this project, you need to create/have an account on Spotify.

Then, you need create a new file called `credentials.py`, in the folder `utils/`, with the following content:

```python
SPOTIFY_CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_AUTHORIZATION_TOKEN = "YOUR_SPOTIFY_AUTHORIZATION_TOKEN"
```

> You can find the credentials on the Spotify developer website.