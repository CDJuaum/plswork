from discord.ext import commands
import sys
from os import execl
from discord import Embed
import pickle

with open("variables.pkl", "rb") as file:
    variables = pickle.load(file)

ch = variables["ch"]
processed_streamers = variables["processed_streamers"]

class Restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
    name="restart",
    aliases=["rr"],
    help="Restarts Bot.",
    usage="restart",
    hidden=True,
)
    async def restart(self, ctx):
        if str(ctx.author.id) != ch.get_bot_owner_id():
            embed = Embed(
                title="Permission Error",
                description="You don't have permissions to use this command.",
                color=0xFF0000,
            )
            embed.set_thumbnail(url="https://i.imgur.com/lmVQboe.png")
            await ctx.send(embed=embed)
            return
        data = {"Restarted": True, "Streamers": processed_streamers}
        ch.save_to_temp_json(data)
        embed = Embed(
            title="Restarting",
            description="Bot is restarting...",
            color=0x00FF00,
        )
        embed.set_thumbnail(url="https://i.imgur.com/TavP95o.png")
        await ctx.send(embed=embed)

        python = sys.executable
        print(python)
        execl(python, python, *sys.argv)

async def setup(bot):
    await bot.add_cog(Restart(bot))