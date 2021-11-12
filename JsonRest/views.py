
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from rest_framework.parsers import JSONParser

from JsonRest.models import JsonData
from JsonRest.serializers import JsonDataSerializer

# Create your views here.
class SavedJson(APIView):
    
    parser_classes = [JSONParser]

    
    
    def post(self,request):
        
        return Response({"success":request.data})
    
    
    def get(self,request):
        return Response({"success":"get Method"})
    
  