#!python2.7
from datetime import datetime
from emoji import UNICODE_EMOJI

import requests

import dialogs


class Emoji(object):
	
	def __init__(self):
		
		self.start = datetime.utcnow()
		self.name = dialogs.input_alert("Gimme Emoji")
		self.user = 1
		self.end = None
		self.logged = False
		
		if not self.is_emoji:
			print("Given text is not an Emoji.")
			dialogs.alert("Not an Emoji!")
	
	
	@property
	def is_emoji(self):
		count = 0
		for emoji in UNICODE_EMOJI:
			count += self.name.count(emoji)
			if count > 1:
				return False
		return bool(count)
	
	
	def log(self):
		"Log emoji check-in on Life Timeline"
		
		if self.logged or not self.is_emoji:
			return self.logged
		
		response = requests.post(
			url = "https://life-timelines.herokuapp.com/emoji-check-in",
			data = {
				"name": self.name,
				"start": self.start,
				"end": self.end,
				"user": self.user,
			})
		
		if response.status_code == 200:
			print(response.text)
			self.logged = True
		
		print(response.status_code)
		
		return self.logged

if __name__ == "__main__":
	
	a = Emoji()
	
	print(a.name)
	
	a.log()
