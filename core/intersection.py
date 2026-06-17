from core.types import Point



class Intersection:
    def __init__(self,
                 id : int ,
                 position : Point):
        self._id = id 
        self._position = position
        self._incoming_lane_ids = []
        self._outgoing_lane_ids = []
        

    @property
    def position(self) -> Point:
        return self._position
    
    @position.setter
    def position(self, new_position : Point):
        self._position = new_position
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def incoming_lane_ids(self) -> list[int]:
        return self._incoming_lane_ids.copy()
    
    @property
    def outgoing_lane_ids(self) -> list[int]:
        return self._outgoing_lane_ids.copy()
    
    def add_incoming_lane(self, lane_id : int):
        if lane_id not in self._incoming_lane_ids:
            self._incoming_lane_ids.append(lane_id)
        else:
            raise ValueError(f"lane_id : {lane_id} already added to intersection : {self._id}")
        
    def add_outgoing_lane(self, lane_id : int):
        if lane_id not in self._outgoing_lane_ids:
            self._outgoing_lane_ids.append(lane_id)
        else:
            raise ValueError(f"lane_id : {lane_id} already added to intersection : {self._id}")
        
    def remove_incoming_lane(self, lane_id : int):
        try:
            self._incoming_lane_ids.remove(lane_id)
        except ValueError:
            raise ValueError(f"intersection : {self._id} doesnt have incoming lane with this id : {lane_id}")
    def remove_outgoing_lane(self , lane_id : int):
        try:
            self._outgoing_lane_ids.remove(lane_id)
        except ValueError:
            raise ValueError(f"intersection : {self._id} doesnt have outgoing lane with this id : {lane_id}")
        
    