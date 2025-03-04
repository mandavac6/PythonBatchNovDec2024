"""
Purpose: Creating html using lxml
    - lxml has simple syntax and faster in performance
"""

from lxml import etree

# Adding meta data to tags
html_elem = etree.Element("html", lang="en_GB")
print(etree.tostring(html_elem).decode("utf-8"))


# Retrieving attributes - results in None if not present
print(f'{html_elem.get("lang") =}')
print(f'{html_elem.get("some") =}')

# Set attributes
html_elem.set("some", "Apple is fruit")

print(f'{html_elem.get("some") =}')

print(etree.tostring(html_elem).decode("utf-8"))

# <html lang="en_GB"/>
# html_elem.get("lang") ='en_GB'
# html_elem.get("some") =None
# html_elem.get("some") ='Apple is fruit'
# <html lang="en_GB" some="Apple is fruit"/>