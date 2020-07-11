import json
import requests
import logging
from details import Details
from errors import *

'''
API for DiscordRobots Bot List
Python 3.7
Version: V0.5
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

STATS_ERROR_CODES = {
    "403": "You are currently banned from discord-robots-api. Contact someone in the following discord for more information's: https://discord.gg/ExCrcDX",
    "404": "Some arguments don't seem to be right! Check them again and reach your goal!",
    "503": "Currently the api is not available because someone's working over there. For more information's, check the following discord: https://discord.gg/ExCrcDX",
    "500": "Something unexpected happened! Contact someone from the following discord server: https://discord.gg/ExCrcDX"
}

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

        assert logging_level in LOGGING_LEVELS
        logging.basicConfig(format=logging_format, datefmt=logging_datefmt, level=LOGGING_LEVELS[logging_level], filename=logging_file if logging_file else "",
                            filemode=logging_mode)

        logging.info("\nDiscordRobots object has been initialized!")

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
        url = BASE_URL + "conn/test.php?token=" + self.token

        res = requests.get(url=url, params=dict())
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
        throws an TokenIsInvalidException if there's an invalid token

        returns if user has already voted (bool)
        """

        if not self.token:
            logging.error("Hey there, it's me, the logger, just want to say, your token isn't set yet!")
            raise TokenIsInvalidException("There's no token")

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

    def send_stats(self, server_count: int, shard_count: int, user_count: int):
        """
        Sends stats to the api itself so it can work with it

        expects the following arguments:
        server_count (int) - the current sum of the guilds the bot is in
        shard_count (int)  - the current sum of the shards your bot has (if you don't use a shard-manager, this should be 1)
        user_count (int)   - the sum of all the users from your guilds

        throws TokenIsInvalidException if the token is not set yet
        throws an ErrorCodeException if something's wrong with the api or you
        """

        if not self.token:
            logging.error("Hey there, it's me, the logger, just want to say, your token isn't set yet!")
            raise TokenIsInvalidException("There's no token")

        url = BASE_URL + "/stats/send.php?token=" + self.token + "&userCount=" + str(user_count) + "&shardCount=" + str(shard_count) + "&serverCount=" + str(server_count)
        res = requests.get(url)
        data = res.json()

        if data["status"] in STATS_ERROR_CODES:
            logging.error("Hey there, it's me, the logger! Did you know, something terrible happened? No? Just read the error message in your console!")
            raise ErrorCodeException("Oopsie whoopsie, something bad just happened! The exception says: " + STATS_ERROR_CODES[data["status"]])

    def get_stats(self) -> dict:
        """
        Gets the stats that you send in with send_stats
        Note: this isn't really necessary, just an easier way to get your old stats :)

        throws TokenIsInvalidException if the token is not set yet

        returns a dict with information's about the 'server_count', 'shard_count' and 'user_count'
        """

        if not self.token:
            logging.error("Hey there, it's me, the logger, just want to say, your token isn't set yet!")
            raise TokenIsInvalidException("There's no token")

        url = BASE_URL + "/stats/get.php?token=" + self.token
        res = requests.get(url=url)
        data = res.json()

        data["server_count"] = data.pop("serverCount")
        data["shard_count"] = data.pop("shardCount")
        data["user_count"] = data.pop("userCount")
        del data["connected"]

        logging.info("Successfully gathered information's about your bot stats")

        return data

    def get_details(self) -> Details:
        """
        Gathering the details from the bot

        throws TokenIsInvalidException if the token is not set yet

        returns a Details object with the information's
        """

        if not self.token:
            logging.error("Hey there, it's me, the logger, just want to say, your token isn't set yet!")
            raise TokenIsInvalidException("There's no token")

        url = BASE_URL + "/details/test.php?token=" + self.token
        res = requests.get(url=url)
        data = res.json()

        logging.info("Successfully gathered details about your bot")

        return Details(data)