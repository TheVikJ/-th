import discord
import pytesseract
import requests
import shutil
import json

image_url = ""
client = discord.Client()
TOKEN = 'NzY2NzY0ODc2OTgyNjQ4ODgy.X4oHcA.IStMDtup6MXXnPXcfNDBwPbO-OM'

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!factor'):
        problem = message.content.replace('!factor ', '')
        if '+' in problem:
            for i in range(len(problem)):
                if problem[i] == '+':
                    problem = problem.replace('+', '%2B')
        if '^' in problem:
            for i in range(len(problem)):
                if problem[i] == '^':
                    problem = problem.replace('^', '%5E')
        if '.' in problem:
            for i in range(len(problem)):
                if problem[i] == '.':
                    problem = problem.replace('.', '%2E')
        solution = requests.get('https://newton.now.sh/api/v2/factor/' + problem).text
        msg = json.loads(solution)
        await message.channel.send(msg.get('result'))

    if message.content.startswith('!simplify'):
        problem = message.content.replace('!simplify ', '')
        if '+' in problem:
            for i in range(len(problem)):
                if problem[i] == '+':
                    problem = problem.replace('+', '%2B')
        if '^' in problem:
            for i in range(len(problem)):
                if problem[i] == '^':
                    problem = problem.replace('^', '%5E')
        if '.' in problem:
            for i in range(len(problem)):
                if problem[i] == '.':
                    problem = problem.replace('.', '%2E')
        solution = requests.get('https://newton.now.sh/api/v2/simplify/' + problem).text
        msg = json.loads(solution)
        await message.channel.send(msg.get('result'))

    if message.content.startswith('!roots'):
        problem = message.content.replace('!roots ', '')
        if '+' in problem:
            for i in range(len(problem)):
                if problem[i] == '+':
                    problem = problem.replace('+', '%2B')
        if '^' in problem:
            for i in range(len(problem)):
                if problem[i] == '^':
                    problem = problem.replace('^', '%5E')
        if '.' in problem:
            for i in range(len(problem)):
                if problem[i] == '.':
                    problem = problem.replace('.', '%2E')
        solution = requests.get('https://newton.now.sh/api/v2/zeroes/' + problem).text
        msg = json.loads(solution)
        await message.channel.send(msg.get('result'))

    if message.content.startswith('!imgfactor'):
        image_url = message.attachments[0].url
        local_file = open('local_image.jpg', 'wb')
        imgget = requests.get(image_url, stream=True)
        imgget.raw.decode_content = True
        shutil.copyfileobj(imgget.raw, local_file)
        del imgget

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        problem = pytesseract.image_to_string(r'C:\Users\91959\PycharmProjects\sigmath\local_image.jpg')
        problem = problem.replace(problem[len(problem)-1], '')
        for i in range(len(problem)):
            if problem[i] in "*%":
                problem = problem.replace(problem[i], '^')
            elif problem[i] in "?":
                problem = problem.replace(problem[i], '^2')
        if '+' in problem:
            for i in range(len(problem)):
                if problem[i] == '+':
                    problem = problem.replace('+', '%2B')
        if '^' in problem:
            for i in range(len(problem)):
                if problem[i] == '^':
                    problem = problem.replace('^', '%5E')
        if '.' in problem:
            for i in range(len(problem)):
                if problem[i] == '.':
                    problem = problem.replace('.', '%2E')

        solution = requests.get('https://newton.now.sh/api/v2/factor/' + problem).text
        msg = json.loads(solution)
        await message.channel.send(msg.get('result'))

    if message.content.startswith('!imgroots'):
        image_url = message.attachments[0].url
        local_file = open('local_image.jpg', 'wb')
        imgget = requests.get(image_url, stream=True)
        imgget.raw.decode_content = True
        shutil.copyfileobj(imgget.raw, local_file)
        del imgget

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        problem = pytesseract.image_to_string(r'C:\Users\91959\PycharmProjects\sigmath\local_image.jpg')
        problem = problem.replace(problem[len(problem)-1], '')
        for i in range(len(problem)):
            if problem[i] in "*%":
                problem = problem.replace(problem[i], '^')
            elif problem[i] in "?":
                problem = problem.replace(problem[i], '^2')
        if '+' in problem:
            for i in range(len(problem)):
                if problem[i] == '+':
                    problem = problem.replace('+', '%2B')
        if '^' in problem:
            for i in range(len(problem)):
                if problem[i] == '^':
                    problem = problem.replace('^', '%5E')
        if '.' in problem:
            for i in range(len(problem)):
                if problem[i] == '.':
                    problem = problem.replace('.', '%2E')

        solution = requests.get('https://newton.now.sh/api/v2/zeroes/' + problem).text
        msg = json.loads(solution)
        await message.channel.send(msg.get('result'))

    if message.content.startswith('!imgsimplify'):
        image_url = message.attachments[0].url
        local_file = open('local_image.jpg', 'wb')
        imgget = requests.get(image_url, stream=True)
        imgget.raw.decode_content = True
        shutil.copyfileobj(imgget.raw, local_file)
        del imgget

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        problem = pytesseract.image_to_string(r'C:\Users\91959\PycharmProjects\sigmath\local_image.jpg')
        problem = problem.replace(problem[len(problem)-1], '')
        for i in range(len(problem)):
            if problem[i] in "*%":
                problem = problem.replace(problem[i], '^')
            elif problem[i] in "?":
                problem = problem.replace(problem[i], '^2')
        if '+' in problem:
            for i in range(len(problem)):
                if problem[i] == '+':
                    problem = problem.replace('+', '%2B')
        if '^' in problem:
            for i in range(len(problem)):
                if problem[i] == '^':
                    problem = problem.replace('^', '%5E')
        if '.' in problem:
            for i in range(len(problem)):
                if problem[i] == '.':
                    problem = problem.replace('.', '%2E')

        solution = requests.get('https://newton.now.sh/api/v2/simplify/' + problem).text
        msg = json.loads(solution)
        await message.channel.send(msg.get('result'))

@client.event
async def on_ready():
       print('Logged in as')
       print(client.user.name)
       print(client.user.id)
       print('------')

client.run(TOKEN)