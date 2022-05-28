# Pull base image
FROM python:3.9.6-alpine

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOME=$WORKDIR
ENV APP_HOME=$WORKDIR

# Install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Create secret key
RUN export SECRET=`python -c "import secrets; print(secrets.token_urlsafe())"`

# Copy entrypoint
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy project
COPY . .
RUN mkdir $WORKDIR/staticfiles

# Entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
