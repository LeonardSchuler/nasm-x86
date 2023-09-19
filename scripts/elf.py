#!/usr/bin/env python3

def get_content():
    with open("first", "rb") as f:
        content = f.read()
    return content

def get_header(content):
    return content[:52]

def main():
    content = get_content()
    header = get_header(content)

if __name__ == "__main__":
    main()
