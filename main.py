import os as brutality_ghosty

brutality_ghosty.system("pip install discord.py==1.7.3")
brutality_ghosty.system("pip install colorama")
brutality_ghosty.system(
    "sleep 2 && clear >/dev/null 2>&1 &"
    if brutality_ghosty.name == "posix"
    else "timeout /t 2 >nul 2>&1 && cls"
) 
import json as ghostop
import random as ghostyjija
from colorama import Fore, Style, init
import discord
from discord.ext import commands, tasks
import time
import re
import asyncio as made_by_ghosty


ghostyop = discord.Intents.all()
GhoStyyy = "."
ghosty = commands.Bot(
    command_prefix=GhoStyyy, case_insensitive=True, self_bot=True, intents=ghostyop
)
ghosty.remove_command("help")

running = True
pray_loop_running = True
last_gem_check = 0

print(
    f"""{Fore.BLUE}

           ▒▒                    ▒▒            ▒▒       ▒▒▒
        ▒▒▒▒▒▒▒   ▒▒▒     ▒▒▒▒ ▒▒▒▒▒▒▒▒        ▒▒▒▒     ▒▒▒▒  ░░░░░░░░
      ▒▒▒▒████▒▒ ▒▒█▒▒  ▒▒▒█▒▒▒▒░█████▒        ▒█▒▒   ▒▒▒██▒ ░░██████░
     ▒▒▒▒██░░██▒▒▒██▒▒ ▒▒░██▒░▒██░░░░█▒        ▒██▒▒ ▒▒██░▒▒ ░█░░░░░█░
     ▒▒██░░░░██▒▒██▒▒▒ ▒░██▒▒██░░░░░░█▒        ▒▒█▒▒▒▒██▒▒▒  ░█░░░░░█░
    ▒▒██░░█░░█▒▒▒█▒▒▒▒▒▒░█▒▒▒█░░░█░░██▒         ▒█▒▒▒██▒▒    ░░░█████░
    ▒▒█░░░░░░█▒▒█░░██░▒░█▒▒ ▒█░░░░░█▒▒▒         ▒░█▒██▒▒     ░░░░░░██░
    ▒▒█░░░░██▒▒▒████████▒▒  ▒██░░███▒▒          ▒▒██░▒       ░█░░░░░█░
     ▒██████▒▒▒███▒▒▒██▒▒   ▒▒████▒▒▒            ▒█▒▒        ░░██████░
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒              ▒▒▒          ░░░░░░░
     ▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒               ▒▒▒
               ▒▒   ▒▒        ▒▒                 ▒▒
                                                             BETA VERSION{Style.RESET_ALL}"""
)

init(autoreset=True)
print(f"{Fore.LIGHTRED_EX}\n\n > Made By GhoSty{Style.RESET_ALL}")

@ghosty.event
async def on_ready():
    print(
        f"{Fore.LIGHTRED_EX} > OwO Farm v3 Connected To:{Style.RESET_ALL}",
        f"{Fore.LIGHTGREEN_EX}{ghosty.user}{Style.BRIGHT}{Style.RESET_ALL}",
    )
    print(f"{Fore.LIGHTRED_EX} > Minor Updates And Fixes{Style.RESET_ALL}")




@ghosty.command(aliases=["h"])
async def help(ctx):
    ghosty_help = """
    # 🤑 GhoSty OwO Farm V3 🤑 
Prefix: `.`

**__Main__**
 🌟 Start: *Starts The AutoBot*
 🛑 Stop: *Stops The AutoBot*

**__Features__**
 ⚠ Ban Bypass
 🚨 Auto Detects OwO Warnings
 ⏱ Auto Cut After 1 Warning
 💎 Auto Use Gems 
 🏹 Fast And Secure

**__Made with 💖 and 🧠 by GhoSty__** 
"""
    await ctx.send(ghosty_help)  





async def parse_gems(inventory_message):
    rarity_order = ['f', 'l', 'm', 'e', 'r', 'u', 'c']
    gems_by_tier = {
        '1': [],
        '2': [],
        '3': [],
        '4': []
    }
    lines = inventory_message.split('\n')
    for line in lines:
        for tier in ['1', '2', '3', '4']:
            for rarity in rarity_order:
                pattern = fr'`(\d+)`<:({rarity}gem{tier}):\d+>'
                match = re.search(pattern, line)
                if match:
                    gem_number = match.group(1)  
                    gems_by_tier[tier].append((rarity, gem_number))
    for tier in gems_by_tier:
        gems_by_tier[tier].sort(key=lambda x: rarity_order.index(x[0]))
    selected_gems = []
    for tier in ['1', '2', '3', '4']:
        if gems_by_tier[tier]:
            selected_gems.append(gems_by_tier[tier][0][1])
    
    return selected_gems

