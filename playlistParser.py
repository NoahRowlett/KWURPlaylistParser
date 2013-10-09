import sys, os, re
from decimal import *
 
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename. No command line argument found that specifies a file to use." % sys.argv[0])
 
filename = sys.argv[1]
 
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])

class Song:
	# constructor:
	def __init__(self, name, artist, album, label):
		self.name = name.rstrip()
		self.artist = artist.rstrip()
		self.album = album.rstrip()
		self.label = label.rstrip()

	def get_name(self):
		return self.name 

	def get_artist(self):
		return self.artist

	def get_album(self):
		return self.album

	def get_label(self):
		return self.label

	def set_name(self, name):
		self.name = name.rstrip()

	def set_artist(self, artist):
		self.artist = artist.rstrip()

	def set_artist(self, album):
		self.album = album.rstrip()

	def set_label(self):
		self.label = label.rstrip()

	def format_output(self):
		return  self.get_artist() + " - " + self.get_name() + " - " + self.get_album()

	def format_output_html_table(self):
		return  "\n\t\t<td>" + self.get_name() + "</td>\n\t\t<td>" + self.get_artist() + "</td>\n\t\t<td>" + self.get_album() + "</td>\n\t\t<td>" + self.get_label() + "</td>"


def parseString(string):
	match = re.findall(r"<td class=\"resultlist\">(.*?)</td>", string)
	if match is not None:
		return match


playlist = []

def infoOrg(info):
	if isinstance(info,list):
		if len(info) == 9:
			song = Song(info[5], info[4], info[6], info[7])
			playlist.append(song)


f = open(filename)
for line in f:
	lineAsString = line.rstrip()
	if parseString(lineAsString) is not None:
		infoOrg(parseString(lineAsString))

for song in playlist:
	print str(playlist.index(song) + 1) + ". " + song.format_output()

# print "<table>"
# for song in playlist:
# 	print "\t<tr>" + song.format_output_html_table() + "\n\t</tr>\n"
# print "</table>"

 
f.close()
