# new_post.py
import sys
from datetime import date
import os

title = " ".join(sys.argv[1:])
slug = title.lower().replace(" ", "-")
today = date.today().isoformat()
filename = f"posts/{today}-{slug}.md"

template = f"""---
title: {title}
slug: {slug}
date: {today}
---

Write your blog here in **Markdown**.

You can add images like:
![alt text](/media/{slug}/image.png)

And links like:
[Visit OpenAI](https://dn.ht)
"""

os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write(template)

print(f"Created: {filename}")
