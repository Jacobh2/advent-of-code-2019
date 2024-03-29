pytest:
	docker build -f Dockerfile.pytest -t pytest . && docker run --rm -it pytest

# DAY 1
day1-part1-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_1/part1.py

day1-part2-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_1/part2.py

day1-part1-js:
	docker build -f Dockerfile.nodejs -t nodejs . && docker run --rm -it nodejs node --experimental-modules day_1/part1.mjs  day_1

day1-part2-js:
	docker build -f Dockerfile.nodejs -t nodejs . && docker run --rm -it nodejs node --experimental-modules day_1/part2.mjs  day_1

# DAY 2
day2-part1-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_2/part1.py

day2-part2-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_2/part2.py

# DAY 3
day3-part1-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_3/part1.py

day3-part2-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_3/part2.py

# DAY 4
day4-part1-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_4/part1.py

day4-part2-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_4/part2.py

# DAY 5
day5-part1-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_5/part1.py

day5-part2-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_5/part2.py

# DAY 6
day6-part1-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_6/part1.py

day6-part2-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_6/part2.py

# DAY 7
day7-part1-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python -m day_7.part1

day7-part2-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_7/part2.py

# DAY 8
day8-part1-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_8/part1.py

day8-part2-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_8/part2.py

# DAY 9
day9-part1-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_9/part1.py

day9-part2-py:
	docker build -f Dockerfile.pytest -t pythonrun . && docker run --rm -it pythonrun python day_9/part2.py