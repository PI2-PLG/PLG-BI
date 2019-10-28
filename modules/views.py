from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from modules.models import Module, ModuleData
from modules.serializers import ModuleDataSerializer
import io


class NewModule(APIView):

    '''
    Cria um novo modulo
    '''
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


class GetAllModuleList(APIView):

    '''
    Retorna uma lista com todos os módulos cadastrados
    '''
    def get(self, request):
        try:
            modules = Module.objects.all()
            module_list = {}
            index = 0
            for module in modules:
                module_list['module-'+str(index)] = {
                                                     'name':module.name,
                                                     'latitude':module.module_data.last().latitude,
                                                     'longitude':module.module_data.last().longitude
                                                     }
                index += 1
            print(module_list)
            return Response(module_list, status=status.HTTP_200_OK)
        except:
            return Response({'response': 'something_are_wrong'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


class GetAllData(APIView):

    '''
    Retorna todos os módulos e seus dados
    '''
    def get(self, request):
        try:
            modules = Module.objects.all()
            data_list = {}
            for module in modules:
                query_list = module.module_data.all()
                data_index = 1
                aux_dict_2 = {}
                for query in query_list:
                    aux_dict = {}
                    aux_dict['date'] = query.date
                    aux_dict['latitude'] = query.latitude
                    aux_dict['longitude'] = query.longitude
                    aux_dict['temperature'] = query.temperature
                    aux_dict['humidity'] = query.humidity
                    aux_dict['pressure'] = query.pressure
                    aux_dict['ppm'] = query.ppm
                    aux_dict_2['data-set-'+str(data_index)] = aux_dict
                    data_index += 1
                    data_list[module.name] = aux_dict_2
            return Response(data_list, status=status.HTTP_200_OK)
        except:
            return Response({'response': 'something_are_wrong'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)