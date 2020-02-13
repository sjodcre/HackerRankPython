# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
# def multiple_replace(dict, text): #this have error when they're sticked e.g. && ||
#   # Create a regular expression  from the dictionary keys
#   regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

#   # For each match, look-up corresponding value in dictionary
#   return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text) 
# dict = {
#     " || " : " or ",
#     " && " : " and "
#   } 
lines= int(input())
for _ in range(lines):
    text = input()
    text = re.sub(r"(?<= )&&(?= )", "and", text)
    text = re.sub(r"(?<= )\|\|(?= )", "or", text)
    print(text)
    # print (multiple_replace(dict, input()))
    # print (re.sub("(<!--.*?-->)", "", input())) #remove comment
