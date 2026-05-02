m: manage

manage:
	uv run python manage.py $(filter-out $@ m,$(MAKECMDGOALS))

lint-fix:
	uv run ruff check --fix .
	uv run ruff format .
	uv run djlint . --reformat

lint-check:
	uv run ruff check .
	uv run djlint . --lint

%:
	@:
