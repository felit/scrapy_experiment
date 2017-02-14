# -*- coding:utf8 -*-
import logging

from scrapy.extensions.feedexport import IFeedStorage
from zope.interface import implementer

logger = logging.getLogger(__name__)

# TODO
@implementer(IFeedStorage)
class MongodbStorage():
    def __init__(uri):
        logger.info('uri:%s', uri)
        """Initialize the storage with the parameters given in the URI"""

    def open(spider):
        """Open the storage for the given spider. It must return a file-like
        object that will be used for the exporters"""

    def store(file):
        """Store the given file stream"""