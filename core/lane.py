from core.types import Point


class Lane:
    def __init__(self ,
                 start_point : Point,
                 end_point : Point,
                 direction : int 
                 ):
        self._start_point = start_point
        self._end_point = end_point
        self._vehicle_list : list
    
