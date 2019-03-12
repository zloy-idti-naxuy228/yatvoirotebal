import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

import random

bottoken = "snip"
commandprefix = "#"

bot = commands.Bot(command_prefix=commandprefix)

@bot.event
async def on_ready():
    print ("Starting up")
    print ("My username is " + bot.user.name + " and i am running with the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="в хате Lazeropa", type=0))
    print ("Started")

@bot.command()
async def kanadskiy():
	await bot.say('Канадский не мудак!')
	await bot.say('Потому что он мудак')

@bot.command()
async def lazerop():
	await bot.say('Лазероп Гамасех? или же он Хештэх?')

@bot.command()
async def kanadec():
	await bot.say(' 189.098.56.71.0 - Айпи Мудака')

@bot.command()
async def zloy():
	await bot.say('Кто же такой Злой? Он не мудак но мудак ты! Это Бог создал бота а чего Ты добился? Мудак!')
	
@bot.command()
async def fuzic():
	await bot.say('Эт Мудак Который Выебывается')


bot.run('NTU1MTI2MTYxMzIwMTgxNzYx.D2mrmw.jTNrKsbFS9pnhvNL3jW8jsdixw0')
