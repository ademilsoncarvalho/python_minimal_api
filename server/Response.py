class Response:

    def __init__(self, status, body=''):
        self.__body = body
        self.__status = status

    @property
    def status(self):
        return self.__status

    @property
    def body(self):
        return self.__body
