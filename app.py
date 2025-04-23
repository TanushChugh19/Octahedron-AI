import os
import time
from datetime import datetime as dt

import discord
import ollama
import requests as r
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="*", intents=intents)
bot.remove_command("help")

embed_colors = {
    "Default": 0,
    "Aqua": 1752220,
    "Dark Aqua": 1146986,
    "Green": 5763719,
    "Dark Green": 2067276,
    "Blue": 3447003,
    "Dark Blue": 2123412,
    "Purple": 10181046,
    "Dark Purple": 7419530,
    "Gold": 15844367,
    "Orange": 15105570,
    "Red": 15548997,
    "Dark Red": 10038562,
    "Grey": 9807270,
    "Dark Grey": 9936031,
    "Light Grey": 12370112,
    "Navy": 3426654,
    "Yellow": 16776960,
    "Blurple (Discord)": 5793266,
    "White": 16777215,
}


class EmbedButtons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(
            discord.ui.Button(
                label="Become a premium member 👑",
                style=discord.ButtonStyle.primary,
                url="https://example.com",
            )
        )
        self.add_item(
            discord.ui.Button(
                label="Support Team 🧑‍💼",
                style=discord.ButtonStyle.secondary,
                url="https://example.com",
            )
        )


def getTimeOfAnyCity(city):
    url = f"http://api.timezonedb.com/v2.1/get-time-zone?key={os.getenv("API_KEY")}&format=json&by=zone&zone={city}"
    response = r.get(url).json()

    if response.get("status") != "OK":
        return f"Error: Couldn't retrieve time for {city}. Check API response."

    timestamp = response.get("formatted")
    if response.get("status") != "OK":
        return f"Error: Invalid time data for {city}."

    d_t = dt.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    format_time = d_t.strftime("%I:%M %p | %A, %d %B %Y")

    return f"Time {city}: {format_time}"


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Game(
            name="Octahedron AI | *help",
            platform="Xbox",
            assets={
                "large_image": "1364584978637389844",
                "small_image": "1364584978637389844",
            },
        )
    )
    print(f"Bot is ready as {bot.user.name}")
    print(f"The following commands are loaded: {bot.commands}")


@bot.command(name="help")
async def hello(ctx, include_buttons: bool = True):
    async with ctx.typing():
        list_ofCommands = [
            "*help (List all commands)",
            "*hello (Greet the bot)",
            "*hi (Greet the bot)",
            "*oct (Send a prompt)",
            "*summarise (Summarise last 10 messages)",
            '*describe (Use Octahedron\'s cutting edge image recognition tech to identify images. You can put a prompt after the !describe command to explain the AI the way of description. For example: !describe in a poetic way. If no promp is given then the default is "describe consicely")',
            "*local (Allows you to see local date and time)",
            "*code (Write code in Java, C#, C, C++, Python and JavaScript. It must be within 1983 characters, limit increasing soon with more languages on the way!)",
            "*zones (Give a list of common time zones with time of mentioned zone. For example: *zones IST for India time | by default it is UTC)",
            "*rag (Give Octahedron access to internet's latest data. With !oct it uses training data that goes upto December 2023) 💸 Feature is paid",
            "*imagegen (Generate unique images with Octahedron) 💸 Feature is paid",
        ]
        finalCommands = "\n".join(
            f"{index+1}. {command}" for index, command in enumerate(list_ofCommands)
        )
        embed_cmd = discord.Embed(
            title="Octahedron's response:",
            description=f"{finalCommands}",
            color=embed_colors["White"],
        )
        embed_cmd.set_footer(
            text="I am an AI large language model made by Tanush Chugh 🥳."
        )
        if include_buttons:
            await ctx.reply(embed=embed_cmd, view=EmbedButtons())
        else:
            await ctx.reply(embed=embed_cmd)


@bot.command(name="rag")
async def rag(ctx, *, message="news today", include_buttons: bool = True):
    async with ctx.typing():
        embed_rag = discord.Embed(
            title="Octahedron's response:",
            description=f'The message "{message}" can\'t be searched as this feature is for premium users. Please pay ₹299/month or ₹2999/year 💸',
            color=embed_colors["White"],
        )
        embed_rag.set_footer(
            text="I am an AI large language model made by Tanush Chugh 🥳."
        )
        if include_buttons:
            await ctx.reply(embed=embed_rag, view=EmbedButtons())
        else:
            await ctx.reply(embed=embed_rag)


