import re

some_string = input()
title = re.findall(r"(?<=<title>)(.*)<\/title>", some_string)
title = "".join(title)
content = re.findall(r"(?<=<body>).+<\/body>", some_string)
content = "".join(content)
to_remove = re.findall(r"<[^>]+>|\\n", content)
for r in to_remove:
    if r in content:
        content = content.replace(r, "")
    if r in title:
        title = title.replace(r, "")
print(f"Title: {title}")
print(f"Content: {content}")
