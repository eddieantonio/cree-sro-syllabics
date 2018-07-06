all: Cans-to-Latn.py


%.py: %.fsm parse_foma.py
	python3 parse_foma.py -o $@ $<

%.fsm: %.xfscript
	printf "source $<\nsave stack $@\n" | foma


.PHONY: all
