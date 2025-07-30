# write/utils.py
import markdown
from pathlib import Path
from django.conf import settings

def read_markdown(slug):
    post_dir = Path(settings.BASE_DIR) / 'posts' / slug / 'index.md'
    if not post_dir.exists():
        return None
    with open(post_dir, 'r', encoding='utf-8') as f:
        content = f.read()
    html = markdown.markdown(content, extensions=['fenced_code', 'codehilite'])
    return html
