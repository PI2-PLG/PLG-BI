from enum import Enum

class ModuleStatusSet(Enum):
    ONLINE = 'ONLINE'
    OFFLINE = 'OFFLINE'
    UNKNOWN = 'UNKNOWN'
    FIRERISK = 'FIRERISK'
    IN_MOTION = 'IN_MOTION'