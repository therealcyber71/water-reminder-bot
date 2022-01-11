from discord.ext import commands, tasks
import randfacts
import keep_alive
bot = commands.Bot("-")
bot.remove_command("help")
target_channel_id = 739335614155194490


@bot.command()
async def ping(ctx):
    await ctx.send('Pong! :rocket: {0}'.format(round(bot.latency, 1)))


@tasks.loop(hours = 24)
async def test():
    channel = await bot.fetch_channel('739335614155194490')#water channel ID
    x = randfacts.get_fact()
    
    await channel.send("Your daily water reminder: Drink Water :potable_water:")
    await channel.send("Fact of the Day: " + x)
@bot.event
async def on_ready():
    test.start()
    
keep_alive.keep_alive() 
bot.run("Bot token")
