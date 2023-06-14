FROM python:3.11.4-bullseye
RUN mkdir /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5080
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh","entrypoint.sh"]