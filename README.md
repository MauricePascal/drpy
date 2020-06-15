# drpy
This is the official DiscordRobotsAPI for discord.py. You can work with votes a so many more

# Overview
* [Setup](https://github.com/MauricePascal/drpy/blob/master/README.md#creating-the-discordrobotsapi-object)
* [Votes](https://github.com/MauricePascal/drpy/blob/master/README.md#votes)
* [Download](https://github.com/MauricePascal/drpy/blob/master/README.md#download)
* [Support](https://github.com/MauricePascal/drpy/blob/master/README.md#support)

## Creating the DiscordRobotsAPI Object
This is the setup for your Bot. Replace "token" with the DiscordRobots Token of your Bot
 
```java
    DiscordRobotsAPI drAPI = new DiscordRobotsAPI.Builder()
        .setToken(token)
        .build();
```

## Votes
Work with votes

```java
    String userId = [...] //User ID
    if(Votes.isVoted(userId)) {
        [...]
    }
```

## Download
The API is currently not available for download

## Support
* [Discord-Server](https://discord.gg/ExCrcDX)
* [Website](https://www.keksstudios.tk/discordrobots)
* [Documentation](#)
