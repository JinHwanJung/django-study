from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        print('request._request.GET', request._request.GET)
        print('request.GET', request.GET)
        print('request.query_params', request.query_params)
        return Response('DRF GET OK')

    def post(self, request, *args, **kwargs):
        print('request._request.POST', request._request.POST)
        print('request.POST', request.POST)
        print('request.data', request.data)
        return Response('DRF POST OK')
