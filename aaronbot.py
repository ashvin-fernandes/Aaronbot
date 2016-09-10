import discord
import asyncio
import random

import urllib.request
import urllib.parse
import re

import logging

#Put login info into login.txt


client = discord.Client()


def invalid():
	response = ".. ?"
	return response
		
def bot(message):
	input = message.content.partition(' ')[2]
	if (input == ""):
		response = "What happened.. ?"
	elif (input.find("know") != -1):
		response = "How do you mean.. ?";
	elif (input.find("?") != -1) :
		response = "You don't kNOW.. ?";
	elif (input.find("have") != -1):
		response = "HAVE";
	elif (input.find("now") != -1):
		response = "NOW";
	elif (input.find("bye") != -1 or input.find("b-") != -1 or input.find("buh") != -1):
		response = "b-";
	else :
		phrases = open('phrases.txt').read().splitlines() #Add dynamic wrestling videos
		response = random.choice(phrases) 
		

	return response

def coin():
	n = random.randint(0,1)
	if n == 0:
		response = "Heads"
	else:
		response = "Tails"
		
	return response
	
def kappaspam():
	response = "kappa kappa kappa kappa kappa\n kappa kappa kappa kappa kappa\n kappa kappa kappa kappa kappa"
	return response

def video(message):
	input = message.content.partition(' ')[2]
	query_string = urllib.parse.urlencode({"search_query" : input})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	response = "http://www.youtube.com/watch?v=" + search_results[0]
	return response
	
def lolbans():
	html_content = urllib.request.urlopen("http://bestbans.com/tier/silver")
	banlist = re.findall(r': \w+</b>', html_content.read().decode())
	response = ""
	for ban in banlist:
		response = response + ban.replace("</b>", " ")
	
	return response
	
def magic(message):
	input = message.content.partition(' ')[2]
	query_string = urllib.parse.urlencode({"q" : input})
	html_content = urllib.request.urlopen("http://magiccards.info/query?" + query_string)
	card = re.findall(r'http:\/\/magiccards\.info\/scans\/en\/(.*)\.jpg', html_content.read().decode())
	if len(card) > 0:
		response = "http://magiccards.info/scans/en/" + card[0] + ".jpg"
	else:
		response = "Nothing found"
		
	return response
	
	
def help(): #Test
	file = open('help.txt')
	response = ""
	for line in file:
		response = response + line
		
	return response

def test():
	print("test")
	
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')	

@client.event
async def on_message(message):
	input = ""
	response = ""
	censor = ""
	
	if message.content.startswith('!help'):
		response = help()
	elif message.content.startswith('!bot'):
		response = bot(message)
	elif message.content.startswith('!coin'):
		response = coin()
	elif message.content.startswith('!kappaspam'):
		response = kappaspam()
	elif message.content.startswith('!video'):
		response = video(message)
	elif message.content.startswith('!lolbans'):
		response = lolbans()
	elif message.content.startswith('!magic'):
		response = magic(message)
	elif message.content.startswith("!"):
		response = invalid()

	if response != "" :	
		rather = random.randint(1, 10)
		if (rather == 10):
			response += " rather"
		await client.send_message(message.channel, response)
		
login = open('login.txt').read().split(" ")
client.run(login[0], login[1])

		

