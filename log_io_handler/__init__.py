import logging
from emitter import Send

"""
log.io logging handler
======================

Handler for the python logging framework for log.io stateless TCP API

http://logio.org/

Usage:
::

from log_io_handler import LogIOHandler

Logger.addHandler(LogIOHandler)

#or dict_config
'handlers'
        'log_io': {
            'level': 'DEBUG',
            'class': 'log_io_handler.LogIOHandler',
            #optional configs
            'logstream': 'EXAMPLE_STREAM',
            'node': 'EXAMPLE_NODE',
            'host': 'EXAMPLE_HOST',
            'port': 28777,
        }

    logstream: name of log.io stream default (PythonStream)
    node: name of log.io node default (PythonNode)
    host: log.io server domain or ip address  (default localhost)
    port: log.io api port (default 28777)
"""

VERSION = '1.1'
AUTHOR = "Raymond McGinlay"
EMAIL = "raymond@thisislevelup.com"
URL = "www.thisislevelup.com"


class LogIOHandler(logging.Handler):
    """A log handler that transmits log entries to log.io server.

    If the request is passed as the first argument to the log record,
    request data will be provided in the report.
    """

    def __init__(self, logstream='PythonStream',
                 node='PythonNode',
                 host='localhost',
                 port=28777):
        logging.Handler.__init__(self)
        self.logstream = logstream
        self.node = node
        self.host = host
        self.port = port

    def emit(self, record):
        message = self.format(record)
        msg_string = "+log|%s|%s|info|%s\r\n" %\
            (self.logstream, self.node, message)
        Send.config_dict = {'host': self.host, 'port': self.port}
        Send(msg_string)
