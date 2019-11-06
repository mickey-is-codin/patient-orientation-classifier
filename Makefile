PY=python3
PY_SRC=src/heatmap_generator.py
RESULTS=mkdir -p results/

maps : $(PY_SRC)
	@$(RESULTS)
	$(PY) $(PY_SRC)
