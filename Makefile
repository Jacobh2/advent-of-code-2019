pytest:
	docker build -f Dockerfile.pytest -t pytest . && docker run --rm -it pytest

#make javascript FOLDER=day_1 FILE=part1.mjs
javascript:
	docker build -f Dockerfile.nodejs -t nodejs . && docker run --rm -it nodejs node --experimental-modules $(FOLDER)/$(FILE)  $(FOLDER)