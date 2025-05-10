from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Responds with 'ワンダーホイ！！！'"""
        await ctx.send("ワンダーホイ！！！")

def setup(bot):
    bot.add_cog(General(bot))
