import re, requests, json, random, time, datetime, os, glob, asyncio, discord, pymysql
import quadra_config
from quadra_config import db_connect 
# import threading
from quadra_log_module import log_append

DATABASE = db_connect()
back_time = 6

# def resync_db(sql):
#    curs = sql.cursor()
#    curs.execute("SELECT 1 LIMIT 1")
#    threading.Timer(60 * 60 * back_time, resync_db(DATABASE)).start()

# resync_db(DATABASE)

client = discord.Client()


@client.event
async def on_ready():
    log_append(text="Bot is online now")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('4!'):
        log_append(
            user=message.author,
            guild=message.guild,
            category="Listener",
            text=message.content)

    if message.content.startswith('4!hello'):
        await message.channel.send('Hello!')

client.run(quadra_config.BOT_TOKEN)