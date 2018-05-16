#Grab the latest alpine image
FROM python:3.6.5-alpine3.6

# Install python and pip
# RUN apk add --no-cache --update python3 py-pip bash
ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt
RUN mkdir -p /var/www/supygirls

# Add local files to the image.
# ADD ./server /var/www/igames/

# Add kwarwp files to the image.
ADD ./src /var/www/supygirls

WORKDIR /var/www/supygirls/

# Expose is NOT supported by Heroku
# EXPOSE 8000

# Run the image as a non-root user
RUN adduser -D myuser
USER myuser

ARG ikt
ARG ikw
ARG port=80

ENV IKT=$ikt
ENV IKW=$ikw
ENV PORT=$port
# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
#CMD gunicorn wsgi
# Set-up app folder.
