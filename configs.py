# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("3261311", ""))
    API_HASH = os.environ.get("41377ec3060b15a5105dbe1e8af95c99", "")
    BOT_TOKEN = os.environ.get("1970829702:AAFDF5g1c3vc9z3RPLFTPELurC17IiRJ3Ug", "")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("1869495895", ""))
    PRO_USERS = list(set(int(x) for x in os.environ.get("1869495895", "0").split()))
    PRO_USERS.append(1869495895)
    MONGODB_URI = os.environ.get("mongodb+srv://amal:amal@cluster0.fiw9iam.mongodb.net/?retryWrites=true&w=majority", "")
    LOG_CHANNEL = int(os.environ.get("-1001568469839", ""))
    BROADCAST_AS_COPY = bool(os.environ.get("False", "False"))
