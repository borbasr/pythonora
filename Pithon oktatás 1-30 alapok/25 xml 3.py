import xml.etree.ElementTree as xml_tree

tree = xml_tree.parse('test.xml')
root = tree.getroot()

root[0][1].text = 'Modositva'
root[0][1].set('name', 'mod')
root[0][1].set('uj', 'valami')

tree.write('new_test.xml', encoding='utf-8')

attrib = {}
cars = root.makeelement('cars', attrib)
root.append(cars)

attrib = {'color': 'black', 'brand': 'Audi'}
car = root[1].makeelement('car', attrib)
root[1].append(car)
tree.write('new.xml')
