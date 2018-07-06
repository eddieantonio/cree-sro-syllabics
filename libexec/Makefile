all: Cans-to-Latn.py


%.py: %.fsm
	python3 parse_foma.py $< > $@

%.fsm: %.xfscript
	printf "source $<\nsave stack $@\n" | foma


.PHONY: all
.DELETE_ON_ERROR:
