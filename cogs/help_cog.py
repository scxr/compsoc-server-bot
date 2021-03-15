import discord
from discord.ext import commands
import random
class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')
    
    @commands.command()
    async def help(self, ctx):
        help_embed = discord.Embed(title='Help', colour=random.randint(0, 0xFFFFFF))
        help_embed.add_field(name="!upcoming_hackathons", value="Shows paginated embed for upcoming hackathons from devpost")
        help_embed.set_footer(text='View my source code here : https://github.com/scxr/compsoc-server-bot')
        await ctx.send(embed=help_embed)
def setup(bot):
    bot.add_cog(HelpCog(bot))