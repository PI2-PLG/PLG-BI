from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from modules.models import Module, ModuleData
import io


class NewModule(APIView):

    def post(self, request):
        print(request.data["module"])
        try:
            module = request.data["module"]
            module_name = module["name"]
            new_module = Module(name=module_name)
            new_module.save()
            return Response({'response': 'module_successfully_created'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'response': 'module_unseccessfully_created'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


