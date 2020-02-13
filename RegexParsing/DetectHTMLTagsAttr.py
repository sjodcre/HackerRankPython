# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for attr in attrs:
            print("->",attr[0], ">",attr[1])

    def handle_startendtag(self, tag, attrs):
        print (tag)
        for attr in attrs:
            print("->",attr[0], ">",attr[1])

x =int(input())
parser = MyHTMLParser()
for _ in range(x):
    # print(input())
    parser.feed(input())
