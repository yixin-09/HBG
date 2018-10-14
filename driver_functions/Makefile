include /home/yixin/experiment/HBG/herbgrind/Makefile.common

FLAGS=-g -Wall -DHAVE_INLINE -std=c11 -lm -lgsl -lgslcblas -lmpfr -lgmp -I/home/yixin/experiment/HBG/herbgrind/valgrind/herbgrind/include/ -I/home/yixin/experiment/HBG/herbgrind/deps/gmp-64/ -I/home/yixin/experiment/HBG/herbgrind/deps/mpfr-64/src/

CSRC = $(wildcard *.c)
COUT = $(patsubst %.c,%.out,$(CSRC))

CC ?= gcc

# NOTE : does not build mini-nocall.sout (trouble on osx)
all: $(COUT)

%.out: %.c
	$(CC) -o $@ $< $(FLAGS)
	chmod u+x $@
%.sout: %.s
	$(CC) $(FLAGS) -o $@ $<
	chmod u+x $@

%.s: %.c
	$(CC) $(FLAGS) -S -o $@ $<

clean:
	rm -rf *.out *.sout *.dSYM
