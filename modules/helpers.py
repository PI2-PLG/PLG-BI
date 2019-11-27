from modules.models import Module, ModuleData
from .enum import ModuleStatusSet
import io

def setModuleStatus(module_name):

    try:
        module = Module.objects.get(name=module_name)
    except:
        return 'UNKNOWN'

    status = isOffline(module)
    status = isInMotion(module)

def isOffline(module):
    try:
        if(module.module_data.last().latitude == 0.0 and module.module_data.last().longitude == 0.0):
            status = 'OFFLINE'
            '''
                Como os valores de longitude e latitude foram iguais a 0
                o sistema busca o ultimo valor de longitude e latitude como
                localização atual do módulo
            '''
            last_data_id = module.module_data.last().id
            last_data = ModuleData.objects.get(id=last_data_id)
            all_data = module.module_data.all()
            for data in all_data:
                if(data.longitude != 0 and data.latitude != 0):
                    last_data.latitude = data.latitude
                    last_data.longitude = data.longitude
            last_data.save()
            setStatus(module, status)
        else:
            status = 'ONLINE'
            setStatus(module, status)
    except:
        status = 'UNKNOWN'
        setStatus(module, status)

def isInMotion(module):
    try:
        if(module.module_data.last().velocity > 1.0):
            status =  'IN_MOTION'
            setStatus(module, status)
        elif(module.status == 'OFFLINE'):
            status =  'OFFLINE'
            setStatus(module, status)
        else:
            status = 'ONLINE'
            setStatus(module, status)
    except:
        status = 'UNKNOWN'
        setStatus(module, status)

def setStatus(module, status):
    module.status = status
    module.save()
