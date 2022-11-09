from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from XtenEngine.common_util import ResponseMessage
from BillingService.meter import MeterService


class Meter(APIView):
    @staticmethod
    def get(request):
        response_return = ResponseMessage()
        try:
            response_return = MeterService(request=request, token=request.META['HTTP_AUTHORIZATION']).getDataMeter()
            return Response(response_return)
        except Exception:
            response_return.set_error_status('Exception Occurred')
            return Response(response_return)