from core.types import VehiclePriority
from core.types import VehicleStatus





class Vehicle:
    def __init__(self ,
                 des_gateway_id : int ,
                 id: int = -1,
                 priority : VehiclePriority = VehiclePriority.NORMAL ,
                 status : VehicleStatus = VehicleStatus.WAITING,
                 ):
        self._id = id
        self._current_lane_id : int | None = None 
        self._lane_pos = 0.0
        self._priority = priority
        self._status= status
        self._des_gateway = des_gateway_id
        
    
    # setter 
    def set_lane_pos(self,lane_pos)->None:
        if lane_pos < 0 or lane_pos > 1:
            raise ValueError("invalid lane position")
        self._lane_pos = lane_pos
    
    def set_state(self, status : VehicleStatus)-> None:
        self._status = status
    
    def set_priority(self , priority : VehiclePriority)->None:
        self._priority = priority

    
    # getter
    def get_lane_pos(self)-> float:
        return self._lane_pos
    
    def get_status(self)-> VehicleStatus:
        return self._status
    
    def get_priority(self)-> VehiclePriority:
        return self._priority
    



# todo
# rais ..