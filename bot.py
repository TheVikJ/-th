import discord
import pytesseract
import requests
import shutil
import json
import wolframalpha

image_url = ""
client = discord.Client()
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
WOLFRAM = 'XXXXXXXXXXXXXXXXX'
wolframclient = wolframalpha.Client(WOLFRAM)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!factor'):
        problem = message.content.replace('!factor ', 'factor ')
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!domain'):
        problem = message.content.replace('!domain ', 'domain of ')
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!range'):
        problem = message.content.replace('!range ', 'range of ')
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!solve'):
        problem = message.content.replace('!solve ', 'solve ')
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!simplify'):
        problem = message.content.replace('!simplify ', 'simplify ')
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!imgdomain'):
        problem = 'domain of f(x) = '

        image_url = message.attachments[0].url
        local_file = open('local_image.jpg', 'wb')
        imgget = requests.get(image_url, stream=True)
        imgget.raw.decode_content = True
        shutil.copyfileobj(imgget.raw, local_file)
        del imgget

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        problem += pytesseract.image_to_string(r'C:\Users\91959\PycharmProjects\sigmath\local_image.jpg')
        problem = problem.replace(problem[len(problem) - 1], '')

        for i in range(len(problem)):
            if problem[i] in "*%":
                problem = problem.replace(problem[i], '^')
            elif problem[i] in "?":
                problem = problem.replace(problem[i], '^2')

        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!imgrange'):
        problem = 'range of f(x) = '

        image_url = message.attachments[0].url
        local_file = open('local_image.jpg', 'wb')
        imgget = requests.get(image_url, stream=True)
        imgget.raw.decode_content = True
        shutil.copyfileobj(imgget.raw, local_file)
        del imgget

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        problem += pytesseract.image_to_string(r'C:\Users\91959\PycharmProjects\sigmath\local_image.jpg')
        problem = problem.replace(problem[len(problem) - 1], '')

        for i in range(len(problem)):
            if problem[i] in "*%":
                problem = problem.replace(problem[i], '^')
            elif problem[i] in "?":
                problem = problem.replace(problem[i], '^2')

        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)
        
    if message.content.startswith('!roots'):
        problem = message.content.replace('!roots ', 'solve ')
        problem += ' = 0 for x'
        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

    if message.content.startswith('!imgsolve'):
        problem = 'solve '

        image_url = message.attachments[0].url
        local_file = open('local_image.jpg', 'wb')
        imgget = requests.get(image_url, stream=True)
        imgget.raw.decode_content = True
        shutil.copyfileobj(imgget.raw, local_file)
        del imgget

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        problem += pytesseract.image_to_string(r'C:\Users\91959\PycharmProjects\sigmath\local_image.jpg')
        problem = problem.replace(problem[len(problem) - 1], '')

        for i in range(len(problem)):
            if problem[i] in "*%":
                problem = problem.replace(problem[i], '^')
            elif problem[i] in "?":
                problem = problem.replace(problem[i], '^2')

        res = wolframclient.query(problem)
        ans = next(res.results).text
        await message.channel.send(ans)

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
        print(problem)

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
