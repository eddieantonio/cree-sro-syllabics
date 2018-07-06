all: Cans-to-Latn.txt

%.txt: %.fsm
	<$< gunzip >$@
%.fsm: %.xfscript
	printf "source $<\nsave stack $@\n" | foma
