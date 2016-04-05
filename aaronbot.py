import discord
import asyncio
import random

client = discord.Client()

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
	n = 1
	if message.content.startswith('!sleep'):
		await asyncio.sleep(5)
		await client.send_message(message.channel, 'Done sleeping')
	elif message.content.startswith('!bot'):
		response = bot(message)
	elif message.content.startswith('!coin'):
		response = coin(message)
	elif message.content.startswith('!kappaspam'):
		response = kappaspam()
	elif "Angelo" in message.content:
		await client.send_message(message.channel, (message.content.replace("Angelo", "------")))
		await client.send_message(message.channel, "MESSAGE EDITED: Stop talking about your master " + message.author.name)
		await client.delete_message(message)
	elif message.content.startswith('!help'):
		pass
		
	await client.send_message(message.channel, response)

		
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
		phrases = open('phrases.txt').read().splitlines()
		response = random.choice(phrases) 
		
	return response
	
def coin(message):
	n = random.randint(0,1)
	if n == 0:
		response = "Heads"
	else:
		response = "Tails"
		
	return response
	
def kappaspam():
	response = "kappa kappa kappa kappa kappa\n kappa kappa kappa kappa kappa\n kappa kappa kappa kappa kappa"
	return response
	
	
		
async def on_member_join(member):
	if member.name == "Reikkou":
		await client.send_message(message.channel, "@everyone PNIG ALERT")
		await client.send_message(message.channel, "HI PNIG!")


		

client.run('ztemzqgs@pwrby.com', 'bigguy4U')