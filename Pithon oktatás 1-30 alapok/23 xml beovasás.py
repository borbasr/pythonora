from xml.dom import minidom


xml_doc = minidom.parse('test.xml')
print(xml_doc)

items = xml_doc.getElementsByTagName('items')
item = xml_doc.getElementsByTagName('item')

for i in item:
    print(i.attributes['name'].value)
    print(i.firstChild.data)









