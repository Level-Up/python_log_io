 log.io logging handler
  6 ======================
  7 
  8 Handler for the python logging framework for log.io stateless TCP API
  9 
 10 http://logio.org/
 11 
 12 Usage:
 13 ::
 14 
 15 from log_io_handler import LogIOHandler
 16 
 17 Logger.addHandler(LogIOHandler)
 18 
 19 #or dict_config
 20 'handlers'
 21         'log_io': {
 22             'level': 'DEBUG',
 23             'class': 'log_io_handler.LogIOHandler',
 24             #optional configs
 25             'logstream': 'EXAMPLE_STREAM',
 26             'node': 'EXAMPLE_NODE',
 27             'host': 'EXAMPLE_HOST',
 28             'port': 28777,
 29         }
 30 
 31     logstream: name of log.io stream default (PythonStream)
 32     node: name of log.io node default (PythonNode)
 33     host: log.io server domain or ip address  (default localhost)
 34     port: log.io api port (default 28777)
