#
# read the data from the URL and print it
#
import re
import urllib.request
# open a connection to a URL using urllib
# webUrl  = urllib.request.urlopen('https://www.youtube.com/user/guru99com')

#get the result code and print it
# print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
#data = webUrl.read()
#print (data)

result = []

def get_markdown(year, day):
    code = open('conv_input.txt').read()
    temp = re.findall(r"(?:<article class=\"day-desc\">(?P<day>.*?)</article>|<p>(?P<answer>Your puzzle answer was <code>\d+</code>.)</p>)",
    code,
    flags=re.I | re.S | re.M)

    #days = re.findall(r"")
    for day in temp:
        print(day.group("answer"))

get_markdown(2023, 1)

# Returns a Regex that matches anything inside the delimiter.
# The given delimiter is escaped to allow the use of special characters.
#
# anything_inside("**") #=> /\*\*.*\*\*/
def anything_inside(start, ending=nil)
  start = "\\" + start.chars.join("\\")
  ending = start if ending == nil
  Regexp.new(start + ".*" + ending)
end

# This function translates MarkDown to HTML.
#
# markdown_to_html("plaintext") #=> "plaintext"
# markdown_to_html("**bold only**") #=> "<b>bold only</b>"
# markdown_to_html("_italics only_") #=> "<i>italics only</i>"
# markdown_to_html("`code only`") #=> "<code>code only</code>"
# markdown_to_html("    code by indentation") #=> "<code>code by indentation</code>"
# markdown_to_html("> To be or not to be\n\n") #=> "<q> To be or not to be</q>"
# markdown_to_html(35.chr + "Title\n") #=> "<h1>Title</h1>"
# markdown_to_html("\npara\n") #=> "\n<p>para</p>\n"
# markdown_to_html("[foo](http://foo.com)") #=> "<a href=\"http://foo.com\">foo</a>"
def html_to_markdown(text)
  text
    .gsub
    .gsub(anything_inside(">", "\n\n"))  {|txt| "<q>#{txt.sub(/^>*/,"").tr("\n\n", "")}</q>" }
    .gsub(anything_inside("**")) {|txt| "<b>#{txt.tr("**","")}</b>"}
    .gsub(anything_inside("_")) {|txt| "<i>#{txt.tr("_","")}</i>"}
    .gsub(anything_inside("`"))  {|txt| "<code>#{txt.tr("`","")}</code>"}
    .gsub(anything_inside("#", "\n")) {|txt| "<h1>#{txt.tr("\n","").sub(/^\#*/,"")}</h1>"}
    .gsub(anything_inside("\n")) {|txt| "\n<p>#{txt.tr("\n","")}</p>\n"}
    .gsub(/\ \ \ \ .*/) {|txt| "<code>#{txt.strip}</code>"}
    .gsub(/\[.*\]\(.*\)/) do |txt|
       to_show = txt.match(/(\[.*\])/)[1].tr("[","").tr("]","")
       url = txt.match(/(\(.*\))/)[1].tr("(","").tr(")","")
       "<a href=\"#{url}\">#{to_show}</a>"
    end
end
