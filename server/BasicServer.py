from http.server import BaseHTTPRequestHandler
import json

from server.Routes import Routes

from server.RequestApi import RequestApi


class HandleRequests(BaseHTTPRequestHandler):
    def do_GET(self):
        request = self.__make_request("GET")
        self.make_response(request)

    def do_POST(self):
        request = self.__make_request("POST")
        self.make_response(request)

    def do_PUT(self):
        request = self.__make_request("PUT")
        self.make_response(request)

    def do_DELETE(self):
        request = self.__make_request("DELETE")
        self.make_response(request)

    def make_response(self, request):
        if not request.error:
            response = Routes().get_routes(request)
            self.__set_headers(response.status)
            json_string = json.dumps(response.body)
            self.wfile.write(bytes(json_string, "utf-8"))
        else:
            self.__set_headers(400)
            self.wfile.write(bytes(request.error, "utf-8"))

    def __set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def __make_request(self, method):
        request = RequestApi()
        if not self.headers['Content-Type'] == "application/json":
            request.error = "Content-Type needs to be json"
            return request

        if 'Content-Length' in self.headers:
            request.body = self.rfile.read(int(self.headers['Content-Length']))

        request.path = self.path
        request.method = method

        return request
