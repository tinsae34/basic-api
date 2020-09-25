import telebot
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import time
telegramtoken = "1348341121:AAEJuxhu8ANhM0dnFEhcaNlGFIogXb8HAJ4"
website = 'https://www.worldometers.info/coronavirus/country/ethiopia/'
bot = telebot.TeleBot(token=telegramtoken)

req = requests.get(website)

scrap = BeautifulSoup(req.content, 'html.parser')
 
find1 = scrap.find(class_='maincounter-number').get_text()
ss = scrap.find(id='newsdate2020-09-17')
allfind = ss.find('li').get_text()
print(allfind)
find2 = scrap.find(id='maincounter-wrap')
find3 = find2.find_all('span')
print(find3)
print(find1)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,'Welcome to real time corona virus tracker bot to get corona virus update type /new or to get total corona virus case type /all ')

@bot.message_handler(commands=['all'])
def new(message):
    bot.reply_to(message,f'Total Coronavirus Cause ={find1}')


@bot.message_handler(commands=['new'])
def all(message):
    bot.reply_to(message,f"{allfind} in Ethiopia")


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(5)



