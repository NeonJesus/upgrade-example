import flask
import logging
import sys
import json
from datetime import datetime

handler = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(level=logging.DEBUG, handlers=[handler])


def timestamp():
    logging.info('Request for Time received')
    time = datetime.now()
    message = {'date': time.isoformat()}
    logging.info(f'Returning the time: {message}')
    return json.dumps(message)


if __name__ == '__main__':
    timestamp()
