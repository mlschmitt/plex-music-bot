import argparse
import sys

from plex_playlist_builder import PlexPlaylistBuilder


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('--username', '-u', help='Plex account username/email', required=True, type=str)
	parser.add_argument('--password', '-p', help='Plex account password', required=True, type=str)
	parser.add_argument('--resource', '-r', help='Plex server resource name', required=True, type=str)
	parser.add_argument('--playlist_title', '-t', help='Name of target playlist to update', default='Music Bot', type=str)
	parser.add_argument('--track_count', '-c', help='Number of tracks to add to playlist', default=50, type=int)

	args = parser.parse_args()

	print(f'Generating playlist named "{args.playlist_title}" with {args.track_count} tracks...')

	PlexPlaylistBuilder(
	    username=args.username,
	    password=args.password,
	    resource=args.resource
	).build_playlist(
	    playlist_title=args.playlist_title,
	    track_count=int(args.track_count)
	)