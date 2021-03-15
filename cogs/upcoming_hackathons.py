import requests
import discord
from discord.ext import commands
import paginator
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
import os
class UpcomingHackathons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def tst(self, ctx):
        pass
    
    @commands.command()
    async def upcoming_hackathons(self, ctx):
        await ctx.send('This could take a little while, please allow up to a minute.')
        options = webdriver.ChromeOptions()
        options.headless = True
        options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), options=options)
        driver.get('https://devpost.com/hackathons?order_by=deadline&status[]=upcoming')
        soup = BeautifulSoup(driver.page_source)
        driver.close()
        hackathons = soup.find_all("div", {"class":"main-content"})
        hackathon_list = []
        for hackathon in hackathons:
            #thumbnail = hackathon.find_all("img",{"class":"hackathon-thumbnail"})[0]
            
            actual_thumbnail = ''
            title = hackathon.find_all("h3", {"class":"mb-4"})[0].text
            sub_date = hackathon.find_all("div", {"class":"submission-period"})[0].text
            prizes = hackathon.find_all("span", {"class":"prize-amount"})[0].text
            hackathon_scraped = (actual_thumbnail, title, sub_date, prizes)
            hackathon_list.append(hackathon_scraped)
        embeds_for_paging = []
        for hackathon in hackathon_list:
            print(hackathon) 
            embed=discord.Embed(title=hackathon[1], color=0x44885e)
            embed.set_author(name="Bot made by XO")
            #embed.set_thumbnail(url=hackathon[0])
            embed.add_field(name="Prize Pool", value=hackathon[3], inline=False)
            embed.add_field(name="Submission Date", value=hackathon[2], inline=True)
            embeds_for_paging.append(embed)
            embed.set_footer(text="View my source here : https://github.com/scxr/compsoc-server-bot")
        print(embeds_for_paging)
        mypaginator = paginator.AutoEmbedPaginator(ctx)
        
        await mypaginator.run(embeds_for_paging)
def setup(bot):
    bot.add_cog(UpcomingHackathons(bot))