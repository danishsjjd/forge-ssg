from forge_ssg.markdown.textnode import TextNode, TextType


def main() -> None:
    node = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.exmaple.com"
    )
    print(node)


if __name__ == "__main__":
    main()
