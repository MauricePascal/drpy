import json
import requests

'''
API for DiscordRobots Bot List
Python 3.7
Author: <Author>
'''

BASE_URL = "https://discordrobots-api.000webhostapp.com/"

class TokenIsInvalidException(Exception):
    pass

class IDIsInvalidException(Exception):
    pass

class DiscordRobots:
    """
    Class for DiscordRobotsAPI in Python
    Contains functions like connecting to the API, gathering informations and more
    """
    def __init__(self, token: str):
        """
        Initiate the class
        expects the following arguments: token (str)

        throws a TokenIsInvalidException if the token is invalid
        """

        if not type(token) == str:
            raise TokenIsInvalidException("Token is invalid!")

        self.token = token
        self.api_url = BASE_URL + "conn/test.php?token=" + self.token

    def connect(self):
        """
        Connects to DiscordRobots API

        throws a raise TokenIsInvalidException if token is invalid
        """
        res = requests.get(url=self.api_url, params=dict())
        data = res.json()

        connected = data['connected']
        if not connected:
            raise TokenIsInvalidException("Token is invalid!")
        else:
            print("Successfully connected to API!")

    def has_voted(self, user_id: str) -> bool:
        """
        Checks if the given user ID (str) has already voted

        excepts a user_id (str)

        throws an IDIsInvalidException if the user ID is invalid
        throws an TokenIsInvalidException if there's and invalid token

        returns if user has already voted (bool)
        """
        if not user_id:
            raise IDIsInvalidException("User ID is invalid!")

        url = BASE_URL + "votes/test.php?token=" + self.token + "&id=" + user_id
        print(url)
        res = requests.get(url=url, params=dict())
        data = res.json()

        connected = json.dumps(data["connected"], indent=4)
        if connected == "false":
            raise TokenIsInvalidException("Got an invalid Token!")
        else:
            voted = json.dumps(data["isVoted"], indent=4)
            return voted == "true"
