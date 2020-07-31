import logging
import sys
import json
from flask import Flask
from datetime import datetime

handler = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(level=logging.DEBUG, handlers=[handler])


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def timestamp():
    logging.info('Request for Time received')
    time = datetime.now()
    message = {'date': time.isoformat()}
    logging.info(f'Returning the time: {message}')
    return json.dumps(message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
