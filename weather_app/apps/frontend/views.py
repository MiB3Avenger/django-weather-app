import json

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@swagger_auto_schema(
        method="GET",
        operation_id="v1/frontend/",
        operation_description="A default path for allowing django to serve API's V1 url to frontend.",
    )
@api_view(["GET"])
def frontend(request):
    return Response({'success': True}, status=status.HTTP_200_OK)