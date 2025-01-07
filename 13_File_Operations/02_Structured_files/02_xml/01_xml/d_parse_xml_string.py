"""
Purpose: To parse(read) xml string
"""

import xml.etree.ElementTree as ET

input_string = """
<stuff>
    <users>
        <user x="1">
            <id>001</id>
            <name>tom</name>
        </user>
        <user x="12">
            <id>009</id>
            <name>brady</name>
        </user>
    </users>
</stuff>"""

stuff_tree = ET.fromstring(input_string)

nodes = stuff_tree.findall("users") 
print(nodes)

# cant find in child level
nodes = stuff_tree.findall("user")
print(nodes)

# to check in subchild level
nodes = stuff_tree.findall("users/user")  
print(nodes)
print("User count:", len(nodes))


for item in nodes:
    print("\nName", item.find("name").text)
    print("Id", item.find("id").text)
    print("Attribute", item.get("x")) 