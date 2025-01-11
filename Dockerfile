# образ на основе которого создаём контейнер
FROM python:3.10.11

# рабочая директория внутри проекта
WORKDIR /app/

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE="1"
ENV PYTHONUNBUFFERED="1"

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
# копируем содержимое текущей папки в контейнер
COPY . .
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
