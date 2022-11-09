from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from Apps.Authen.authen import AuthenticateService
from XtenEngine.common_util import ResponseMessage
from django.http import HttpResponse
from django.template import Context, loader
from rest_framework.renderers import TemplateHTMLRenderer


class Authenticate(APIView):
    @staticmethod
    def post(request):
        if not request.data:
            return Response({'Error': "Please provide email/password"}, status="400")
        response_return = ResponseMessage()
        request_data = dict()
        request_data['email'] = request.data.get('email', '')
        request_data['password'] = request.data.get('password', '')
        request_data['username'] = request.data.get('username', '')
        try:
            response_return = AuthenticateService(request=request).login(request_data)
            return Response(response_return)
        except Exception:
            response_return.set_error_status('Exception Occurred')
            return Response(response_return)


class Register(APIView):
    @staticmethod
    def post(request):
        if not request.data:
            return Response({'Error': "Please provide email/password"}, status="400")
        response_return = ResponseMessage()
        request_data = dict()
        request_data['email'] = request.data.get('email', '')
        request_data['password'] = request.data.get('password', '')
        request_data['first_name'] = request.data.get('first_name', '')
        request_data['last_name'] = request.data.get('last_name', '')
        try:
            response_return = AuthenticateService(request=request).register(request_data)
            return Response(response_return)
        except Exception:
            response_return.set_error_status('Exception Occurred')
            return Response(response_return)


class CanRegister(APIView):
    @staticmethod
    def get(request):
        response_return = ResponseMessage()
        request_data = dict()
        request_data['userid'] = request.GET.get('userid', '')
        try:
            response_return = AuthenticateService(request=request).canRegister(request_data)
            return Response(response_return)
        except Exception:
            response_return.set_error_status('Exception Occurred')
            return Response(response_return)


class VerifyToken(APIView):
    @staticmethod
    def post(request):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        response_return = ResponseMessage()
        request_data = dict()
        request_data['token'] = request.data.get('token')
        try:
            response_return = AuthenticateService(request=request).verifyToken(request_data)
            return Response(response_return)
        except Exception:
            response_return.set_error_status('Exception Occurred')
            return Response(response_return)