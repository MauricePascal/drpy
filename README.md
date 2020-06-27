# DiscordRobotsAPI - Python

DiscordRobotsAPI - Python is the official Python API for DiscordRobots.
Simply it's based on requests but this API makes it easier to use and handle these requests!


## New Features!
	- V.0.4.1: Changed name from discordrobotsapi.py to drpy.py to make imports easier
	- V.0.4: Token must be directly parsed into api#connect()
	- V0.3.1: Added logging and changed print statements to logging statements
	- V0.3: Added Custom Exceptions
	- V0.2: Fixed Base URL Bugs
	- V0.1: Added a class and refactor the code
	


## Installation

DiscordRobotsAPI for Python needs the following packages installed:  
	- Json (already in Python3.7)  
	- Requests (already in Python3.7)  
	- Logging (already in Python3.7)  
  
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
from discordrobotsapi.drpy import DiscordRobots

TOKEN = "The Bot Token that your Bot currently has"

api = DiscordRobots()
api.connect(TOKEN)
```

If you run this and nothing is printed in your console then everything is fine!



### Todo:
	- Currently no ToDos
  
  
## License
[MIT](https://choosealicense.com/licenses/mit/)
  
  
  
### Some useful links
[DiscordRobots](https://www.keksstudios.tk/discordrobots)  
[DiscordRobotsAPI on Github](https://github.com/MauricePascal/drpy)  
[DiscordRobotsAPI for Python on Github](https://github.com/MauricePascal/drpy/tree/master/discordrobotsapi)  
  
  
*Project powered by KeksStudios.tk*
