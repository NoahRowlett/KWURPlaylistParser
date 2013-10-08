import sys, os, re
from decimal import *
 
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename. No command line argument found that specifies a file to use." % sys.argv[0])
 
filename = sys.argv[1]
 
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])

class Song:
	# constructor:
	def __init__(self, name, artist, label):
		self.name = name.rstrip()
		self.artist = artist.rstrip()
		self.label = label.rstrip()

	def get_name(self):
		return self.name 

	def get_artist(self):
		return self.artist

	def get_label(self):
		return self.label

	def set_name(self, name):
		self.name = name.rstrip()

	def set_artist(self, artist):
		self.artist = artist.rstrip()

	def set_label(self):
		self.label = label.rstrip()

	def format_output(self):
		return  ""


def parseString(string):
	match = re.findall(r"<td class=\"resultlist\">(.*?)</td>", string)
	if match is not None:
		return match
	else:
		print "oh boy..."

playlist = []

def infoOrg(info[]){
	
}



f = open(filename)
for line in f:
	lineAsString = line.rstrip()
	if parseString(lineAsString) is not None:
		print parseString(lineAsString)
	else:
		print "oh no!"

 
f.close()
