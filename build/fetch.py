# Fetch files

# Author: Elliot Weishaar

import argparse
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
import ewtk_log


def main():
    parser = argparse.ArgumentParser(description="Download a file and verify integrity")
    logger = ewtk_log.Logger()
    print(logger.stream_log(WARNING, "WARNING"))
    print(logger.stream_log(INFO, "INFO"))


if __name__ == '__main__':
    main()
