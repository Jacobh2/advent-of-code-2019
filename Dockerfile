FROM python:3.7 AS build

WORKDIR /usr/src/install

COPY requirements.txt requirements.txt

RUN pip wheel -r requirements.txt 

FROM python:3.7-slim AS RUN

WORKDIR /usr/src/install

COPY --from=build /usr/src/install .

RUN pip install -r requirements.txt -f .

WORKDIR /usr/src/app

RUN rm -rf /usr/src/install

COPY . .

CMD ["python", "-m", "pytest"]
