import discord
import asyncio

from discord.ext import commands

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"Pong! Latency: {self.bot.latency} ms")

async def setup(bot):
    await bot.add_cog(misc(bot))