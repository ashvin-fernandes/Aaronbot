import discord
import asyncio
from random import randint

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
	if message.content.startswith('!test'):
		counter = 0
		tmp = await client.send_message(message.channel, 'Calculating messages...')
		async for log in client.logs_from(message.channel, limit=100):
			if log.author == message.author:
				counter += 1

		await client.edit_message(tmp, 'You have {} messages.'.format(counter))
	elif message.content.startswith('!sleep'):
		await asyncio.sleep(5)
		await client.send_message(message.channel, 'Done sleeping')
	elif message.content.startswith('!bot'):
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
		elif (input.find("bye") != -1 or input.find("b-") != -1):
			response = "b-";
		else :
			n = randint(1,11)
			if n == 1:
				response = "Did you know Pnig's my best friend on snapchat.. ?";
			elif n == 2:
				response = "How do you mean.. ?";
			elif n == 3:
				response = "What happened.. ?";
			elif n == 4:
				response = "Such as.. ?";
			elif n == 5:
				response = "They're not even good!";
			elif n == 6:
				response = "You've got a lot of loyalty ";
			elif n == 7:
				response = "I'm HAVING fun" ;
			elif n == 8:
				response = "Whatever d00d";
			elif n == 9:
				response = "Pretty cheap";
			elif n == 10:
				response = "l0l";
			elif n == 11:
				response = "demmit";
		
		await client.send_message(message.channel, response)
	elif message.content.startswith('!coin'):
		n = randint(0,1)
		if n == 0:
			response = "Heads"
		else:
			response = "Tails"
		await client.send_message(message.channel, response)

	elif message.content.startswith('!bot'):
		pass
	elif message.content.startswith('!bot'):
		pass
	elif message.content.startswith('!help'):
		pass


		

client.run('ztemzqgs@pwrby.com', 'bigguy4U')