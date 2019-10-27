from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from modules.models import Module, ModuleData
from modules.serializers import ModuleDataSerializer
import io


class NewModule(APIView):

    def post(self, request):
        try:
            module = request.data["module"]
            module_name = module["name"]
            new_module = Module(name=module_name)
            new_module.save()
            return Response({'response': 'module_successfully_created'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'response': 'module_unseccessfully_created'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

class NewModuleData(APIView):

    def post(self, request):
        try:
            module = request.data["module"]
            module_data = request.data["module_data"]

            module_name = module["name"]
            module = Module.objects.get(name=module_name)

            '''
            A data é coletada automaticamente ao criar um novo conjunto de dados
            '''
            data = ModuleData.objects.create(
                    latitude = module_data["latitude"],
                    longitude = module_data["longitude"],
                    temperature = module_data["temperature"],
                    humidity = module_data["humidity"],
                    pressure = module_data["pressure"],
                    ppm = module_data["ppm"],
                    module=module)
            module.module_data.add(data)
            return Response({'response': 'module-data_successfully_created'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'response': 'module-data_unseccessfully_created'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

class GetAllModuleData(APIView):

    def post(self, request):
        try:
            module = request.data["module"]
            module_name = module["name"]
            module = Module.objects.get(name=module_name)
            module_data = module.module_data.all()

            all_data = {}
            data_index = 0
            for data in module_data:
                module_data = ModuleDataSerializer(data)
                data_dict = {
                            'date':module_data.data['date'],
                            'latitude':module_data.data['latitude'],
                            'longitude':module_data.data['longitude'],
                            'temperature':module_data.data['temperature'],
                            'humidity':module_data.data['humidity'],
                            'pressure':module_data.data['pressure'],
                            'ppm':module_data.data['ppm'],
                            }
                data_name = 'data-set-'+str(data_index)
                all_data[data_name] = data_dict
                data_index += 1

            return Response(all_data, status=status.HTTP_201_CREATED)
        except:
            return Response({'response': 'module_data_not_found'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)