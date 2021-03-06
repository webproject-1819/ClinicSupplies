FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code


RUN pip install pipenv
RUN pipenv install --system --deploy

COPY clinicsupplies ./clinicsupplies
COPY drugshop ./drugshop
COPY templates ./templates
COPY manage.py ./

ENV PORT 8000
EXPOSE $PORT
RUN python manage.py collectstatic --noinput
# Init DB if local, might also require `$> python manage.py createsuperuser`
RUN python manage.py migrate
# Set DJANGO_SETTINGS_MODULE=myrecommendations.settings_heroku when deployin on Heroku
CMD gunicorn -b 0.0.0.0:$PORT clinicsupplies.wsgi
