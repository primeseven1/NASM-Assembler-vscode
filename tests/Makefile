C_SOURCE_FILES := $(shell find ./ -name '*.c')

all:
	gcc -c $(C_SOURCE_FILES) -S -masm=intel

clean:
	rm -f *.s