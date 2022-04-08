"""
Name: cleaner.py
Authors: lawlesst
Cleaning invalid characters from xml
https://gist.github.com/lawlesst/4110923
"""

import sys
import re

def invalid_xml_remove(char):
    """Tracks illegal unicode characters"""
    #http://stackoverflow.com/questions/1707890
    # /fast-way-to-filter-illegal-xml-unicode-chars-in-python
    illegal_unichrs = [ (0x00, 0x08), (0x0B, 0x1F), (0x7F, 0x84), (0x86, 0x9F),
                    (0xD800, 0xDFFF), (0xFDD0, 0xFDDF), (0xFFFE, 0xFFFF),
                    (0x1FFFE, 0x1FFFF), (0x2FFFE, 0x2FFFF), (0x3FFFE, 0x3FFFF),
                    (0x4FFFE, 0x4FFFF), (0x5FFFE, 0x5FFFF), (0x6FFFE, 0x6FFFF),
                    (0x7FFFE, 0x7FFFF), (0x8FFFE, 0x8FFFF), (0x9FFFE, 0x9FFFF),
                    (0xAFFFE, 0xAFFFF), (0xBFFFE, 0xBFFFF), (0xCFFFE, 0xCFFFF),
                    (0xDFFFE, 0xDFFFF), (0xEFFFE, 0xEFFFF), (0xFFFFE, 0xFFFFF),
                    (0x10FFFE, 0x10FFFF) ]

    illegal_ranges = [f"{chr(low)}-{chr(high)}"
                  for (low, high) in illegal_unichrs
                  if low < sys.maxunicode]

    illegal_xml_re = re.compile(f'[{"".join(illegal_ranges)}]')
    if illegal_xml_re.search(char) is not None:
        #Replace with space
        return ''
    else:
        return char

def scrub_literal(value):
    """
    Scrubs control characters from the incoming values to remove
    things like form feeds (\f) and line breaks (\n) which might
    cause problems with Jena.
    Data with these characters was found in the Backstage data.
    """
    if not value:
        return None
    if isinstance(value, int):
        return value
    text = ''.join([c for c in value if not ascii.iscntrl(c)\
                if not ascii.isctrl(c)])
    text = text.replace('"', '')
    text = text.replace('\ufffd', '')
    text = clean_char(text)
    if isinstance(text, str):
        text = str(text, errors='replace')
    return text.strip()

def clean_char(char):
    """
    Function for remove invalid XML characters from
    incoming data.
    """
    #Get rid of the ctrl characters first.
    #http://stackoverflow.com/questions/1833873/python-regex-escape-characters
    char = re.sub('\x1b[^m]*m', '', char)
    #Clean up invalid xml
    char = invalid_xml_remove(char)
    replacements = [
        ('\u201c', '\"'),
        ('\u201d', '\"'),
        ("\u001B", ''), #http://www.fileformat.info/info/unicode/char/1b/index.htm
        ("\u0019", ''), #http://www.fileformat.info/info/unicode/char/19/index.htm
        ("\u0016", ''), #http://www.fileformat.info/info/unicode/char/16/index.htm
        ("\u001C", ''), #http://www.fileformat.info/info/unicode/char/1c/index.htm
        ("\u0003", ''), #http://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=0x
        ("\u000C", '')
    ]
    for rep, new_char in replacements:
        if char == rep:
            return new_char
    return char