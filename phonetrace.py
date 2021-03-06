#!usr/bin/env/python
import sys
import requests
import json
import time
import urllib

class color:

   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'


class config:
	key = "" #go to numverify login and put the api here

def main():
	if len(sys.argv) == 2:
		number = sys.argv[1]
		api = "http://apilayer.net/api/validate?access_key=" + config.key + "&number=" + number + "&country_code=&format=1"
		output = requests.get(api)
		content = output.text
		obj = json.loads(content)
		country_code = obj['country_code']
		country_name = obj['country_name']
		location = obj['location']
		carrier = obj['carrier']
		line_type = obj['line_type']

		print color.YELLOW + "[+] " + color.END + "Phone number information gathering"
		print "--------------------------------------"
		time.sleep(2)

		if country_code == "":
			print " - Getting Country		[ " + color.RED + "FAILED " + color.END + "]"
		else:
			print " - Getting Country		[ " + color.GREEN + "OK " + color.END + "]"

		time.sleep(2)
		if country_name == "":
			print " - Getting Country Name		[ " + color.RED + "FAILED " + color.END + "]"
		else:
			print " - Getting Country Name		[ " + color.GREEN + "OK " + color.END + "]"

		time.sleep(2)
		if location == "":
			print " - Getting Location		[ " + color.RED + "FAILED " + color.END + "]"
		else:
			print " - Getting Location		[ " + color.GREEN + "OK " + color.END + "]"
		time.sleep(2)
		if carrier == "":
			print " - Getting Carrier		[ " + color.RED + "FAILED " + color.END + "]"
		else:
			print " - Getting Carrier		[ " + color.GREEN + "OK " + color.END + "]"

		time.sleep(2)
		if line_type == None:
			print " - Getting Device		[ " + color.RED + "FAILED " + color.END + "]"
		else:
			print " - Getting Device		[ " + color.GREEN + "OK " + color.END + "]"
		print "--------------------------------------"	
		print ""
		print color.YELLOW + "[+] " + color.END + "Target Information"
		print "--------------------------------------"
		print " - Phone number: " + str(number)
		print " - Country: " + str(country_code)
		print " - Country Name: " + str(country_name)
		print " - Location: " + str(location)
		print " - Carrier: " + str(carrier)
		print " - Device: " + str(line_type)
		print "--------------------------------------"
	else:
		print "Usage Of This Tool:"
		print "	./%s <phone-number>" % (sys.argv[0])
		print "	./%s +100000000" % (sys.argv[0])

main()
