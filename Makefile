.PHONY: debug
first: first.o
	ld -m elf_i386 -o first first.o

first.o: first.s
	nasm -f elf -o first.o first.s

debug:
	gdb -ex "layout asm" -ex "display/i $pc" -ex "break _start" -ex "run" first