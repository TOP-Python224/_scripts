from sys import path

script_dir = path[0]

test_page = '\\'.join((script_dir, 'Test Page.html'))

html_page = [
    '<html>\n',
    '\t<body>\n',
    '\t\t<h1>Test Page</h1>\n',
    '\t\t<div class=style1>\n',
    '\t\t\t<p>Test text for test page.</p>\n',
    '\t\t</div>\n',
    '\t</body>\n',
    '</html>\n',
]

with open(test_page, 'w', encoding='utf-8') as f_out:
    f_out.writelines(html_page)


with open(test_page, encoding='utf-8') as f_in:
    print(f_in.read())
