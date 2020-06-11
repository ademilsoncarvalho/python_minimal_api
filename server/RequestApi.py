import json
from urllib import parse


class RequestApi:

    def __init__(self):
        self.__body = None
        self.__path = None
        self.__method = None
        self.__params = {}
        self.__error = None

    @property
    def error(self):
        return self.__error

    @property
    def params(self):
        return self.__params

    @error.setter
    def error(self, error):
        self.__error = error

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, method):
        self.__method = method

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        url = parse.urlparse(path)
        params = parse.parse_qs(parse.urlsplit(path).query)
        # get first item param request
        self.__params.update({k: v[0] for k, v in params.items()})
        self.__path = url.path

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__params.update(json.loads(body))
        self.__body = body

    def __str__(self):
        return f" Body : {self.__body}" \
               f" Params : {self.__params}" \
               f" Path : {self.__params}" \
               f" Method : {self.__method}"
