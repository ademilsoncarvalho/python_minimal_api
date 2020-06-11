from server.Response import Response


class User:

    def _get(self, request):
        user1 = {"name": "Ademilson"}
        user2 = {"name": "Pedro"}
        list = [user1, user2]
        response = Response(200, list)
        return response

    def _post(self, request):
        response = Response(200, request.params)
        return response

    def _put(self, request):
        response = Response(200, request.params)
        return response

    def _delete(self, request):
        response = Response(200, request.params)
        return response
