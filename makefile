install:
	pip install uv
	pip install --upgrade uv
	uv venv tetris
	.venv\Scripts\activate
	uv pip install -r pyproject.toml

run:
	uv run main.py

build_dist:
	uv build