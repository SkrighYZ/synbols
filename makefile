SHELL=/bin/bash
userid := $(shell id -u)
versiontag = $(shell date +%Y-%m-%d)

SYNBOLS_RUN = docker run --user $(userid) -it -v $(CURDIR)/generator:/generator -v $(CURDIR):/local synbols

docker:
	docker build -t synbols:latest .
	docker tag synbols:latest synbols:$(versiontag)

font-cache:
	rm alphabet_fonts.cache; $(SYNBOLS_RUN) sh -c "cd /local; python -c 'from synbols.fonts import ALPHABET_MAP'"

font-licenses:
	$(SYNBOLS_RUN) cat font_licenses.csv
	@echo "All licenses were automatically extracted based on the directory structure of the Google Fonts repository (https://github.com/google/fonts). Refer to this repository for license details."

view-dataset:
	$(SYNBOLS_RUN) sh -c "cd /local; python ../generator/view_dataset.py"
	open dataset.png

dataset:
	$(SYNBOLS_RUN) sh -c "cd /local; python ../generator/generate_dataset.py"

test:
	$(SYNBOLS_RUN) sh -c "cd /local; python ../generator/view_generator.py"

view_font_clusters:
	$(SYNBOLS_RUN) sh -c "cd /local; python ../generator/view_font_clustering.py"

datasets:
	generator/generate_dataset.py --n_samples=100000 > default.log &
	generator/generate_dataset.py --dataset=camouflage --n_samples=100000 > camouflage.log &
	generator/generate_dataset.py --dataset=tiny --n_samples=10000 > tiny.log &
	generator/generate_dataset.py --dataset=segmentation --n_samples=100000 > segmentation.log &
	generator/generate_dataset.py --dataset=missing-symbol --n_samples=100000 > missing-symbol.log &
	generator/generate_dataset.py --dataset=less_variations --n_samples=100000 > less_variations.log &
	wait
	generator/generate_dataset.py --n_samples=1000000 > default_1M.log &
	generator/generate_dataset.py --dataset=all_fonts --n_samples=1000000 > all_fonts_1M.log &
	generator/generate_dataset.py --dataset=all_chars --n_samples=1000000 > all_chars_1M.log &
	generator/generate_dataset.py --dataset=less_variations --n_samples=1000000 > less_variations_1M.log &
	wait

splits:
	$(SYNBOLS_RUN) sh -c "cd /local; python ../generator/generate_splits.py"


font_check:
	$(SYNBOLS_RUN) sh -c "cd /local; python generator/run_font_checks.py"
