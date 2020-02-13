import sys
import xml.etree.ElementTree as etree

total = []
def get_attr_number(node):
    # your code goes here    
    total.append(len(node.attrib))
    for child in node:
        # total+= len(child.attrib)
        get_attr_number(child)
    return(sum(total))

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))