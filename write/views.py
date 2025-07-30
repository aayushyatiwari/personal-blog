import os
from django.shortcuts import render, Http404
from pathlib import Path
import markdown
import yaml
from django.conf import settings

POST_DIR = Path(settings.BASE_DIR) / "posts"

def load_post(slug):
    path = POST_DIR / slug / "index.md"
    if not path.exists():
        raise Http404("Post not found.")

    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    try:
        meta_raw, content = raw.split('---\n', 2)[1:]
        metadata = yaml.safe_load(meta_raw)
    except Exception:
        raise Http404("Invalid post format.")

    html = markdown.markdown(content)
    return {
        "title": metadata.get("title", "Untitled"),
        "date": metadata.get("date", ""),
        "slug": slug,
        "content": html,
    }

def home(request):
    posts = []
    for folder in sorted(POST_DIR.iterdir(), reverse=True):
        if folder.is_dir():
            try:
                post = load_post(folder.name)
                posts.append(post)
            except:
                continue
    return render(request, "home.html", {"posts": posts})

def post_detail(request, slug):
    post = load_post(slug)
    return render(request, "post.html", {"post": post})

def about(request):
    return render(request, "about.html")
