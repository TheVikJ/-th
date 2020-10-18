# Σth
Σth (sigmath): your favourite homework helper discord bot

## Inspiration 🧠
For the past few months, I've loved to create discord bots in Python using the discord.py package so I knew I wanted to do something with that. I married that with the fact that I always study with friends using Discord where we often solve the demanding questions of IB Maths Analysis and Approaches, Higher Level. One thing I noticed was that there wasn't this thing I could just screenshot my problem into which solves it, at least not on Discord which many use to study. Thus, Σth was born.

## What it does 📷✖➕➖➗
Σth is an all-around maths homework helper discord bot. You can do two main things which are either to put your expression in a command, or take a screenshot of your problem and attach it to an '!img' command. The '!img' command works on Tesseract OCR to extract your text so you will get the correct answer! Here are the commands:

**Main Commands:**

!roots [expression]: find zeroes/roots/solutions to expressions

!factor [expression]: factor an expression 

!domain [expression]: domain of an expression

!range [expression]: range of an expression

!solve [expression] for [desired variable]: solve for the value of a variable in an expression

!simplify [expression]: simplify an expression

**Screenshot Commands (a screenshot of your problem must be attached):**

!imgroots: find zeroes/roots/solutions to expressions

!imgfactor: factor an expression 

!imgdomain: domain of an expression

!imgrange: range of an expression

!imgsolve: solve for the value of a variable in an expression

!imgsimplify: simplify an expression

## How I built it 🔧🔨🧰
I used the Discord API's Python package called discord.py for the Discord bot part of things. As for extracting the information and text from the image, I'm using the Tesseract OCR which I downloaded the .exe for which, when combined with the pytesseract package, it can extract text from an image (kind of sort of) reliably. 

Lastly, to compute the maths, I used a combination of the Newton API and the WolframAlpha API.

## Challenges I ran into 🏃‍♂️🏃‍♂️
**1. Extracting Text From Image 📷**

This was by far the hardest part of my whole project. I started off by asking the (extremely helpful) mentors how I could do this and I got really good suggestions! For example, Sohil gave me some GeeksForGeeks links and Shivam gave me the Google Cloud Recognition API for OCR. While these were amazing solutions, I wasn't advanced enough to understand the GeeksForGeeks link and didn't have access to a credit card which meant I couldn't use the Cloud Vision API. This led me to do further research, finally coming to an alright solution on the verge of giving up: Tesseract OCR and the pytesseract package. This wasn't the best solution as I later learnt, because the OCR would often give me bad results and the font size (which is needed for the exponents and logarithms) was not taken into consideration. However, it worked for the time being (even though it's not perfect right now).

**2. Finding An API For Computing Maths ➕➖➗**

For some reason, there are like 48,291 APIs online for Maths Facts, Maths Trivia, etc. but only very few for actually solving questions. Luckily, I waded through the API waters and found the lost city of Newton API, residing near the trench of the WolframAlpha API.

**3. Coding Skills 💻**

This weekend, I wanted to challenge myself so I wanted to try to make a really ambitious project on my own. I realized very easily that my coding skills weren't as good as I needed them to be to actually make the full project but because I stuck on, I actually managed to make a decent working prototype of my idea (even if the OCR doesn't work too well).

## Accomplishments that I'm proud of and what I learned 🏆🧠🏅

**1. Working Prototype**

Right now, the OCR works like 80% of the time and the calculation comes back right almost 100% of the time. I'm extremely proud I managed to accomplish that with my project over just two days and that I challenged my self, and not only completed it but excelled. At the end of the day, I'm just overjoyed at how my final project came out!

**2. Implementing OCR**

This was not only my first time working with OCR, but also my first time working with any ML-related library which proved to be a bit challenging in understanding how it all works, but I managed to implement it successfully, and in the end the OCR worked!

## What's next for Σth (sigmath) ⏭⏭
I would really like to learn more about ML and OCR so I can implement one specifically for equations and maths to make my bot more accurate, which would be number one on my to-do list. I would also like to expand my bot to calculus as well to help more people with more advanced problem. 
