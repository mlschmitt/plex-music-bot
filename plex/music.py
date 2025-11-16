from functools import cached_property
from plexapi.exceptions import NotFound


class PlexMusic():
	def __init__(self, plex_library):
		self.library = plex_library

	# Methods

	def recently_added_tracks(self, limit: int = 50, filters: dict = {}):
		return self.library_search(
			sort_value='addedAt:desc',
			media_type='track',
			limit=limit,
			filters=filters,
		)

	def recently_played_tracks(self, limit: int = 50, filters: dict = {}):
		return self.library_search(
			sort_value='lastViewedAt:desc',
			media_type='track',
			limit=limit,
			filters=filters,
		)

	def top_played_tracks(self, limit: int = 50, filters: dict = {}):
		return self.library_search(
			sort_value='viewCount:desc',
			media_type='track',
			limit=limit,
			filters=filters
		)

	def least_played_tracks(self, limit: int = 50, filters: dict = {}):
		return self.library_search(
			sort_value='viewCount:asc',
			media_type='track',
			limit=limit,
			filters=filters,
		)

	def all_tracks(self):
		return self.library.all(libtype='track')

	def all_artists(self):
		return self.library.all(libtype='artist')

	def library_search(
		self,
		sort_value: str,
		media_type: str,
		limit: int,
		filters: dict = {}
	):
		return self.library.search(
			sort=sort_value,
			libtype=media_type,
			limit=limit,
			filters=filters,
		)

	def replace_playlist_tracks(self, playlist_title, playlist_songs):
		target_playlist = self.get_playlist(playlist_title)
		if not target_playlist:
			self.library.createPlaylist(playlist_title, items=playlist_songs)
		else:
			target_playlist.removeItems(target_playlist.items())
			target_playlist.addItems(playlist_songs)

	def get_playlist(self, playlist_title):
		try:
			return self.library.playlist(playlist_title)
		except NotFound:
			return None
	
	def edit_playlist_description(self, playlist_title: str, playlist_description: str):
		target_playlist = self.get_playlist(playlist_title)
		if target_playlist:
			target_playlist.edit(summary=playlist_description)

	# Properties

	@cached_property
	def total_track_count(self):
		return self.library.totalViewSize(libtype='track')

	@cached_property
	def total_artist_count(self):
		return self.library.totalViewSize(libtype='artist')
