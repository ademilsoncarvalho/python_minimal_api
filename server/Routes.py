import inspect
import os

from server.Response import Response


class Routes:
    PATH_CONTROLLERS = 'routes/controllers'
    DIR_NAME = os.path.dirname(__file__)

    def __init__(self):
        pass

    def get_routes(self, request):

        try:
            http_method = request.method
            route = self.__get_class_method(request)
            str_class = route['class']
            str_method = route['method'] + "_" + http_method.lower()

            if not self.__verify_class_exists(str_class):
                raise Exception("Controller not found")

            module = __import__(self.PATH_CONTROLLERS.replace('/', '.') + '.' + str_class, fromlist=[str_class])
            if not inspect.ismodule(module):
                raise Exception("Controller not found")
            class_route = getattr(module, str_class)
            if not callable(class_route):
                raise Exception("Controller not found")
            class_invoke = class_route()
            method = getattr(class_invoke, str_method)
            if not callable(method):
                raise Exception("Method not found")
            return method(request)
        except Exception as err:
            print('Error route:', err)
            return Response(404, {"error": "Route not found"})

    def __verify_class_exists(self, name_class):
        return os.path.exists(self.DIR_NAME + "/../" + self.PATH_CONTROLLERS + "/" + name_class + '.py')

    def __get_class_method(self, request):
        # first param to class and second to method
        split_route = []
        for path in request.path.split('/'):
            if path and len(split_route) <= 1:
                split_route.append(path)

        str_class = split_route[0].title()

        if len(split_route) <= 1:
            split_route.append("")

        return {'class': str_class, 'method': split_route[1]}