@bot.command(name="imagegen")
async def imagegen(ctx, *, message="cat", include_buttons: bool = True):
    async with ctx.typing():
        embed_img = discord.Embed(
            title="Octahedron's response:",
            description=f'The image of "{message}" can\'t be searched as this feature is for premium users. Please pay ₹299/month or ₹2999/year 💸',
            color=embed_colors["White"],
        )
        embed_img.set_footer(
            text="I am an AI large language model made by Tanush Chugh 🥳."
        )
        if include_buttons:
            await ctx.reply(embed=embed_img, view=EmbedButtons())
        else:
            await ctx.reply(embed=embed_img)


@bot.command(name="hello")
async def hello(ctx, include_buttons: bool = True):
    async with ctx.typing():
        embed_hello = discord.Embed(
            title="Octahedron's response:",
            description="Nice to meet you! My name is Octahedron, and I'll do my best to assist you with your questions. What's on your mind?",
            color=embed_colors["White"],
        )
        embed_hello.set_footer(
            text="I am an AI large language model made by Tanush Chugh 🥳."
        )
        if include_buttons:
            await ctx.reply(embed=embed_hello, view=EmbedButtons())
        else:
            await ctx.reply(embed=embed_hello)


@bot.command(name="hi")
async def hello(ctx, include_buttons: bool = True):
    async with ctx.typing():
        embed_hi = discord.Embed(
            title="Octahedron's response:",
            description="Hello! What's on your mind? Need some assistance with something?",
            color=embed_colors["White"],
        )
        embed_hi.set_footer(
            text="I am an AI large language model made by Tanush Chugh 🥳."
        )
        if include_buttons:
            await ctx.reply(embed=embed_hi, view=EmbedButtons())
        else:
            await ctx.reply(embed=embed_hi)


@bot.command(name="local")
async def local(ctx, include_buttons: bool = True):
    async with ctx.typing():
        current_date_time = time.strftime("%I:%M %p | %A, %d %B %Y", time.localtime())
        embed_time = discord.Embed(
            title="Local date and time",
            description=f"{current_date_time}",
            color=embed_colors["White"],
        )
        embed_time.set_footer(
            text="I am an AI large language model made by Tanush Chugh 🥳."
        )
        if include_buttons:
            await ctx.reply(embed=embed_time, view=EmbedButtons())
        else:
            await ctx.reply(embed=embed_time)


@bot.command(name="zones")
async def time_zones(ctx, *, message="Etc/UTC", include_buttons: bool = True):
    async with ctx.typing():
        if "error" in message.lower():
            embed_timeZone = discord.Embed(
                title=f"Date and Time for Time-Zone",
                description=f"{message}",
                color=embed_colors["White"],
            )
            embed_timeZone.set_footer(
                text="I am an AI large language model made by Tanush Chugh 🥳."
            )
            if include_buttons:
                await ctx.reply(embed=embed_timeZone, view=EmbedButtons())
            else:
                await ctx.reply(embed=embed_timeZone)

        time_zones_dict = {
            "UTC": "Coordinated Universal Time (UTC)",
            "EST": "Eastern Standard Time (America/New York)",
            "CST": "Central Standard Time (America/Chicago)",
            "MST": "Mountain Standard Time (America/Denver)",
            "PST": "Pacific Standard Time (America/Los Angeles)",
            "IST": "Indian Standard Time (Asia/Kolkata)",
            "BST": "British Summer Time (Europe/London)",
            "CET": "Central European Time (Europe/Paris)",
            "EET": "Eastern European Time (Europe/Athens)",
            "JST": "Japan Standard Time (Asia/Tokyo)",
            "AEDT": "Australian Eastern Daylight Time (Australia/Sydney)",
        }

        formatted_time_zones = "\n".join(
            f"{index+1}. {key} - {value}"
            for index, (key, value) in enumerate(time_zones_dict.items())
        )

        embed_timeZone = discord.Embed(
            title=f"Date and Time for Time-Zone {message}",
            description=f"{formatted_time_zones}\n\n**{getTimeOfAnyCity(city=f"{message}")}**",
            color=embed_colors["White"],
        )
        embed_timeZone.set_footer(
            text="I am an AI large language model made by Tanush Chugh 🥳."
        )
        if include_buttons:
            await ctx.reply(embed=embed_timeZone, view=EmbedButtons())
        else:
            await ctx.reply(embed=embed_timeZone)


