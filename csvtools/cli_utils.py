import logging
import sys


def configure_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=level)


def configure_stdin_encoding(encoding: str) -> None:
    if "reconfigure" in dir(sys.stdin):
        sys.stdin.reconfigure(encoding=encoding)
        logging.debug('encoding %s applied', encoding)
    else:
        logging.debug('using default encoding')
