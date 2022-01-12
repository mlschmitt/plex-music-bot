# plex-bot

Script for automatically building a radio-like playlist in Plex.


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
