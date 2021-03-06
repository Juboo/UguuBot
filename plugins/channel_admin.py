# Plugin made by Lukeroge and neersighted
from util import hook


@hook.command(channeladminonly=True)
def topic(inp, conn=None, chan=None, notice=None):
    "topic [channel] <topic> -- Change the topic of a channel."
    message = inp
    inp = inp.split(" ")
    if inp[0][0] == "#":
        message = message.replace(inp[0],'').strip()
        out = "TOPIC %s :%s" % (inp[0], message)
    else:
        out = "TOPIC %s :%s" % (chan, message)
    conn.send(out)


@hook.command('k',channeladminonly=True)
@hook.command(channeladminonly=True)
def kick(inp, chan=None, conn=None, notice=None):
    "kick [channel] <user> [reason] -- Makes the bot kick <user> in [channel] "\
    "If [channel] is blank the bot will kick the <user> in "\
    "the channel the command was used in."
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "KICK %s %s" % (chan, user)
        if len(inp) > 2:
            reason = ""
            for x in inp[2:]:
                reason = reason + x + " "
            reason = reason[:-1]
            out = out + " :" + reason
    else:
        user = inp[0]
        out = "KICK %s %s" % (chan, user)
        if len(inp) > 1:
            reason = ""
            for x in inp[1:]:
                reason = reason + x + " "
            reason = reason[:-1]
            out = out + " :" + reason

    notice("Attempting to kick %s from %s..." % (user, chan))
    conn.send(out)


@hook.command(channeladminonly=True)
def op(inp, conn=None, chan=None, notice=None):
    "op [channel] <user> -- Makes the bot op <user> in [channel]. "\
    "If [channel] is blank the bot will op <user> in "\
    "the channel the command was used in."
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s +o %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s +o %s" % (chan, user)
    notice("Attempting to op %s from %s..." % (user, chan))
    conn.send(out)


@hook.command(channeladminonly=True)
def deop(inp, conn=None, chan=None, notice=None):
    "deop [channel] <user> -- Makes the bot deop <user> in [channel]. "\
    "If [channel] is blank the bot will deop <user> in "\
    "the channel the command was used in."
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s -o %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s -o %s" % (chan, user)
    notice("Attempting to deop %s from %s..." % (user, chan))
    conn.send(out)


@hook.command(channeladminonly=True,autohelp=False)
def up(inp, conn=None, chan=None, notice=None, user=None):
    "up -- Makes the bot op you in [channel]. "\
    "If [channel] is blank the bot will op you in "\
    "the channel the command was used in."
    out = u"MODE %s +o %s" % (chan, user.replace('~',''))
    notice("Attempting to op %s from %s..." % (user,chan))
    conn.send(out)


@hook.command(channeladminonly=True,autohelp=False)
def down(inp, conn=None, chan=None, notice=None, user=None):
    "down -- Makes the bot deop you in [channel]. "\
    "If [channel] is blank the bot will op you in "\
    "the channel the command was used in."
    out = "MODE %s -o %s" % (chan, user.replace('~',''))
    notice("Attempting to deop %s from %s..." % (user,chan))
    conn.send(out)


@hook.command(channeladminonly=True)
def ban(inp, conn=None, chan=None, notice=None):
    "ban [channel] <user> -- Makes the bot ban <user> in [channel]. "\
    "If [channel] is blank the bot will ban <user> in "\
    "the channel the command was used in."
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s +b %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s +b %s" % (chan, user)
    notice("Attempting to ban %s from %s..." % (user, chan))
    conn.send(out)


@hook.command(channeladminonly=True)
def unban(inp, conn=None, chan=None, notice=None):
    "unban [channel] <user> -- Makes the bot unban <user> in [channel]. "\
    "If [channel] is blank the bot will unban <user> in "\
    "the channel the command was used in."
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s -b %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s -b %s" % (chan, user)
    notice("Attempting to unban %s from %s..." % (user, chan))
    conn.send(out)


@hook.command('kb',channeladminonly=True)
@hook.command(channeladminonly=True)
def kickban(inp, chan=None, conn=None, notice=None):
    "kickban [channel] <user> [reason] -- Makes the bot kickban <user> in [channel] "\
    "If [channel] is blank the bot will kickban the <user> in "\
    "the channel the command was used in."
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out1 = "MODE %s +b %s" % (chan, user)
        out2 = "KICK %s %s" % (chan, user)
        if len(inp) > 2:
            reason = ""
            for x in inp[2:]:
                reason = reason + x + " "
            reason = reason[:-1]
            out = out + " :" + reason
    else:
        user = inp[0]
        out1 = "MODE %s +b %s" % (chan, user)
        out2 = "KICK %s %s" % (chan, user)
        if len(inp) > 1:
            reason = ""
            for x in inp[1:]:
                reason = reason + x + " "
            reason = reason[:-1]
            out = out + " :" + reason

    notice("Attempting to kickban %s from %s..." % (user, chan))
    conn.send(out1)
    conn.send(out2)

@hook.command(channeladminonly=True)
def enable(inp, conn=None, chan=None, notice=None, bot=None):
    "enable [channel] <commands|all> -- Enables commands for a channel." \
    "(you can add/delete multiple commands at once)"
    inp = inp.lower()
    if inp[0][0] == "#": 
        chan = inp.split()[0]
        inp = inp.replace(chan,'').strip()
    channel = chan.lower()
    targets = inp.split()[0:]

    try: bot.channelconfig[channel]
    except: bot.channelconfig[channel] = {}

    try: 
        disabled_commands = bot.channelconfig[channel]['disabled_commands']
    except: 
        disabled_commands = []
        bot.channelconfig[channel]['disabled_commands'] = disabled_commands

    if 'all' in targets:
       notice("All commands are now enabled on %s." % chan)
       bot.channelconfig[chan]['disabled_commands'] = []
    else:
        for target in targets:
            if target in disabled_commands:
                notice("%s is now enabled on %s." % (target,chan))
                bot.channelconfig[channel]['disabled_commands'].remove(target)
            else:
                notice("%s is not disabled on %s." % (target,chan))
    bot.channelconfig.write()
    return

@hook.command(channeladminonly=True)
def disable(inp, conn=None, chan=None, notice=None, bot=None):
    "disable [channel] <commands> -- Disables commands for a channel." \
    "(you can add/delete multiple commands at once)"
    inp = inp.lower()
    if inp[0][0] == "#": 
        chan = inp.split()[0]
        inp = inp.replace(chan,'').strip()
    channel = chan.lower()
    targets = inp.split()[0:]

    try: bot.channelconfig[channel]
    except: bot.channelconfig[channel] = {}

    try:
        disabled_commands = bot.channelconfig[channel]['disabled_commands']
    except: 
        disabled_commands = []
        bot.channelconfig[channel]['disabled_commands'] = disabled_commands

    for target in targets:
        if target in disabled_commands:
            notice("%s is already disabled on %s." % (target,chan))
        else:
            notice("%s is now disabled on %s." % (target,chan))
            bot.channelconfig[channel]['disabled_commands'].append(target)
    bot.channelconfig.write()
    return


@hook.command(autohelp=False,channeladminonly=True)
def disabled(inp, chan=None, notice=None, bot=None):
    "disabled -- Lists channels's disabled commands."
    if bot.channelconfig[chan.lower()]['disabled_commands']:
        notice("Disabled on %s: %s." % (chan, ", ".join(bot.channelconfig[chan]['disabled_commands'])))
    else:
        notice("There is nothing disabled on %s." % chan)
    return