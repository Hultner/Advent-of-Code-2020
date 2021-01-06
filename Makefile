DAY := $(shell date +%d)

ifdef $$DAY
	DAY := $$DAY
endif

.PHONY : day
day: 
	cp -r aoc/day_XX aoc/day_$(DAY)
	cp tests/test_day_XX.py tests/test_day_$(DAY).py
	sed -i '' "s/XX/$(DAY)/g" aoc/day_$(DAY)/core.py
	sed -i '' "s/XX/$(DAY)/g" tests/test_day_$(DAY).py

build:
	rm aoc.o
	(cd aoc; zip -r -9 ../aoc.o .)
	chmod +x aoc.o
	ex -s -c '1i|#!/usr/bin/env python3' -c x aoc.o

