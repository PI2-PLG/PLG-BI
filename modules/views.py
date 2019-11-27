from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from modules.models import Module, ModuleData
from modules.serializers import ModuleDataSerializer
from decimal import Decimal
from rest_framework.permissions import AllowAny
from .enum import ModuleStatusSet
from .helpers import setModuleStatus
import io


class NewModule(APIView):

    permission_classes = (AllowAny,)

    '''
    Cria um novo modulo
    '''
    def post(self, request):

        try:
            module = request.data["module"]
            module_name = module["name"]
            new_module, created = Module.objects.get_or_create(name=module_name)
            if(created):
                print("[LOG] - New module created: " + module_name)
            else:
                print("[LOG] - "+ module_name + " was found")

            return Response({'response': 'module_successfully_created'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'response': 'module_unseccessfully_created'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

class ModuleStatus(APIView):
    permission_classes = (AllowAny,)

    '''
    Retorna o status de um módulo
    '''
    def get(self, request):
        try:
            module = request.data["module"]
            module_name = module["name"]
            query_module = Module.objects.get(name=module_name)
        except:
            return Response({'response': 'module_data_not_found'}, status=status.HTTP_200_OK)

        response = {}
        response["module"] = {
                              "name": query_module.name,
                              "status": query_module.status,
                             }
        return Response(response, status=status.HTTP_200_OK)

    '''
    Define o status de um módulo
    '''
    def post(self, request):
        try:
            module = request.data["module"]
            module_name = module["name"]
            query_module = Module.objects.get(name=module_name)
        except:
            return Response({'response': 'module_data_not_found'}, status=status.HTTP_200_OK)

        try:
            new_status = module["status"]
            query_module.status = ModuleStatusSet(new_status).value
            query_module.save()
            return Response({'response': 'status_saved'})
        except:
            return Response({'response': 'status_not_saved'}, status=status.HTTP_200_OK)

class NewModuleData(APIView):

    permission_classes = (AllowAny,)

    '''
    Cria um conjunto de dados de um determinado módulo
    '''
    def post(self, request):
        try:
            module = request.data["module"]
            module_data = request.data["module_data"]
            module_name = module["name"]
            module = Module.objects.get(name=module_name)

            '''
            A data é coletada automaticamente ao criar um novo conjunto de dados
            '''
            print(f"[LOG] Saving data in {module_name}")
            print("=======================VALUES=======================")
            print(f"latitude: {module_data['latitude']}")
            print(f"longitude: {module_data['longitude']}")
            print(f"temperature: {module_data['temperature']}")
            print(f"humidity: {module_data['humidity']}")
            print(f"velocity: {module_data['velocity']}")
            print(f"ppm: {module_data['ppm']}")
            print(f"signal_strength: {module_data['signal_strength']}")
            print("===================================================")
            data = ModuleData.objects.create(
                    latitude = Decimal(module_data["latitude"]),
                    longitude = Decimal(module_data["longitude"]),
                    temperature = Decimal(module_data["temperature"]),
                    humidity = Decimal(module_data["humidity"]),
                    velocity = Decimal(module_data["velocity"]),
                    ppm = module_data["ppm"],
                    signal_strength=module_data["signal_strength"],
                    module=module)
            module.module_data.add(data)

            '''
            Salvando status
            '''
            setModuleStatus(module.name)

            print("[LOG] - New data saved in " + module_name)
            return Response({'response': 'module-data_successfully_created'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'response': 'module-data_unseccessfully_created'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


class GetAllModuleData(APIView):

    permission_classes = (AllowAny,)

    '''
    Retorna todos os conjuntos de dados de um determinado módulo
    '''
    def get(self, request):
        try:
            module = request.data["module"]
            module_name = module["name"]
            module = Module.objects.get(name=module_name)
            module_data = module.module_data.all()
            all_data = {}
            dates = []
            latitudes = []
            longitudes = []
            temperatures = []
            humidities = []
            velocity_group = []
            signal_group = []
            ppms = []
            for data in module_data:
                module_data = ModuleDataSerializer(data)
                dates.append(module_data.data['date'])
                latitudes.append(module_data.data['latitude'])
                longitudes.append(module_data.data['longitude'])
                temperatures.append(module_data.data['temperature'])
                humidities.append(module_data.data['humidity'])
                velocity_group.append(module_data.data['velocity'])
                ppms.append(module_data.data['ppm'])
                signal_group.append(module_data.data['signal_strength'])

            all_data = {'name': module.name,
                        'status':module.status,
                        'date':dates,
                        'latitude':latitudes,
                        'longitude':longitudes,
                        'temperature':temperatures,
                        'humidity':humidities,
                        'velocity':velocity_group,
                        'ppm':ppms,
                        'signal_strength':signal_group,
                        }
            return Response(all_data, status=status.HTTP_200_OK)
        except:
            return Response({'response': 'module_data_not_found'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


class GetAllModuleList(APIView):

    permission_classes = (AllowAny,)

    '''
    Retorna uma lista com todos os módulos cadastrados
    '''
    def get(self, request):
        try:
            modules = Module.objects.all()
            module_list = {}
            index = 0
            for module in modules:
                print(module.module_data)
                if(module.module_data.last() != None and module.module_data.last() != None):
                    module_list['module-'+str(index)] = {
                                                         'name':module.name,
                                                         'status':module.status,
                                                         'latitude':module.module_data.last().latitude,
                                                         'longitude':module.module_data.last().longitude
                                                         }
                else:
                    module_list['module-'+str(index)] = {
                                                         'name':module.name,
                                                         'status':module.status,
                                                         'latitude':0.00,
                                                         'longitude':0.00
                                                         }
                index += 1
            return Response(module_list, status=status.HTTP_200_OK)
        except:
            return Response({'response': 'something_are_wrong'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


class GetAllData(APIView):

    permission_classes = (AllowAny,)

    '''
    Retorna todos os módulos e seus dados
    '''
    def get(self, request):
        try:
            modules = Module.objects.all()
            data_list = []
            for module in modules:
                query_list = module.module_data.all()
                data_set = {}
                dates = []
                latitudes = []
                longitudes = []
                temperatures = []
                humidities = []
                velocity_group = []
                ppms = []
                signal_group = []
                for query in query_list:
                    dates.append(query.date)
                    latitudes.append(query.latitude)
                    longitudes.append(query.longitude)
                    temperatures.append(query.temperature)
                    humidities.append(query.humidity)
                    velocity_group.append(query.velocity)
                    ppms.append(query.ppm)
                data_list.append({
                                          "name":module.name,
                                          "status":module.status,
                                          "date":dates,
                                          "latitude":latitudes,
                                          "longitude":longitudes,
                                          "temperature":temperatures,
                                          "humidity":humidities,
                                          "velocity":velocity_group,
                                          "ppm":ppms,
                                          "signal_strength":signal_group,
                                         })
            return Response(data_list, status=status.HTTP_200_OK)
        except:
            return Response({'response': 'something_are_wrong'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)