# from currency.models import RequstResponseLog
from time import time
from currency.models import RequstResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        RequstResponseLog.objects.create(
            path=request.path,
            time=time() - start
        )
        return response
