from cleaner_utils.cleaner import clean_char
from xml.sax.saxutils import escape

def escape_value(text: str) -> str:
    """Escape the illegal characters for an ontology property"""
    if text is None:
        return None
    # function to escape XML character data
    text = escape(text)
    text = text.replace('\n', '')
    text = text.replace('\r', '')
    text = text.replace('\f', '')
    text = text.replace('\b', '')
    text = text.replace('"', '')
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace('{', '')
    text = text.replace('}', '')
    text = text.replace('#', '')
    text = text.replace('|', '')
    text = clean_char(text)
    return text

def escape_iri(text: str) -> str:
    """For IRI, we replace space character by _"""
    if text is None:
        return None
    text = escape_value(text)
    text = text.replace(' ', '_')
    text = text.replace('.', '_')
    return text