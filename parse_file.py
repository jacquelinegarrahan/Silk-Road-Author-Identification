from html.parser import HTMLParser
from bs4 import BeautifulSoup
import re


def parse_forum_html(file_name):
	"""Extracts all users from a silk road forum page, and their posts"""
	file = open(file_name, "r")
	soup = BeautifulSoup(file, "html.parser")

	post_headers = soup.find_all('dt') #titles contain: title, post by, and time
	for div in soup.find_all("a"):
		div.decompose()
	post_bodys = soup.find_all('dd')
	authors = []
#	dates = []
	content = []
	for post in post_headers:
		text = post.get_text()
		info = text[text.find('Post by:'):]
		date_idx = info.find('on')
		poster = info[len('Post by: '):date_idx-1]
		poster = poster.strip()
#		date = info[date_idx+len('on '):] ### convert data to usable format
#		dates.append(date)
		authors.append(poster)
	for post in post_bodys:
		for div in post.find_all("blockquote", {'class':'bbc_standard_quote'}): 
			div.decompose()
		text = post.get_text()
		text = text.strip()
		text = text.lower()
		text = re.sub("[^' a-zA-Z]", ' ', text)
		text = text.replace('.', ' ')
		text = text.replace('a ', ' ')
		text = text.replace(' as ', ' ')
		text = text.replace(' about ', ' ')
		text = text.replace(' above ', ' ')
		text = text.replace(' am ', ' ')
		text = text.replace(' again ', ' ')
		text = text.replace(' after ', ' ')
		text = text.replace(' all ', ' ')
		text = text.replace(' an ', ' ')
		text = text.replace(' at ', ' ')
		text = text.replace(' any ', ' ')
		text = text.replace(' are ', ' ')
		text = text.replace(' be ', ' ')
		text = text.replace(' before ', ' ')
		text = text.replace(' been ', ' ')
		text = text.replace(' because ', ' ')
		text = text.replace(' being ', ' ')
		text = text.replace(' below ', ' ')
		text = text.replace(' between ', ' ')
		text = text.replace(' both ', ' ')
		text = text.replace(' but ', ' ')
		text = text.replace(' by ', ' ')
		text = text.replace(' could ', ' ')
		text = text.replace(' did ', ' ')
		text = text.replace(' do ', ' ')
		text = text.replace(' does ', ' ')
		text = text.replace( "don't", ' ')
		text = text.replace(' doing ', ' ')
		text = text.replace(' down ', ' ')
		text = text.replace(' during ', ' ')
		text = text.replace(' each ', ' ')
		text = text.replace(' few ', ' ')
		text = text.replace(' for ', ' ')
		text = text.replace(' from ', ' ')
		text = text.replace(' had ', ' ')
		text = text.replace(' has ', ' ')
		text = text.replace(' have ', ' ')
		text = text.replace(' having ', ' ')
		text = text.replace(' he ', ' ')
		text = text.replace(" he'd ", ' ')
		text = text.replace(" he'll ", ' ')
		text = text.replace(" he's ", ' ')
		text = text.replace(' her ', ' ')
		text = text.replace(' here ', ' ')
		text = text.replace(" here's ", ' ')
		text = text.replace(' hers ', ' ')
		text = text.replace(' after ', ' ')
		text = text.replace(' herself ', ' ')
		text = text.replace(' him ', ' ')
		text = text.replace(' himself ', ' ')
		text = text.replace(' his ', ' ')
		text = text.replace(' how ', ' ')
		text = text.replace(" how's ", ' ')
		text = text.replace("i ", ' ')
		text = text.replace("i'd ", ' ')
		text = text.replace("i'm ", ' ')
		text = text.replace("i'll ", ' ')
		text = text.replace("i've ", ' ')
		text = text.replace(' if ', ' ')
		text = text.replace(' in ', ' ')
		text = text.replace(' into ', ' ')
		text = text.replace(' is ', ' ')
		text = text.replace(' it ', ' ')
		text = text.replace("it's ", ' ')
		text = text.replace('its ', ' ')
		text = text.replace(' itself ', ' ')
		text = text.replace(" let's ", ' ')
		text = text.replace(' me ', ' ')
		text = text.replace(' more ', ' ')
		text = text.replace(' most ', ' ')
		text = text.replace(' myself ', ' ')
		text = text.replace(' my ', ' ')
		text = text.replace(' nor ', ' ')
		text = text.replace(' of ', ' ')
		text = text.replace(' on ', ' ')
		text = text.replace(' once ', ' ')
		text = text.replace(' only ', ' ')
		text = text.replace(' or ', ' ')
		text = text.replace(' other ', ' ')
		text = text.replace(' our ', ' ')
		text = text.replace(' ours ', ' ')
		text = text.replace(' ourselves ', ' ')
		text = text.replace(' out ', ' ')
		text = text.replace(' over ', ' ')
		text = text.replace(' own ', ' ')
		text = text.replace(' same ', ' ')
		text = text.replace(' she ', ' ')
		text = text.replace(" she'd ", ' ')
		text = text.replace(" she'll ", ' ')
		text = text.replace(" she's ", ' ')
		text = text.replace(' should ', ' ')
		text = text.replace(' so ', ' ')
		text = text.replace(' some ', ' ')
		text = text.replace(' such ', ' ')
		text = text.replace(' than', ' ')
		text = text.replace(' that ', ' ')
		text = text.replace(" that's ", ' ')
		text = text.replace('the ', ' ')
		text = text.replace(' their ', ' ')
		text = text.replace(' theirs ', ' ')
		text = text.replace(' them ', ' ')
		text = text.replace(' themseves ', ' ')
		text = text.replace(' then ', ' ')
		text = text.replace(' there ', ' ')
		text = text.replace(" there's ", ' ')
		text = text.replace(' these ', ' ')
		text = text.replace(" they ", ' ')
		text = text.replace(" they'd ", ' ')
		text = text.replace(" they'll ", ' ')
		text = text.replace(" they're ", ' ')
		text = text.replace(" they've ", ' ')
		text = text.replace('this ', ' ')
		text = text.replace(' those ', ' ')
		text = text.replace(' through ', ' ')
		text = text.replace(' to ', ' ')
		text = text.replace(' too ', ' ')
		text = text.replace(' under ', ' ')
		text = text.replace(' until ', ' ')
		text = text.replace(' up ', ' ')
		text = text.replace(' very ', ' ')
		text = text.replace(' was ', ' ')
		text = text.replace('we ', ' ')
		text = text.replace(" we'd ", ' ')
		text = text.replace(" we'll ", ' ')
		text = text.replace(" we're ", ' ')
		text = text.replace(" we've ", ' ')
		text = text.replace(' were ', ' ')
		text = text.replace(' what ', ' ')
		text = text.replace(' what ', ' ')
		text = text.replace(" what's ", ' ')
		text = text.replace(' when ', ' ')
		text = text.replace(" when's ", ' ')
		text = text.replace(' where ', ' ')
		text = text.replace(" where's ", ' ')
		text = text.replace(' which ', ' ')
		text = text.replace(' while ', ' ')
		text = text.replace(' who ', ' ')
		text = text.replace(" who's ", ' ')
		text = text.replace(' whom ', ' ')
		text = text.replace(' why ', ' ')
		text = text.replace(" why's ", ' ')
		text = text.replace(' with ', ' ')
		text = text.replace(' would ', ' ')
		text = text.replace(' you ', ' ')
		text = text.replace(" you'd ", ' ')
		text = text.replace(" you'll ", ' ')
		text = text.replace(" you're ", ' ')
		text = text.replace(" you've ", ' ')
		text = text.replace(' your ', ' ')
		text = text.replace(' yours ', ' ')
		text = text.replace(' yourself ', ' ')
		text = text.replace(' yourselves ', ' ')
		text = text.replace(' can ', ' ')
		text = text.replace(' not ', ' ')
		text = text.replace(' and ', ' ')
		text = text.replace('if ', ' ')
		text = text.replace("''", ' ')


		content.append(text)

	return authors, content