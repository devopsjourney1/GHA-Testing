FROM alpine:3.15
WORKDIR /app
RUN apk --no-cache add python3=3.9.18-r0 py3-pip=20.3.4-r1 curl=-8.4.0-r0
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY app.py .
COPY templates/ templates/
ARG APP_VERSION="alpha"
ENV APP_VERSION=${APP_VERSION}
CMD ["python3", "app.py"]