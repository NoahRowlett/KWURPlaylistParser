import sys, os, re
import HTMLParser
 
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename. No command line argument found that specifies a file to use." % sys.argv[0])
 
filename = sys.argv[1]
playlist = []
 
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])

class Song:
	# constructor:
	def __init__(self, name, artist, album, label, timestamp):
		self.name = name.rstrip()
		self.artist = artist.rstrip()
		self.album = album.rstrip()
		self.label = label.rstrip()
		self.timestamp = timestamp.rstrip()

	def get_name(self):
		return self.name 

	def get_artist(self):
		return self.artist

	def get_album(self):
		return self.album

	def get_label(self):
		return self.label

	def get_timestamp(self):
		return self.timestamp

	def set_name(self, name):
		self.name = name.rstrip()

	def set_artist(self, artist):
		self.artist = artist.rstrip()

	def set_artist(self, album):
		self.album = album.rstrip()

	def set_label(self):
		self.label = label.rstrip()

	def set_timestamp(self):
		self.timestamp = timestamp.rstrip()

	def format_output(self):
		return  self.get_artist() + " - " + self.get_name() + " - " + self.get_album()

	def format_output_for_db(self):
		return  self.get_name() + "\t" + self.get_artist() + "\t" + self.get_album() + "\t" + self.get_label() + "\t" + self.get_timestamp()

	def format_output_html_table(self):
		return  "\n\t\t<td>" + self.get_name() + "</td>\n\t\t<td>" + self.get_artist() + "</td>\n\t\t<td>" + self.get_album() + "</td>\n\t\t<td>" + self.get_label() + "</td>"


def parseString(string):
	match = re.findall(r"<td class=\"resultlist\">(.*?)</td>", string)
	if match is not None:
		return match

def infoOrg(info):
	if isinstance(info,list):
		if len(info) == 9:
			song = Song(info[5], info[4], info[6], info[7], info[3])
			playlist.append(song)

def printForDB(plist):
	if isinstance(plist,list):
		for song in playlist:
			print song.format_output_for_db()

def printNumberedList(plist):
	if isinstance(plist,list):
		for song in playlist:
			print str(playlist.index(song) + 1) + ". " + song.format_output()

def printHTMLTable(plist):
	if isinstance(plist,list):
		print "<table>"
		for song in plist:
			print "\t<tr>" + song.format_output_html_table() + "\n\t</tr>\n"
		print "</table>"



#Main
f = open(filename)
for line in f:
	lineAsString = line.rstrip()
	lineAsString = HTMLParser.HTMLParser().unescape( lineAsString ) 
	if parseString(lineAsString) is not None:
		infoOrg(parseString(lineAsString))
printNumberedList(playlist)
#printForDB(playlist)
f.close()
