import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # print(elem)
    if level+1 > maxdepth:
        maxdepth = level+1
    for child in elem:        
        depth(child,level+1)
    # children = elem.getchildren()
    # if children:
    #     maxdepth +=1
    #     depth(children,0)
    # your code goes here

if __name__ == '__main__':