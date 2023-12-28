FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

#COPY ./entrypoint.sh /code/entrypoint.sh

#RUN chmod +x /code/entrypoint.sh

#EXPOSE 80

#ENTRYPOINT ["/code/entrypoint.sh"]
CMD ["python", "app/main.py"]