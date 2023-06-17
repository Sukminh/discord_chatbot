from dotenv import load_dotenv
import os
load_dotenv()
import discord
import response

async def send_message(message, user_message, is_private):
    try:
        res = response.handle_response(user_message)
        await message.author.send(res) if is_private else await message.channel.send(res)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = os.getenv("TOKEN")
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_mes = str(message.content)
        chan = str(message.channel)

        print(f"{username} said: '{user_mes}' ({chan})")

        if user_mes[0] == "?":
            user_mes = user_mes[1:]
            await send_message(message, user_mes, is_private=True)
        else:
            await send_message(message, user_mes, is_private=False)

    client.run(TOKEN)