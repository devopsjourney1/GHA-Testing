from flask import Flask, render_template, request
import socket
import os
import time
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

# Get environment variables, or set defaults
background_color    = os.environ.get('BACKGROUND_COLOR', '#a8d1df ')
custom_text         = os.environ.get('CUSTOM_TEXT', 'Hello World!')
text_color          = os.environ.get('TEXT_COLOR', 'black')
title               = os.environ.get('APP_NAME', 'Dockerized Flask App')
version             = os.environ.get('APP_VERSION', 'v1.0.0')


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route("/")
def hello_world():
    # Get the hostname of the container
    hostname = socket.gethostname()
    hit_count = get_hit_count()
    # Renders templates/index.html with the variables
    return render_template('index.html', 
                            title=title,
                            custom_text=custom_text,
                            hit_count=hit_count,
                            version=version,
                            hostname=hostname,
                            background_color=background_color, 
                            text_color=text_color)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=3000)