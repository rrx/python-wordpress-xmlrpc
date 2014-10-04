"""
Library to interface with the WordPress XML-RPC API.

See README for usage instructions.
"""
from wordpress_xmlrpc.base import *
from wordpress_xmlrpc.wordpress import *
from . import methods

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())