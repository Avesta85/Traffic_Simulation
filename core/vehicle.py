from enum import Enum
from lane import Lane
from gateway import GateWay

class VehicleStatus(Enum):
    MOVING = 1
    STOPPED = 2
    
class VehiclePriority(Enum):
    NORMAL = 1
    EMERGENCY = 2



class Vehicle:
    def __init__(self ,
                 des_gateway : GateWay ,
                 id: int = -1,
                 priority : VehiclePriority = VehiclePriority.NORMAL ,
                 status : VehicleStatus = VehicleStatus.INACTIVE,
                 ):
        self.__id = id
        self.__current_lane : Lane
        self.__lane_pos = 0.0
        self.__priority = priority
        self.__status= status
        self.__des_gateway = des_gateway
        
    
    # setter 
    def set_lane_pos(self,lane_pos)->None:
        if lane_pos < 0 or lane_pos > 1:
            raise ValueError("invalid lane position")
        self.__lane_pos = lane_pos
    
    def set_state(self, status : VehicleStatus)-> None:
        self.__status = status
    
    def set_priority(self , priority : VehiclePriority)->None:
        self.__priority = priority

    
    # getter
    def get_lane_pos(self)-> float:
        return self.__lane_pos
    
    def get_status(self)-> VehicleStatus:
        return self.__status
    
    def get_priority(self)-> VehiclePriority:
        return self.__priority
    



# todo
# rais ..