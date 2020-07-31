import argparse
import logging


handler = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(level=logging.DEBUG, handlers=[handler])


main():
    logging.info('TODO')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''Query Endpoint for
                                                    Tiemstamp a user
                                                    specified number
                                                    of times per second''')
    parser.add_argument('--num',
                        type=int,
                        dest='num',
                        help='Number of Requests to make.')
    args = parser.parse_args()
    main()
