# Plex Music Bot

Python scripts for automatically building radio-like music playlists in Plex.

<img src="plex_music_bot_readme_screenshot.png" align="center" alt="Example Plex Music Bot playlist" width="80%">


## Getting Started

Install requirements with pip: `pip install -r requirements.txt`


## Example Usage

```
from plex_playlist_builder import PlexPlaylistBuilder

username = "USERNAME"
password = "PASSWORD"
resource = "plex_server"
PlexPlaylistBuilder(
	username=username, password=password, resource=resource
).build_playlist(
	playlist_title='Cool Playlist', track_count=300
)
```
