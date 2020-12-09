import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading


class MockHandleRequests(BaseHTTPRequestHandler):
    data = None

    def _set_headers(self, code):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path.endswith('/task_list'):
            self._set_headers(200)
            self.wfile.write(json.dumps({'Task1': 'GET',
                                         'Task2': 'POST',
                                         'Task3': 'PUT'}).encode())

        if self.path.endswith('/new'):
            self._set_headers(200)
            self.wfile.write(json.dumps({'hw6': 'SUCCES'}).encode())

        if self.path == '/server_error':
            self._set_headers(500)
            self.wfile.write(json.dumps({'Message': 'ServerError'}).encode())

    def do_POST(self):
        headers = dict(self.headers._headers)

        if self.path.endswith('/task_list'):
            self._set_headers(200)
            self.wfile.write(json.dumps({'Task1': 'GET',
                                         'Task2': 'POST',
                                         'Task3': 'PUT'}).encode())

        elif self.path.endswith('/new'):
            self._set_headers(200)
            self.wfile.write(json.dumps({'hw6': 'SUCCES'}).encode())

        elif self.path == '/server_error':
            self._set_headers(500)
            self.wfile.write(json.dumps({'Message': 'ServerError'}).encode())

        if 'Authorization' not in headers:
            self._set_headers(403)
            self.wfile.write(json.dumps({"Forbidden": 'Error'}).encode())

        else:
            if headers.get('Authorization') in self.data:

                    length = int(self.headers['Content-Length'])
                    post_data = self.rfile.read(length).decode()
                    self._set_headers(200)
                    self.wfile.write(json.dumps(post_data).encode())
            else:
                    self._set_headers(400)
                    self.wfile.write(json.dumps({"Incorrect login": 'Error'}).encode())

    def do_PUT(self):
        headers = dict(self.headers._headers)

        if self.path.endswith('/task_list'):
            self._set_headers(200)
            self.wfile.write(json.dumps({'Task1': 'GET',
                                         'Task2': 'POST',
                                         'Task3': 'PUT'}).encode())

        elif self.path.endswith('/new'):
            self._set_headers(200)
            self.wfile.write(json.dumps({'hw6': 'SUCCES'}).encode())

        elif self.path == '/server_error':
            self._set_headers(500)
            self.wfile.write(json.dumps({'Message': 'ServerError'}).encode())

        if 'Authorization' not in headers:
            self._set_headers(403)
            self.wfile.write(json.dumps({"Forbidden": 'Error'}).encode())

        else:
            if headers.get('Authorization') in self.data:

                length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(length).decode()
                self._set_headers(200)
                self.wfile.write(json.dumps(post_data).encode())
            else:
                self._set_headers(400)
                self.wfile.write(json.dumps({"Incorrect login": 'Error'}).encode())


class SimpleHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = MockHandleRequests
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()

    def set_data(self, data):
        self.handler.data = data


if __name__ == '__main__':
    server = SimpleHTTPServer('127.0.0.1', 1052)
    server.set_data({'max': 1})
    server.start()
