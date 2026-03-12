from pathlib import Path
from gencontent import generate_pages_recursive
from copystatic import clean_copytree
import sys

BASE = Path(__file__).parent.parent
STATIC = BASE / "static"
PUBLIC = BASE / "docs"
CONTENT = BASE / "content"
TEMPLATE = BASE / "template.html"


def main() -> None:
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print(basepath)

    clean_copytree(STATIC, PUBLIC)
    generate_pages_recursive(CONTENT, TEMPLATE, PUBLIC, basepath)


if __name__ == "__main__":
    main()
