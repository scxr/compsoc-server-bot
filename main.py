from discord.ext import commands
import os
TOKEN = os.environ.get('BOT_TOKEN')
bot = commands.Bot(command_prefix='!')

cogs_to_load = [
    'cogs.hello_world',
    'cogs.upcoming_hackathons',
    'cogs.help_cog'
]


if __name__ == '__main__':
    for cog in cogs_to_load:
        bot.load_extension(cog)
        print(f'Loaded {cog}')

    bot.run(TOKEN)
