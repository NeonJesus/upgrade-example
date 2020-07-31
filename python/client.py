import argparse
import logging
import requests
import sys


handler = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(level=logging.DEBUG, handlers=[handler])


def main(url, num, seconds):
    logging.info(f'Contacting URL {url} for time.')
    resp = requests.get(url)
    if resp.status_code == 200:
        logging.info(f'Request returned successfully with {resp.status_code} and the message {resp.json()}')
    else:
        logging.error(f'Request failed with {resp.status_code}')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''Query Endpoint for
                                                    Tiemstamp a user
                                                    specified number
                                                    of times per second''')
    parser.add_argument('--url', type=str, dest='url', required=True,
                        help='URL to make request to.')
    parser.add_argument('--num', type=int, dest='num', default=1,
                        help='Number of Requests to make.')
    parser.add_argument('--sec', type=int, dest='seconds', default=60,
                        help='How long you want to make requests')
    args = parser.parse_args()
    main(args.url, args.num, args.seconds)
