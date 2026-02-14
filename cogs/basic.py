from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}! 😎")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! 🏓 {round(self.bot.latency*1000)}ms")

def setup(bot):
    bot.add_cog(Basic(bot))
