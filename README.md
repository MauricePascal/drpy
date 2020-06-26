# DiscordRobotsAPI - Python

DiscordRobotsAPI - Python is the official Python API for DiscordRobots.
Simply it's based on requests but this API makes it easier to use and handle these requests!


## New Features!
	- V0.3.1: Added logging and changed print statements to logging statements
	- V0.3: Added Custom Exceptions
	- V0.2: Fixed Base URL Bugs
	- V0.1: Added a class and refactor the code
	


## Installation

DiscordRobotsAPI for Python needs the following packages installed:
	- Json (already in Python3.7)
	- Requests (already in Python3.7)

To install DiscordRobotsAPI for Python itself you should use pip:

```sh
$ python3 -m pip install discordrobotsapi
```

or 

```sh
$ pip install discordrobotsapi
```



## Getting Started

So, first of all, you need to import and create an discordrobotsapi object to use all functions!

```py
from discordrobotsapi import discordrobotsapi

TOKEN = "The Bot Token that your Bot currently has"

api = discordrobotsapi.DiscordRobots(TOKEN)
api.connect()
```

If you run this and nothing is printed in your console then everything is fine!



### Todo:
	- Parse the bot token directly into api.connect



### Some useful links
[DiscordRobots](https://www.keksstudios.tk/discordrobots)  
[DiscordRobotsAPI on Github](https://github.com/MauricePascal/drpy)  
[DiscordRobotsAPI for Python on Github](https://github.com/MauricePascal/drpy/tree/master/discordrobotsapi)  



### License
[MIT](https://choosealicense.com/licenses/mit/)

*Project powered by KeksStudios.tk*
