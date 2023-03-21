import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('2042517973:AAEr8Nxx8205xOstR-l95OQMtY7H5fwfUf8')

def get_tiktok_url(message):
	url = message.text
	if 'tiktok.com/' not in url:
		bot.reply_to(message, 'Maaf, url yang anda kirim bukan url TikTok')
		return None
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	video = soup.find('video')
	if video is None:
		bot.reply_to(message, 'Maaaf, saya tidak dapat menemukan video TikTok yang anda inginkan :(')
		return None
	return video['src']

def download_video(url):
	response = requests.get(url, stream=True)
	filename = url.split('/')[-2]+'.mp4'
	with open(filename, 'wb') as f:
		for chunk in response.iter_content(chunk_sizze=1024):
			if chunk:
				f.write(chunk)
	return filename

def send_video(chat_id, filename):
	video = open(filename, 'rb')
	bot.send_video(chat_id, video)

def handle_message(message):
	titok_url = get_tiktok_url(message)
	if tiktok_url is not None:
		filename = download_tiktok_video(tiktok_url)
		send_tiktok_video(message.chat.id, filename)

bot.polling()