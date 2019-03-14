# coding=utf-8
# Works with Python 3.6
import discord
import infoFinder

TOKEN = '####'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    content_lowercase = message.content.lower()

    if content_lowercase.startswith('-help'):
        embed = discord.Embed(color=0xDC4806)
        embed.add_field(name="Bot Commands",
                        value="Type `-hello` for a greeting \n"
                              "Type `-X` to know more about X", inline=False)

        await client.send_message(message.channel, embed=embed)

    elif content_lowercase.startswith('-hello'):
        msg = '...oh... eh... Hey!'.format(message)
        await client.send_message(message.channel, msg)

    elif content_lowercase.startswith('-getall '):
        content = message.content.replace("-getall ", "")

        wholemsg = infoFinder.get_info(content)

        for paragraph in wholemsg:
            if len(paragraph) < 2000:
                await client.send_message(message.channel, paragraph)

    elif content_lowercase.startswith('-'):
        content = message.content.replace("-", "")

        wholemsg = infoFinder.get_info(content)

        if len(wholemsg) > 20:
            await client.send_message(message.channel, "Well... I have a lot of information on that!\n"
                                                       "Could you be more precise?\n"
                                                       "Or, if that's really what you want, type `-GETALL X`")
        else:
            for paragraph in wholemsg:
                if len(paragraph) < 2000:
                    await client.send_message(message.channel, paragraph)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    # Set status as "reading a book"
    await client.change_presence(game=discord.Game(name="Reading a book | -help"))


client.run(TOKEN)

