from pprint import pprint
import requests

raw = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?id=4497286&appid=ecfee0db7ad165b1609aabeaaee0e6f3')
w = raw.json()

brief = w['list'][0]['weather'][0]['description']
morn = w['list'][0]['temp']['morn']
high = w['list'][0]['temp']['max']
day = w['list'][0]['temp']['day']
low = w['list'][0]['temp']['min']
eve = w['list'][0]['temp']['eve']

briefs = str(brief)
mornf = str(round( (int(morn)-273.15)*1.8 + 32))
highf = str(round( (int(high)-273.15)*1.8 + 32))
dayf = str(round( (int(day)-273.15)*1.8 + 32))
lowf = str(round( (int(low)-273.15)*1.8 + 32))
evef = str(round( (int(eve)-273.15)*1.8 + 32))

postText = str("Good morning brothers!    As you are waking up this morning, the temperature outside will be "+mornf+" degrees. The overall weather forecast for today is "+briefs+" with a high of "+highf+" degrees and a low of "+lowf+". The average daily temperature will be around "+dayf+" degrees and be "+evef+" this evening. Have a great day!")

r = requests.post('https://api.groupme.com/v3/bots/post', data = {'bot_id':'5cf33e661c09ee4c24bfb6942e','text':postText})
