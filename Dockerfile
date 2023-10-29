FROM python:3.9 as production-stage
WORKDIR /usr/back-rpg-brenner
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .