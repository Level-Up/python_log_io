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
