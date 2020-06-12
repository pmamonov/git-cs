SCRIPTS += git-cs.py

.PHONY: $(SCRIPTS)

all: $(SCRIPTS)

$(SCRIPTS):
	python $@

clean:
	rm -f *.png *.pyc
