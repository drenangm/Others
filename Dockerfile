FROM python:3.7.8

COPY . /app
COPY './requirements.txt' .
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PORT=5020
EXPOSE $PORT

CMD ["python", "main.py"]