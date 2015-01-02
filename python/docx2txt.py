#!/usr/bin/python

# Convert a .docx file to plain text

import zipfile, re, sys

if len(sys.argv) != 2:
    sys.exit('Usage: ' + sys.argv[0] + ' INPUT.docx')

docx = zipfile.ZipFile(sys.argv[1])
content = docx.read('word/document.xml')
content = re.sub('</w:p>', '\n', content)
content = re.sub('<(.|\n)*?>', '', content)
cleaned = re.sub('\n\s*\n', '\n', content)
print cleaned
