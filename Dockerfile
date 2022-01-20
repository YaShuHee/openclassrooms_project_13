FROM python:3.9-alpine3.15

# copy all the not ignored content in /app/ image directory
COPY . app/
# set working directory for next commands
WORKDIR app/

# install all required libraries for the image
RUN pip install -r requirements.txt

# collect the static files so the admin interface still has its css
RUN mkdir -p statics
RUN python manage.py collectstatic --noinput

# default port, can be changed when creating a container
EXPOSE 8000

# run the application using gunicorn server, when a container is runned
CMD gunicorn --pythonpath oc_lettings_site oc_lettings_site.wsgi