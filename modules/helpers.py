from modules.models import Module, ModuleData
from .enum import ModuleStatusSet
import io

def setModuleStatus(module_name):

    try:
        module = Module.objects.get(name=module_name)
    except:
        return 'UNKNOWN'

    status = isInMotion(module)
    status = isOffline(module)
    return status

def isInMotion(module):
    try:
        if(module.module_data.last().velocity > 1.0):
            return 'IN_MOTION'
        else:
            return 'ONLINE'
    except:
        return 'UNKNOWN'

def isOffline(module):
    try:
        if(module.module_data.last().latitude == 0.0 and module.module_data.last().longitude == 0.0):
            return 'OFFLINE'
        else:
            return 'ONLINE'
    except:
        return 'UNKNOWN'