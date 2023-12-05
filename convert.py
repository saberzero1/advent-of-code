#
# read the data from the URL and print it
#
import re
import urllib.request
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://www.youtube.com/user/guru99com')

#get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
print (data)

def get_markdown(year, day):
    link = 'https://adventofcode.com/' + str(year) + '/day/' + str(day)
    webUrl = urllib.request.urlopen(link)
    code = str(webUrl.getcode())
    temp = re.search(r"<article class=\"ay-desc\">(.*?)</article>",
    code,
    flags=re.I | re.S | re.M)
    day1 = temp[0]
    day2 = temp[1]