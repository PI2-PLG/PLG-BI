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
