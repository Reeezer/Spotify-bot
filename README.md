# Spotify-bot

## Introduction

The Spotify-bot project is designed to create playlists on Spotify based on the user's liked tracks and artists. This project utilizes the Spotify API and Spotify Web API to accomplish this task.

## Installation

To install the project, you need to install the dependencies listed in the `requirements.txt` file. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

> Please ensure that you have Python and `pip` installed on your device.

## Setup

To use this project, you need to create or have an existing Spotify account.

Next, you need to create a Spotify app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and obtain the `Client ID` and `Client Secret` from the app's dashboard page.

Afterward, you need to export the `Client ID` and `Client Secret` as environment variables:

```bash
export SPOTIPY_CLIENT_ID=<your_client_id>
export SPOTIPY_CLIENT_SECRET=<your_client_secret>
```

## Usage

Once the setup is complete, you can run the project using the following command:

```bash
python main.py
```

This will generate multiple playlists based on the user's liked artists and tracks listed in the `playlists.txt` file.

The playlists are categorized as follows:
- Week's releases: These playlists contain tracks released by the user's followed artists within the current week.
- Years' releases: These playlists include user-liked tracks released within the current year, the past 3 years, and the past 5 years.
- Epochs releases: These playlists consist of user-liked tracks released every decade and every year starting from 2010.
- Genres releases: These playlists comprise user-liked tracks that belong to similar genres.

> You can launch each category of playlists separately using their respective scripts, such as `main_<category>.py`.
