from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if(data !='\n'):
            print (">>> Data")
            print(data)
    def handle_comment(self, data):
        number_of_line = len(data.split('\n'))
        if number_of_line>1:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print (">>> Single-line Comment")
            print(data)
  
  
  
  
  
  
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

