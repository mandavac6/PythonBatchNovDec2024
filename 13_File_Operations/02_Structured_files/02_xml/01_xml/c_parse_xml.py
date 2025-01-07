"""
Purpose: Reading(Parsing) XML
"""

import xml.etree.ElementTree as ET
from pprint import pp

tree = ET.parse("books.xml")

books = {}
for each in tree.findall('book'):
    isbn= each.attrib['isbn']
    for each_sub in each.findall('title'):
        book_title = each_sub.text
        books[isbn] = book_title

pp(books)