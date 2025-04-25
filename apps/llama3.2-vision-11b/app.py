# Copyright (c) 2025 Tanush Chugh
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import difflib as df
import os
import secrets
import string
import time
from datetime import datetime as dt

import discord
import ollama
import requests as r
import torch
from discord.ext import commands
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    ALLOWED_USER = 924697503356583967

    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True

    bot = commands.Bot(command_prefix="*", intents=intents)
    bot.remove_command("help")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("Nvidia GPU exists:", torch.cuda.is_available())
    print("Numbers:", torch.cuda.device_count())

    if device == "cpu":
        print(f"Switching to {device} mode as no Nvidia GPU is available.")
        print(
            "If you have a Nvidia GPU, please change the version of the 'torch' module."
        )

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

    time_zones_dict = {
        "UTC": "Coordinated Universal Time (UTC)",
        "EST": "Eastern Standard Time (America/New York)",
        "CST": "Central Standard Time (America/Chicago)",
        "MST": "Mountain Standard Time (America/Denver)",
        "PST": "Pacific Standard Time (America/Los Angeles)",
        "PDT": "Pacific Daylight Time for daylight saving (America/Los Angeles)",
        "IST": "Indian Standard Time (Asia/Kolkata)",
        "BST": "British Summer Time (Europe/London)",
        "CET": "Central European Time (Europe/Paris)",
        "EET": "Eastern European Time (Europe/Athens)",
        "JST": "Japan Standard Time (Asia/Tokyo)",
        "AEDT": "Australian Eastern Daylight Time (Australia/Sydney)",
    }

    activation_keys = {}

    activated_users = {}

    class EmbedButtons(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.add_item(
                discord.ui.Button(
                    label="Become a premium member 👑",
                    style=discord.ButtonStyle.green,
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

    class EmbedButtonsVIP(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.add_item(
                discord.ui.Button(
                    label="Support Team 🧑‍💼",
                    style=discord.ButtonStyle.green,
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

    def generate_key() -> str:
        chars = string.ascii_uppercase + string.digits
        key_parts = []
        for _ in range(4):
            part = "".join(secrets.choice(chars) for _ in range(5))
            key_parts.append(part)
        key = "-".join(key_parts)
        return key

    def create_unique_key() -> str:
        while True:
            new_key = generate_key()
            if new_key not in activation_keys:
                activation_keys[new_key] = False
                return new_key

    def create_multiple_unique_keys(num: int = 10) -> list:
        new_keys = []
        for _ in range(num):
            key = create_unique_key()
            new_keys.append(key)
        return new_keys

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
        create_multiple_unique_keys(num=10)
        print(f"Bot is ready as {bot.user.name}")
        if device == "cuda":
            print("GPU device is ready!")
        else:
            print("GPU device not found!")
        print(
            "-----------------------------------------------------------------------------------------------------------"
        )
        print(f"The following commands are loaded: {bot.commands}")

    @bot.event
    async def on_command_error(ctx, error, include_buttons: bool = True):
        ctx.typing()
        async with ctx.typing():
            if isinstance(error, commands.CommandNotFound):
                command_tags = {
                    "*help": [
                        "list",
                        "commands",
                        "help",
                        "info",
                        "list-of-commands",
                        "octcommands",
                    ],
                    "*hello": [
                        "greet",
                        "greetings",
                        "hello",
                        "hi",
                        "welcome",
                        "hola",
                        "namaste",
                        "bonjour",
                    ],
                    "*hi": [
                        "hiii",
                        "hii",
                        "greetings-my-friend",
                        "hellow",
                        "howdy",
                        "yo",
                        "sup",
                        "salutations",
                    ],
                    "*oct": [
                        "send",
                        "prompt",
                        "octahedron",
                        "message",
                        "command",
                        "tell",
                        "speak",
                    ],
                    "*summarise": [
                        "summarize",
                        "summary",
                        "messages",
                        "last-10",
                        "history",
                        "chat-history",
                    ],
                    "*describe": [
                        "image-recognition",
                        "describe",
                        "AI",
                        "cutting-edge",
                        "image",
                        "detection",
                        "object-recognition",
                    ],
                    "*local": [
                        "local",
                        "date",
                        "time",
                        "timezone",
                        "current",
                        "clock",
                        "timezoneinfo",
                    ],
                    "*code": [
                        "code",
                        "programming",
                        "languages",
                        "Java",
                        "C#",
                        "C",
                        "C++",
                        "Python",
                        "JavaScript",
                        "write",
                        "script",
                        "compile",
                    ],
                    "*zones": [
                        "time-zones",
                        "zones",
                        "utc",
                        "time",
                        "local-time",
                        "timezone-list",
                        "zoneinfo",
                    ],
                    "*rag": [
                        "access",
                        "internet",
                        "data",
                        "latest",
                        "paid-feature",
                        "internet-data",
                        "live-data",
                        "real-time-data",
                    ],
                    "*imagegen": [
                        "image-generation",
                        "generate",
                        "images",
                        "artificial",
                        "AI",
                        "unique",
                        "paid-feature",
                        "art-generation",
                    ],
                }
                available_tags = {}
                for command, tags in command_tags.items():
                    for tag in tags:
                        available_tags[tag] = command
                closest_matches = df.get_close_matches(
                    ctx.invoked_with,
                    list(available_tags.keys()),
                    n=3,
                    cutoff=0.6,
                )
                suggestions = []
                if closest_matches:
                    for match in closest_matches:
                        suggestions.append(
                            f"{match} (Did you mean? {available_tags[match]})"
                        )
                user_id = str(ctx.author.id)
                is_premium_user = user_id in activated_users
                if closest_matches:
                    embed = discord.Embed(
                        title="Activation Status",
                        description=f"Oops! The command `{ctx.invoked_with}` is not recognized. Did you mean one of these?\n"
                        + "".join(
                            [
                                f"```{index + 1}) {match}```"
                                for index, match in enumerate(suggestions)
                            ]
                        ),
                        color=embed_colors["White"],
                    )
                    embed.set_footer(
                        text="I am an AI large language model made by Tanush Chugh 🥳."
                    )
                    if include_buttons:
                        if is_premium_user:
                            await ctx.reply(embed=embed, view=EmbedButtonsVIP())
                        else:
                            await ctx.reply(embed=embed, view=EmbedButtons())
                    else:
                        await ctx.reply(embed=embed)
                else:
                    embed = discord.Embed(
                        title="Activation Status",
                        description=f"Oops! The command `{ctx.invoked_with}` is not recognized. Please check the command and try again.",
                        color=embed_colors["White"],
                    )
                    embed.set_footer(
                        text="I am an AI large language model made by Tanush Chugh 🥳."
                    )
                    if include_buttons:
                        if is_premium_user:
                            await ctx.reply(embed=embed, view=EmbedButtonsVIP())
                        else:
                            await ctx.reply(embed=embed, view=EmbedButtons())
                    else:
                        await ctx.reply(embed=embed)
            else:
                raise error

    @bot.command(name="activate")
    async def activate(ctx, key: str, include_buttons: bool = True):
        ctx.typing()
        async with ctx.typing():
            user_id = str(ctx.author.id)

            if user_id in activated_users:
                message = "You've already activated your premium access! 👑"
                include_buttons = False
            elif key not in activation_keys:
                message = "Invalid activation key! ❌ Please check your key."
                include_buttons = True
            elif activation_keys[key]:
                message = "This key has already been used! 🔒"
                include_buttons = True
            else:
                activation_keys[key] = True
                activated_users[user_id] = True
                message = "Premium features activated successfully! 🎉 Enjoy your new powers 👑"
                include_buttons = False

            embed = discord.Embed(
                title="Activation Status",
                description=message,
                color=(
                    embed_colors["Green"]
                    if "successfully" in message
                    else embed_colors["Red"]
                ),
            )
            embed.set_footer(
                text="I am an AI large language model made by Tanush Chugh 🥳."
            )

            if include_buttons:
                await ctx.reply(embed=embed, view=EmbedButtons())
            else:
                await ctx.reply(embed=embed, view=EmbedButtonsVIP())

    @bot.command(name="showkeys")
    async def show_keys(ctx):
        ctx.typing()
        async with ctx.typing():
            if ctx.author.id == ALLOWED_USER:
                keys_str = "\n".join(
                    [f"{key}: {status}" for key, status in activation_keys.items()]
                )
                try:
                    dm_channel = await ctx.author.create_dm()
                    await ctx.reply("DM sent!")
                    await dm_channel.send(
                        f"Here are your activation keys:\n\n{keys_str}"
                    )
                except discord.errors.Forbidden:
                    await ctx.reply(
                        "I can't send you a DM. Please check your DM settings."
                    )
            else:
                await ctx.reply("You are not authorized to see the activation keys.")

    @bot.command(name="help")
    async def hello(ctx, include_buttons: bool = True):
        user_id = str(ctx.author.id)
        ctx.typing()
        async with ctx.typing():
            list_ofCommands = [
                "*help (List all commands)",
                "*hello (Greet the bot)",
                "*hi (Greet the bot)",
                "*oct (Send a prompt)",
                "*summarise (Summarise last 10 messages)",
                'Under Development (Will be paid 💸): \\*describe (Use Octahedron\'s cutting edge image recognition tech to identify images. You can put a prompt after the \\*describe command to explain the AI the way of description. For example: \\*describe in a poetic way. If no promp is given then the default is "describe consicely")',
                "*local (Allows you to see local date and time)",
                "*code (Write code in Java, C#, C, C++, Python and JavaScript. It must be within 1983 characters, limit increasing soon with more languages on the way!)",
                "\\*zones (Give a list of common time zones with time of mentioned zone. For example: \\*zones IST for India time | by default it is UTC)",
                "\\*rag (Give Octahedron access to internet's latest data. With \\*oct it uses training data that goes upto December 2023) 💸 Feature is paid",
                "*imagegen (Generate unique images with Octahedron) 💸 Feature is paid",
                "*showkeys (DM existing valid premium keys to owner, ie Tanush Chugh)",
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
            if include_buttons and user_id not in activated_users:
                await ctx.reply(embed=embed_cmd, view=EmbedButtons())
            elif include_buttons and user_id in activated_users:
                await ctx.reply(embed=embed_cmd, view=EmbedButtonsVIP())
            else:
                await ctx.reply(embed=embed_cmd)

    @bot.command(name="rag")
    async def rag(ctx, *, message="news today", include_buttons: bool = True):
        user_id = str(ctx.author.id)
        ctx.typing()
        async with ctx.typing():
            if user_id not in activated_users:
                embed_rag = discord.Embed(
                    title="Octahedron's response:",
                    description=f'The message "{message}" can\'t be searched as this feature is for premium users. Please pay ₹299/month or ₹2999/year 💸 or use *activate <key> to activate.',
                    color=embed_colors["Red"],
                )
            else:
                embed_rag = discord.Embed(
                    title="Octahedron's response:",
                    description=f"(Pretend for now as this feature is in the works: {message})",
                    color=embed_colors["Blurple (Discord)"],
                )

            embed_rag.set_footer(
                text="I am an AI large language model made by Tanush Chugh 🥳."
            )
            if include_buttons and user_id not in activated_users:
                await ctx.reply(embed=embed_rag, view=EmbedButtons())
            elif include_buttons and user_id in activated_users:
                await ctx.reply(embed=embed_rag, view=EmbedButtonsVIP())
            else:
                await ctx.reply(embed=embed_rag)

    @bot.command(name="imagegen")
    async def imagegen(ctx, *, message="cat", include_buttons: bool = True):
        user_id = str(ctx.author.id)
        ctx.typing()
        async with ctx.typing():
            if user_id not in activated_users:
                embed_img = discord.Embed(
                    title="Octahedron's response:",
                    description=f'The image of "{message}" can\'t be generated as this feature is for premium users. Please pay ₹299/month or ₹2999/year 💸 or use *activate <key> to activate.',
                    color=embed_colors["Red"],
                )
            else:
                embed_img = discord.Embed(
                    title="Octahedron's response:",
                    description=f"(Pretend for now as this feature is in the works: {message})",
                    color=embed_colors["Blurple (Discord)"],
                )

            embed_img.set_footer(
                text="I am an AI large language model made by Tanush Chugh 🥳."
            )
            if include_buttons and user_id not in activated_users:
                await ctx.reply(embed=embed_img, view=EmbedButtons())
            elif include_buttons and user_id in activated_users:
                await ctx.reply(embed=embed_img, view=EmbedButtonsVIP())
            else:
                await ctx.reply(embed=embed_img)

    @bot.command(name="hello")
    async def hello(ctx, include_buttons: bool = True):
        user_id = str(ctx.author.id)
        ctx.typing()
        async with ctx.typing():
            embed_hello = discord.Embed(
                title="Octahedron's response:",
                description="Nice to meet you! My name is Octahedron, and I'll do my best to assist you with your questions. What's on your mind?",
                color=embed_colors["White"],
            )
            embed_hello.set_footer(
                text="I am an AI large language model made by Tanush Chugh 🥳."
            )
            if include_buttons and user_id not in activated_users:
                await ctx.reply(embed=embed_hello, view=EmbedButtons())
            elif include_buttons and user_id in activated_users:
                await ctx.reply(embed=embed_hello, view=EmbedButtonsVIP())
            else:
                await ctx.reply(embed=embed_hello)

    @bot.command(name="hi")
    async def hello(ctx, include_buttons: bool = True):
        user_id = str(ctx.author.id)
        ctx.typing()
        async with ctx.typing():
            embed_hi = discord.Embed(
                title="Octahedron's response:",
                description="Hello! What's on your mind? Need some assistance with something?",
                color=embed_colors["White"],
            )
            embed_hi.set_footer(
                text="I am an AI large language model made by Tanush Chugh 🥳."
            )
            if include_buttons and user_id not in activated_users:
                await ctx.reply(embed=embed_hi, view=EmbedButtons())
            elif include_buttons and user_id in activated_users:
                await ctx.reply(embed=embed_hi, view=EmbedButtonsVIP())
            else:
                await ctx.reply(embed=embed_hi)

    @bot.command(name="local")
    async def local(ctx, include_buttons: bool = True):
        user_id = str(ctx.author.id)
        ctx.typing()
        async with ctx.typing():
            current_date_time = time.strftime(
                "%I:%M %p | %A, %d %B %Y", time.localtime()
            )
            embed_time = discord.Embed(
                title="Local date and time",
                description=f"{current_date_time}",
                color=embed_colors["White"],
            )
            embed_time.set_footer(
                text="I am an AI large language model made by Tanush Chugh 🥳."
            )
            if include_buttons and user_id not in activated_users:
                await ctx.reply(embed=embed_time, view=EmbedButtons())
            elif include_buttons and user_id in activated_users:
                await ctx.reply(embed=embed_time, view=EmbedButtonsVIP())
            else:
                await ctx.reply(embed=embed_time)

    @bot.command(name="zones")
    async def time_zones(ctx, *, message="UTC", include_buttons: bool = True):
        user_id = str(ctx.author.id)
        ctx.typing()
        async with ctx.typing():
            if message not in time_zones_dict:
                embed_timeZone = discord.Embed(
                    title=f"Date and Time for Time-Zone",
                    description=f"The API couldn't find the time-zone {message}, so I'll use the default time-zone of UTC",
                    color=embed_colors["White"],
                )
                embed_timeZone.set_footer(
                    text="I am an AI large language model made by Tanush Chugh 🥳."
                )
                await ctx.reply(embed=embed_timeZone)
                ctx.typing()
                message = "UTC"
            time_str = getTimeOfAnyCity(message)
            if time_str is None:
                time_str = "Unable to retrieve time. Please check the timezone name."
            formatted_time_zones = "\n".join(
                f"{index+1}. {key} - {value}"
                for index, (key, value) in enumerate(time_zones_dict.items())
            )
            embed_timeZone = discord.Embed(
                title=f"Date and Time for Time-Zone {message}",
                description=f"{formatted_time_zones}\n\n**{time_str}**",
                color=embed_colors["White"],
            )
            embed_timeZone.set_footer(
                text="I am an AI large language model made by Tanush Chugh 🥳."
            )
            if include_buttons and user_id not in activated_users:
                await ctx.reply(embed=embed_timeZone, view=EmbedButtons())
            elif include_buttons and user_id in activated_users:
                await ctx.reply(embed=embed_timeZone, view=EmbedButtonsVIP())
            else:
                await ctx.reply(embed=embed_timeZone)

    @bot.command(name="describe")
    async def describe(
        ctx, *, message="describe clearly and factually", include_buttons: bool = True
    ):
        user_id = str(ctx.author.id)
        ctx.typing()
        if device == "cpu":
            embed_error = discord.Embed(
                title="Image Description by Octahedron:",
                color=discord.Color.red(),
                description="GPU is not available for image recognition. This feature requires GPU for optimal performance.",
            )
            embed_error.set_footer(text="Please contact the bot admin.")
            await ctx.reply(embed=embed_error)
            return
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
                        "content": "You are Octahedron, an advanced visual AI. You specialize in providing accurate, concise, and context-aware descriptions of images. Focus only on what is visually present without making assumptions. Avoid guessing if the content is unclear. Be objective and literal, additionally make sure your response is no more than 4096 characters (including spaces and new lines).",
                    },
                    {
                        "role": "user",
                        "content": f"Way of description ({message.lower()}): Describe this image clearly and concisely, identifying objects, people, and surroundings if possible. Do not guess or hallucinate. Here is the image: {image_url}",
                    },
                ],
            )
            embed_describe = discord.Embed(
                title="Image Description by Octahedron (⚠️ This feature is still under development. Descriptions may be inaccurate):",
                color=embed_colors["White"],
                description=f"{response["message"]["content"]}",
            )
            embed_describe.set_footer(
                text="I am an AI large language model made by Tanush Chugh 🥳."
            )
            if include_buttons and user_id not in activated_users:
                await ctx.reply(embed=embed_describe, view=EmbedButtons())
            elif include_buttons and user_id in activated_users:
                await ctx.reply(embed=embed_describe, view=EmbedButtonsVIP())
            else:
                await ctx.reply(embed=embed_describe)

    @bot.command(name="code")
    async def code(
        ctx,
        *,
        message="a program in python",
        include_buttons: bool = True,
    ):
        user_id = str(ctx.author.id)
        ctx.typing()
        async with ctx.typing():
            response = ollama.chat(
                model="llama3.2-vision",
                messages=[
                    {
                        "role": "system",
                        "content": "Your name is Octahedron. You are a helpful assistant who writes code and doesn't respond to any other questions in no more than 4083 characters, new lines and spaces included. You can only write in JavaScript, Java, C#, C, C++, Python and JavaScript, in case of any other language say that you don't know that language. The code must be begin with 3 backticks and languageName for example ```python and end with 3 backticks and a the code should start with a new line after the backticks and name and the code should end a line before the backticks. In the end always say: I can only code with the code command. Use the help command to do more.",
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
            if include_buttons and user_id not in activated_users:
                await ctx.reply(embed=embed_code, view=EmbedButtons())
            elif include_buttons and user_id in activated_users:
                await ctx.reply(embed=embed_code, view=EmbedButtonsVIP())
            else:
                await ctx.reply(embed=embed_code)

    @bot.command(name="oct")
    async def oct(ctx, *, message="Who are you?", include_buttons: bool = True):
        user_id = str(ctx.author.id)
        ctx.typing()
        async with ctx.typing():
            response = ollama.chat(
                model="llama3.2-vision",
                messages=[
                    {
                        "role": "system",
                        "content": f"Your name is Octahedron, you have premium features that are visible to everyone but accessible only to premium users, don't mention the features unless the user asks you for image generation or web access. Those features can be activated by subscribing to a premium key by clicking the discord button below the message that are not visible to you but made by me in the code file and don't mention that the buttons are invisible to you or made by me in the code file. The button says, also don't use quotation marks while mentioning it, instead use ** before and after it to make it bold: Become a premium member 👑. Also always add the following as a note in the end saying (Please note that I only provide links to my main website, and no other external links are available for premium activation.) in a response if asked for instructions on getting premium features. Also always add after the instructions to click buttons text in a new line: [octahedrontech.com](https://octahedrontech.com). If asked who made you, say: I am an AI large language model made by Tanush Chugh 🥳. If asked for local time or time of any time zone then say use ```local``` command or ```zones``` command. You do not write code and respond to questions without writing code. If code is requested then mention *code command as the only solution. Don't give any other responses, guidance, assistance or help in code, but just say. Also only use single * for help command: Unfortunately I can't code. Use the *code command, I can code in Java, C#, C, C++, Python and JavaScript as of: {time.strftime("%I:%M %p | %A, %d %B %Y", time.localtime())}.",
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
            if include_buttons and user_id not in activated_users:
                await ctx.reply(embed=embed_oct, view=EmbedButtons())
            elif include_buttons and user_id in activated_users:
                await ctx.reply(embed=embed_oct, view=EmbedButtonsVIP())
            else:
                await ctx.reply(embed=embed_oct)

    @bot.command(name="summarise")
    async def summarise(ctx, include_buttons: bool = True):
        user_id = str(ctx.author.id)
        ctx.typing()
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
            if include_buttons and user_id not in activated_users:
                await ctx.reply(embed=embed_sum, view=EmbedButtons())
            elif include_buttons and user_id in activated_users:
                await ctx.reply(embed=embed_sum, view=EmbedButtonsVIP())
            else:
                await ctx.reply(embed=embed_sum)

    bot.run(os.getenv("TOKEN"))
