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

After everything is done, you can run the project with the following command:

```bash
python main.py
```

It will create so many playlists based on the user's liked artists and tracks that are listed in the file `playlists.txt`.

Those playlists may be categorized as that:
- Week's releases: the playlists will contain the tracks that have been released this week from the followed artists.
- Years' releases: the playlists will contain the user liked tracks that have been released this year, this 3 last years and the 5 last years.
- Epochs releases: the playlists will contain the user liked tracks that have been released every decades and every years starting from 2010.
- Genres releases: the playlists will contain the user liked tracks that are in quite the same genre.