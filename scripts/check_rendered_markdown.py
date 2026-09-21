"""Check every built documentation page for Markdown rendering regressions."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


class Article(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.active = False
        self.depth = 0
        self.items = Counter()
        self.text = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "article":
            self.active = True
        if self.active and tag == "li":
            self.depth += 1
            self.items[self.depth] += 1

    def handle_endtag(self, tag):
        if self.active and tag == "li":
            self.depth -= 1
        if tag == "article":
            self.active = False

    def handle_data(self, text):
        if self.active:
            self.text.append(text)


def main():
    errors = []
    pages = 0
    for source in sorted(Path("docs").glob("*.md")):
        target = Path("site/index.html") if source.stem == "index" else Path("site") / source.stem / "index.html"
        if not target.exists():
            errors.append(f"{source}: built page is missing")
            continue
        pages += 1
        article = Article(target.read_text(encoding="utf-8"))
        markdown = source.read_text(encoding="utf-8")
        expected = Counter()
        expected[1] = len(re.findall(r"<li(?:\s|>)", markdown))
        for match in re.finditer(r"^( *)(?:\* |\d+\. )", markdown, re.MULTILINE):
            expected[len(match[1]) // 4 + 1] += 1
        if +expected != +article.items:
            errors.append(f"{source}: list items by nesting depth: expected {dict(+expected)}, rendered {dict(+article.items)}")
        # These docs contain no literal asterisks or Markdown code examples.
        visible = "".join(article.text)
        if re.search(r"\*|!\[|\{\s*width=|^\s*#{1,6} ", visible, re.MULTILINE):
            errors.append(f"{source}: unrendered Markdown appears in the article")
    if not pages:
        errors.append("No documentation pages checked")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Verified {pages} pages: all list items and nesting levels render correctly; no literal Markdown markers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
