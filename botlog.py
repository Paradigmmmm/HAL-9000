import pickle
async def botlog(subcmd):
    if subcmd=="channel":
        msgauth1 = message.author
        message.channel.send("What channel would you like log messages to be posted in?")
        botlogchannel = await channel.history().find(lambda m: m.author.id == msgauth1)
        guildchannellist = pickle.load( open( "guildchannellist", "rb" ))
        guildchannellist.update({message.guild : botlogchannel})
        pickle.dump(guildchannellist, open("guildchannellist", "wb"))
cmds = {"botlog": ("configures botlogger."))
desc = "The Botlogger module of HAL."
