from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

import logging
logger = logging.getLogger(__name__)

class HelloView(APIView):
    logger.debug("In hello view")
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)