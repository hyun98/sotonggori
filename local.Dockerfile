FROM python:3.9.0

RUN echo "test"

COPY ./ /home/sotongapp/

WORKDIR /home/sotongapp/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "-c", "python manage.py runserver 0.0.0.0:8000 --settings=config.settings.local"]
