"""
Helper class for details because I don't like the dict of the API ¯\\_(ツ)_/¯
"""

class Details:
    def __init__(self, data: dict):
        self.__data = data
        self.__connected = data["connected"]

        self.description = data["description"]
        self.library = data["library"]
        self.invite_url = data["invite"]
        self.owner_id = int(data["owner"])
        self.current_votes = int(data["currentVotes"])
        self.support_server_url = data["supportServer"]
