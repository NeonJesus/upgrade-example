import flask
import logging
import sys
from datetime import datetime

handler = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(level=logging.DEBUG, handlers=[handler])


def timestamp():
    logging.info('Request for Time received')
    time = datetime.now()
    logging.info(f'Returning the time: {time}')


if __name__ == '__main__':
    timestamp()
