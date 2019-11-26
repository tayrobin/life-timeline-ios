#!python2.7
import sys
from emoji import UNICODE_EMOJI
from datetime import datetime, timedelta

import requests

import dialogs


class Emoji(object):
	
	def __init__(self, text):
		
		self.start = datetime.utcnow()
		self.name = text
		self.user = 1
		self.end = self.start + timedelta(minutes=15)
		self.logged = False
		
		if not self.is_emoji:
			print("'%s' is not an Emoji." % self.name)
			#dialogs.alert("'%s' is not an Emoji." % self.name)
	
	
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
			url = "https://life-timelines.herokuapp.com/log-emoji",
			data = {
				"name": self.name,
				"start": self.start,
				"end": self.end,
				"user": self.user,
			})
		
		if response.status_code == 201:
			print(response.text)
			self.logged = True
		
		print(response.status_code)
		
		return self.logged

if __name__ == "__main__":
	
	text = dialogs.input_alert("Gimme Emoji (separate by spaces)").split(" ")
	
	for word in text:
		a = Emoji(word)
	
		print(a.name)
	
		print(a.log())
		
	sys.exit()
