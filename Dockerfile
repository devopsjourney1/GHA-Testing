FROM alpine:3.15
WORKDIR /app
RUN apk --no-cache add python3 py3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY app.py .
COPY templates/ templates/
ARG APP_VERSION="alpha"
ENV APP_VERSION=${APP_VERSION}
CMD ["python3", "app.py"]