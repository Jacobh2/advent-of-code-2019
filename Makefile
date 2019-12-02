pytest:
	docker build -f Dockerfile.pytest -t pytest . && docker run --rm -it pytest

day1-part1-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_1/part1.py

day1-part2-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_1/part2.py

day1-part1-js:
	docker build -f Dockerfile.nodejs -t nodejs . && docker run --rm -it nodejs node --experimental-modules day_1/part1.mjs  day_1

day1-part2-js:
	docker build -f Dockerfile.nodejs -t nodejs . && docker run --rm -it nodejs node --experimental-modules day_1/part2.mjs  day_1