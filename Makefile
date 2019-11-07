PY=python3
PY_SRC=src/heatmap_generator.py

RESULTS=mkdir -p results/
DATA=mkdir -p data/

RESULTS_DIR=results/
DATA_DIR=data/

ZIP_URL=https://physionet.org/static/published-projects/pmd/a-pressure-map-dataset-for-in-bed-posture-classification-1.0.0.zip
ZIP=data/dataset.zip

maps : $(PY_SRC)
	@$(RESULTS)
	$(PY) $(PY_SRC)

download:
	@$(DATA)
	@curl $(ZIP_URL) >> $(ZIP)
	@unzip $(ZIP) -d data/
	@rm $(ZIP)

clean:
	rm -rf results/*