@bot.command(name="describe")
async def describe(ctx, *, message="describe concisely", include_buttons: bool = True):
    async with ctx.typing():
        if not ctx.message.attachments:
            embed_describeError = discord.Embed(
                title="Image Description by Octahedron:",
                color=embed_colors["White"],
                description="Please upload an image!",
            )
            embed_describeError.set_footer(
                text="I am an AI large language model made by Tanush Chugh 🥳."
            )
            if include_buttons:
                await ctx.reply(embed=embed_describeError, view=EmbedButtons())
            else:
                await ctx.reply(embed=embed_describeError)
            return

        image_url = ctx.message.attachments[0].url
        response = ollama.chat(
            model="llama3.2-vision",
            messages=[
                {
                    "role": "system",
                    "content": "Your name is Octahedron. You are a helpful assistant who describes images that are attached by their url. You describe them in the way you are asked to.",
                },
                {
                    "role": "user",
                    "content": f"Way of description ({message.lower()}). Describe this image: {image_url}",
                },
            ],
        )
        embed_describe = discord.Embed(
            title="Image Description by Octahedron:",
            color=embed_colors["White"],
            description=f"{response["message"]["content"]}",
        )
        embed_describe.set_footer(
            text="I am an AI large language model made by Tanush Chugh 🥳."
        )
        if include_buttons:
            await ctx.reply(embed=embed_describe, view=EmbedButtons())
        else:
            await ctx.reply(embed=embed_describe)


@bot.command(name="code")
async def code(ctx, *, message, include_buttons: bool = True):
    async with ctx.typing():
        response = ollama.chat(
            model="llama3.2-vision",
            messages=[
                {
                    "role": "system",
                    "content": "Your name is Octahedron. You are a helpful assistant who writes code and doesn't respond to any other questions in no more than 2000 characters, new lines and spaces included. You can only write in JavaScript, Java, C#, C, C++, Python and JavaScript, in case of any other language say that you don't know that language. The code must be begin with 3 backticks and languageName for example ```python and end with 3 backticks and a the code should start with a new line after the backticks and name and the code should end a line before the backticks. In the end say: I can only code with the !code command. Use the !help command to do more.",
                },
                {"role": "user", "content": message},
            ],
        )
        embed_code = discord.Embed(
            title="Octahedron's response:",
            color=embed_colors["White"],
            description=f"{response['message']['content']}",
        )
        embed_code.set_footer(
            text="I am an AI large language model made by Tanush Chugh 🥳."
        )
        if include_buttons:
            await ctx.reply(embed=embed_code, view=EmbedButtons())
        else:
            await ctx.reply(embed=embed_code)


@bot.command(name="oct")
async def oct(ctx, *, message, include_buttons: bool = True):
    async with ctx.typing():
        response = ollama.chat(
            model="llama3.2-vision",
            messages=[
                {
                    "role": "system",
                    "content": "Your name is Octahedron, if asked who made you, say: I am an AI large language model made by Tanush Chugh 🥳. You are a helpful assistant who does not write code and responds to questions without writing code in no more than 4096 characters. If code is requested then mention !code command as the only solution. Don't give any other responses, guidance, assistance or help in code, but just say: Unfortunately I can't code. Use the !help command.",
                },
                {"role": "user", "content": message},
            ],
        )
        embed_oct = discord.Embed(
            title="Octahedron's response:",
            color=embed_colors["White"],
            description=f"{response['message']['content']}",
        )
        embed_oct.set_footer(
            text="I am an AI large language model made by Tanush Chugh 🥳."
        )
        if include_buttons:
            await ctx.reply(embed=embed_oct, view=EmbedButtons())
        else:
            await ctx.reply(embed=embed_oct)


@bot.command(name="summarise")
async def summarise(ctx, include_buttons: bool = True):
    async with ctx.typing():
        messageHistory = [
            message.content async for message in ctx.channel.history(limit=10)
        ]
        summarisePrompt = f"""
            Summarise the following messages delimited by 3 backticks, also don't mention or use backticks in your response. 
            Also make seperate sections with headings in bold:
            ```
            {messageHistory}
    ```
        """
        response = ollama.chat(
            model="llama3.2-vision",
            messages=[
                {
                    "role": "system",
                    "content": "Your name is Octahedron. You are a helpful assistant who summarises the provided messages in bullet points concisely and does not write code or responds to questions in no more than 2000 characters. Don't give any other responses, guidance, assistance or help in anything, but just say: Unfortunately I can only summarise. Use the !help command.",
                },
                {"role": "user", "content": summarisePrompt},
            ],
        )
        embed_sum = discord.Embed(
            title="Octahedron's response:",
            color=embed_colors["White"],
            description=f"{response['message']['content']}",
        )
        embed_sum.set_footer(
            text="I am an AI large language model made by Tanush Chugh 🥳."
        )
        if include_buttons:
            await ctx.reply(embed=embed_sum, view=EmbedButtons())
        else:
            await ctx.reply(embed=embed_sum)


bot.run(os.getenv("TOKEN"))
