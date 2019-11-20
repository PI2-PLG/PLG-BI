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
    return status

def isOffline(module):
    try:
        if(module.module_data.last().latitude == 0.0 and module.module_data.last().longitude == 0.0):
            print("aqui")
            return 'OFFLINE'
        else:
            return 'ONLINE'
    except:
        return 'UNKNOWN'

def isInMotion(module):
    try:
        if(module.module_data.last().velocity > 1.0):
            return 'IN_MOTION'
        else:
            print("aqui!")
            print(module.status)
            return module.status
    except:
        return 'UNKNOWN'