async def do_gem_check(ctx):
    await ctx.send("owo inventory")
    await made_by_ghosty.sleep(3)  
    
    try:
        latest_messages = await ctx.channel.history(limit=2).flatten()
        
        for message in latest_messages:
            if message.author.id == 408785106942164992:  
                if "inventory" in message.content.lower():
                    gem_numbers = await parse_gems(message.content)
                    if gem_numbers: 
                        use_command = "owo use " + " ".join(gem_numbers)
                        await ctx.send(use_command)
                        await made_by_ghosty.sleep(3)
                    else:
                        print("No gems found")
                    break
    except Exception as e:
        print(f"Error in gem check: {e}")
        import traceback
        print(traceback.format_exc())


async def check_warning(ctx):
    global running
    try:
        messages = await ctx.channel.history(limit=10).flatten()
        
        for msg in messages:
            msg_content = str(msg.content).lower()
      
            checkph = [
                "captcha",
                "Please complete thi​s wit​hin 1​0 m​inutes o​r i​t m​ay r​esult i​n a​ ba​n!",
                "P​lease comple​te you​r c​aptcha t​o ver​ify th​at y​ou ar​e huma​n!",
                "a​re y​ou a​ rea​l hu​man?"
            ]
            if any(phrase.lower() in msg_content for phrase in checkph):

            
                global running
                running = False
                
                await ctx.send("⚠ Warning Detected! 🛑 Stopping The Process | Type .start again to re-start grinding")
                print("⚠ Warning Detected! 🛑 Stopping The Process | Type .start again to re-start grinding")
                return True
        return False
    except Exception as e:
        print(f"Warning check error: {e}")
        return False

async def equip_best(ctx):
    await ctx.send("owo team remove all")
    await made_by_ghosty.sleep(2)
    await ctx.send("owo zoo")
    await made_by_ghosty.sleep(3)

    try:
        messages = await ctx.channel.history(limit=5).flatten()
        for msg in messages:
            if msg.author.id == 408785106942164992 and "zoo" in msg.content.lower():
                lines = msg.content.split('\n')
                animals = []
                rarity_score = {'c': 1, 'u': 2, 'r': 3, 'e': 4, 'm': 5, 'l': 6, 'f': 7, 'd': 8}
                zoo_letters = ['C', 'U', 'R', 'E', 'M', 'L', 'F', 'D']
                for i, line in enumerate(lines):
                    if any(letter in line for letter in zoo_letters):
                        emojis = re.findall(r'<a?:.+?:\d+>', line)
                        for emoji in emojis:
                            match = re.search(r'<a?:(.+?):', emoji)
                            if match:
                                name = match.group(1).lower()
                                rarity = zoo_letters[i]
                                score = rarity_score.get(rarity.lower(), 0)
                                animals.append((score, name))
                top_animals = sorted(animals, reverse=True)[:3]
                if top_animals:
                    team_cmd = "owo team add " + " ".join([a[1] for a in top_animals])
                    await ctx.send(team_cmd)
                    print(f"[Auto Equip] {team_cmd}")
    except Exception as e:
        print(f"[Auto Equip Error] {e}")



@ghosty.command()
async def start(ctx):
    global running, last_gem_check
    running = True
    last_gem_check = time.time()
    await equip_best(ctx)
    last_command = None
    farm_count = 0

    while running:
        try:
            now = time.time()
            if now - last_gem_check > 480:
                if await check_warning(ctx): break
                await do_gem_check(ctx)
                last_gem_check = now

            smart_choices = [
                "owo hunt", "owo battle", "owo pray",
                ghostyjija.choices(["owo s 1", "owo piku", "owo army"], weights=[0.4, 0.3, 0.3])[0],
                ghostyjija.choices(["owo b", "owo h", "owo zoo"], weights=[0.3, 0.4, 0.3])[0]
            ]

            if farm_count % 12 == 0:
                smart_choices.append("owo sell all")
            if ghostyjija.random() < 0.03:
                smart_choices.append("owo roll")

            command = ghostyjija.choice(smart_choices)
            while command == last_command:
                command = ghostyjija.choice(smart_choices)
            last_command = command

            await ctx.trigger_typing()
            await made_by_ghosty.sleep(ghostyjija.uniform(0.4, 1.2))
            await ctx.send(command)

            if await check_warning(ctx): break

            farm_count += 1
            delay = ghostyjija.betavariate(2.0, 5.0) * 18 + 5
            await made_by_ghosty.sleep(delay)

            if ghostyjija.random() < 0.04:
                await made_by_ghosty.sleep(ghostyjija.uniform(300, 600))

        except Exception as e:
            print(f"[Error] {e}")



@ghosty.command()  
async def stop(ctx):
    global running  
    await ctx.send(
        "🛑 Stopping | Type .start again to re-start grinding"
    )  
    running = False





with open("config.json", "r") as config_file:  
    config = ghostop.load(config_file)  

ghostyopaf = config["TOKEN"]  
ghosty.run(ghostyopaf, bot=False)
