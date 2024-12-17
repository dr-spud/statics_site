from textnode import TextType, TextNode
def main():
    node = TextNode(
        "hi hello hoiii",
        TextType.BOLD_TEXT,
        "www.youtube.com"
    )

    print(node)

if __name__ == "__main__":
    main()