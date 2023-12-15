FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /code

# Установка зависимостей проекта
COPY ./requirements.txt /code/
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Перенос проекта в образ
COPY ./app /code/app

# Копирование файлов alembic
COPY ./entrypoint.sh /code/entrypoint.sh

RUN chmod +x /code/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/code/entrypoint.sh"]