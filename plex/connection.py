from plexapi.myplex import MyPlexAccount, PlexServer

class PlexConnection():
    def __init__(self, username=None, password=None, resource=None, server_url=None, token=None):
        self.username = username
        self.password = password
        self.resource = resource
        self.server_url = server_url
        self.token = token
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

        # Use token if available, otherwise fall back to 2FA flow
        if self.token:
            return PlexServer(f'http://{self.server_url}:32400', token=self.token)
        else:
            two_factor_code = input("Enter your Plex 2FA code: ")
            account = MyPlexAccount(self.username, self.password, code=two_factor_code)
            return account.resource(self.resource).connect()
