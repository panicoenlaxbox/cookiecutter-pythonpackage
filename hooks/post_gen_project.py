import os

path = os.path.join(os.path.realpath(os.path.curdir), ".env")
with open(path, "rt") as f:
    content = f.read()
content = content.replace("${USERPROFILE}", os.environ["USERPROFILE"])
with open(path, "wt") as f:
    f.write(content)
