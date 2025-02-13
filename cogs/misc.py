import discord
import asyncio

from discord.ext import commands

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"Pong! Latency: {self.bot.latency*1000} ms")

    @commands.command()
    async def greet(self, ctx):
        await ctx.reply(f"No time for salutations, {ctx.author.name}! There are still heretics to be expelled!")

async def setup(bot):
    await bot.add_cog(misc(bot))