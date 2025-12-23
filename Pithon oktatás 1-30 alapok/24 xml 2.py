from xml.dom import minidom
import xml.etree.ElementTree as xml_tree

xml_doc = minidom.parse('test.xml')
print(xml_doc)

items = xml_doc.getElementsByTagName('items')
item = xml_doc.getElementsByTagName('item')

for i in item:
    print(i.attributes['name'].value)
    print(i.firstChild.data)

tree = xml_tree.parse("test.xml")
root = tree.getroot()
for irem in root:
    print(f"Root item: {item}")

print("_"*40)
print(root[0][0].text)


for car in root[1]:
    print(car.attrib)

data = xml_tree.Element("data")
items=xml_tree.SubElement(data, "item")
item1=xml_tree.SubElement(items, "item")
item2=xml_tree.SubElement(items, "item")
item1.set("name", "value1")
item2.set("name", "value2")
item1.text="Data1"
item2.text="Data2"

data_write = xml_tree.tostring(data, encoding="unicode")
with open("test2.xml", "w", encoding="utf-8") as file:
    file.write(data_write)

