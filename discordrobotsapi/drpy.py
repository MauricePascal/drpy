import json
import requests
import logging

'''
API for DiscordRobots Bot List
Python 3.7
Author: Ari24
Contributors: Ari24, MauricePascal
Github: https://github.com/MauricePascal/drpy
'''

BASE_URL = "https://discordrobots-api.000webhostapp.com/"
LOGGING_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

class TokenIsInvalidException(Exception):
    pass

class IDIsInvalidException(Exception):
    pass

class InvalidArgumentException(Exception):
    pass

class DiscordRobots:
    """
    Class for DiscordRobotsAPI in Python
    Contains functions like connecting to the API, gathering information's and more
    """
    def __init__(self, logging_format='%(asctime)s - %(process)d: %(message)s', logging_datefmt="%d.%m.%Y %I:%M:%S (%p)",
                 logging_level="WARNING", logging_file=None, logging_mode="a+"):
        """
        Initiate the class and sets the default api_base_url

        positional keywords:
            - logging_format: sets the format for the logging (default is recommended)
            - logging_datefmt: sets the time format for the logging (default is recommended)
            - logging_level: sets the min. level for logging (default and "INFO" is recommended)
            - logging_file: the logging.log file
            - logging_mode: the write mode for logging into the file, default is "a+" (recommended) so it appends the current logs to the logs from earlier runs

        can throw:
            - assertion-error if logging_level isnt a real logging level
        """

        self.token = None
        self.api_base_url = BASE_URL + "conn/test.php?token="
        self.api_url = ""

        assert logging_level in LOGGING_LEVELS
        logging.basicConfig(format=logging_format, datefmt=logging_datefmt, level=LOGGING_LEVELS[logging_level], filename=logging_file if logging_file else "",
                            filemode=logging_mode)

        logging.info("DiscordRobots object has been init.")

    def connect(self, token: str) -> bool:
        """
        Connects to DiscordRobots API

        excepts the following arguments:
            - the bot's token (str)

        throws a raise TokenIsInvalidException if token is invalid

        returns a bool if the connection was successfully
        """

        if not type(token) == str:
            logging.error("Couldn't create a DiscordRobots object. Reason: Token is invalid!")
            raise TokenIsInvalidException("Token is invalid!")

        self.token = token
        self.api_url = self.api_base_url + self.token

        res = requests.get(url=self.api_url, params=dict())
        data = res.json()

        connected = data['connected']
        if not connected:
            logging.error("Failed to connect to DiscordRobots. Reason: Got an invalid Token in DiscordRobots#connect()!")
            raise TokenIsInvalidException("Token is invalid!")
        else:
            logging.info("Successfully connected to DiscordRobotsAPI with api object")
            return True

    def has_voted(self, user_id: str) -> bool:
        """
        Checks if the given user ID (str) has already voted

        excepts a user_id (str)

        throws an IDIsInvalidException if the user ID is invalid
        throws an TokenIsInvalidException if there's and invalid token

        returns if user has already voted (bool)
        """
        if not user_id or not str(user_id).isnumeric():
            logging.error("Got an invalid User ID in DiscordRobots#has_voted()")
            raise IDIsInvalidException("User ID is invalid!")

        url = BASE_URL + "votes/test.php?token=" + self.token + "&id=" + user_id
        res = requests.get(url=url)
        data = res.json()

        connected = json.dumps(data["connected"], indent=4)
        if connected == "false":
            logging.error("Failed to connect to DiscordRobots. Reason: Got an invalid Token in DiscordRobots#has_voted()!")
            raise TokenIsInvalidException("Got an invalid Token!")
        else:
            voted = json.dumps(data["isVoted"], indent=4)
            logging.info("Successfully gathered information about User having already voted!")
            return voted == "true"
