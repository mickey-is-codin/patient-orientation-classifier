PY=python3
PY_SRC=src/heatmap_generator.py

maps : $(PY_SRC)
	$(PY) $(PY_SRC)
