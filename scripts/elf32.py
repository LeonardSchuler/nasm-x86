#!/usr/bin/env python3

def get_content():
    with open("first", "rb") as f:
        content = f.read()
    return content

def get_header(content):
    return content[:52]

def interpret_header(header):
    print(f"Magic number (0): 0x{header[:1].hex()}")
    print(f"Filetype (1-3): {header[1:4].decode('ascii')}")
    print(f"1 = little endian, 2 = big endian (4): {header[4]}")
    print(f"ELF header version (4): {header[6]}")
    print(f"OS ABI (7): {header[7]}")
    print("1 = relocatable, 2 = executable, 3 = shared, 4 = core (16-17):", int.from_bytes(header[16:18], 'little'))
    print("Instruction set (18-19):", int.from_bytes(header[18:20], 'little'))
    print("ELF Version (20-23):", int.from_bytes(header[20:24], 'little'))
    print(f"Program entry position (somewhat arbitrary but convention in Linux is 0x8049000) (24-27): 0x{header[27:23:-1].hex()} ==", int.from_bytes(header[24:28], 'little'))
    print("Program header table position (28-31):", int.from_bytes(header[28:32], 'little'))

def main():
    content = get_content()
    header = get_header(content)
    interpret_header(header)
    return header

if __name__ == "__main__":
    header = main()
