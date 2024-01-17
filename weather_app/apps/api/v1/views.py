from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@swagger_auto_schema(
        method="GET",
        operation_id="v1/",
        operation_description="A default path for allowing django to serve API's V1 url to frontend.",
    )
@api_view(["GET"])
def v1(request):
    return Response({'success': True}, status=status.HTTP_200_OK)