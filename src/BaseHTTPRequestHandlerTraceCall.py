# coding: utf-8
from __future__ import absolute_import

import aoiktracecall.config
import aoiktracecall.trace


# Only `aoiktracecall` modules are imported here.
# Other modules should be imported after `trace_calls_in_specs` is called.


# Set `FIGLET_WIDTH` to control how figlet wraps
aoiktracecall.config.set_config('FIGLET_WIDTH', 200)


# Trace specs
trace_specs = [
    ('aoiktracecall([.].+)?', False),

    ('.+[.]copy', False),

    ('.+[.]__setattr__', True),

    ('.+[.]log_request', {'hide_below'}),

    ('socket.IntEnum', False),

    ('socket._intenum_converter', False),

    ('socket[.].+[.]getsockname', False),

    ('socket[.].+[.]getpeername', False),

    ('(socket|SocketServer)[.].+[.]fileno', False),

    ('socket._realsocket', False),

    # `SocketIO` is in Python 3
    ('socket[.]SocketIO[.]readinto', {'highlight'}),

    ('socket[.]SocketIO[.]write', {'highlight'}),

    ('socket[.]SocketIO[.]flush', {'highlight'}),

    ('socket[.]SocketIO[.]close', {'highlight'}),

    ('socket[.]SocketIO[.]__(?!init)[^.]+__', False),

    ('socket[.]SocketIO[.].+', True),

    ('socket[.].+[.]__init__', {'highlight'}),

    ('socket[.].+[.]__[^.]+__', False),

    ('socket([.].+)?', {'highlight'}),

    ('selectors.ABCMeta', False),

    ('selectors.Mapping', False),

    ('selectors.SelectSelector', False),

    ('selectors.DefaultSelector.__init__', {'highlight'}),

    ('selectors.DefaultSelector.select', 'hide_tree'),

    ('selectors.DefaultSelector.register', {'highlight'}),

    ('selectors[.].+[.]__[^.]+__', False),

    ('selectors([.].+)?', True),

    # `socketserver` is in Python 3.
    # `SocketServer` is in Python 2.
    ('(socketserver|SocketServer)._eintr_retry', False),

    ('(socketserver|SocketServer)._ServerSelector', False),

    ('(socketserver|SocketServer)[.].+[.]service_actions', False),

    ('(socketserver|SocketServer)[.].+[.]__(?!init)[^.]+__', False),

    ('(socketserver|SocketServer)([.].+)?', {'highlight'}),

    # `http` is in Python 3
    ('http[.].+[.]__(?!init)[^.]+__', False),

    ('http([.].+)?', {'highlight'}),

    # `BaseHTTPServer` is in Python 2
    ('BaseHTTPServer[.].+[.]__(?!init)[^.]+__', False),

    ('BaseHTTPServer([.].+)?', {'highlight'}),

    # `email` is used for parsing HTTP headers in Python 3
    ('email[.].+[.]__(?!init)[^.]+__', False),

    ('email([.].+)?', {'highlight'}),

    # `mimetools` is used for parsing HTTP headers in Python 2
    ('mimetools[.].+[.]__(?!init)[^.]+__', False),

    ('mimetools([.].+)?', {'highlight'}),

    # Remove 'hide_below' to see the parsing details
    ('__main__.CustomHandler.parse_request', {
        'highlight', 'hide_below'
    }),

    ('__main__[.].+[.]__(?!init)[^.]+__', False),

    ('__main__([.].+)?', {'highlight'}),
]


# Trace calls in specs
aoiktracecall.trace.trace_calls_in_specs(specs=trace_specs)


# Import modules after `trace_calls_in_specs` is called
import sys


# If is Python 2
if sys.version_info[0] == 2:
    from BaseHTTPServer import BaseHTTPRequestHandler
    from SocketServer import TCPServer

# If is Python 3
else:
    from http.server import BaseHTTPRequestHandler
    from socketserver import TCPServer


class CustomHandler(BaseHTTPRequestHandler):
    """
    This HTTP request handler echoes request body in response body.
    """

    def do_POST(self):
        # Get request header `Content-Length`
        content_length = int(self.headers.get('content-length', 0))

        # Read request body
        request_body = self.rfile.read(content_length)

        # Send response status
        self.send_response(200)

        # Send response header `Content-Length`
        self.send_header('Content-Length', str(len(request_body)))

        # End headers
        self.end_headers()

        # Send response body
        self.wfile.write(request_body)


def main():
    try:
        # Create `TCPServer` with `CustomHandler`
        server = TCPServer(
            ('127.0.0.1', 8000), CustomHandler
        )

        # Serve forever
        server.serve_forever()

    # If have `KeyboardInterrupt`
    except KeyboardInterrupt:
        # Ignore
        pass


# Trace calls in this module
aoiktracecall.trace.trace_calls_in_this_module()


# If is run as main module
if __name__ == '__main__':
    # Call main function
    exit(main())
