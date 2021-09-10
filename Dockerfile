FROM joyzoursky/python-chromedriver:3.9-alpine-selenium

RUN mkdir packages
ADD requirements.txt packages
RUN pip install -r packages/requirements.txt

COPY ./app ./app

EXPOSE 80

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]