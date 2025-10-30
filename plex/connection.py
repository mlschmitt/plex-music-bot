from plexapi.myplex import MyPlexAccount

class PlexConnection():
    def __init__(self, username=None, password=None, resource=None):
        self.username = username
        self.password = password
        self.resource = resource
        self._server = None

    @property
    def music_library(self, section_name='Music'):
        return self.library.section(section_name)

    @property
    def library(self):
        return self.server.library

    @property
    def server(self):
        if not self._server:
            self._server = self._setup_server()
        return self._server

    def _setup_server(self):
        print(f'Connecting to Plex server {self.resource}...')
        # In plex/connection.py, line 26:
        two_factor_code = input("Enter your Plex 2FA code: ")
        account = MyPlexAccount(self.username, self.password, code=two_factor_code)

        print(f'Connecting to Plex server {self.resource}... DONE.')
        return account.resource(self.resource).connect()
