import random

from discord import Member
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: Member): # basic kick command
        sentencing = ["shall be burned at the stake!", "has been excommunicated by the Pope!", "was practicing witchcraft!", "was practicing black magic!"]
        await ctx.reply(f"{member.name} {random.choice(sentencing)}")
        await self.bot.kick(member)

    @kick.error # error handling on kick
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("you dont have perms, womp womp")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("i dont have perms bro bro, gimme perms first dud")

async def setup(bot):
    await bot.add_cog(moderation(bot))