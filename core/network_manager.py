from core.vehicle import Vehicle
from core.road import Road
from core.gateway import Gateway
from core.intersection import Intersection
from core.lane import Lane


class NetworkManager:
    def __init__(self):
        self._intersections: dict[int, Intersection] = {}
        self._roads: dict[int, Road] = {}  
        self._lanes: dict[int, Lane] = {}  
        self._gateways: dict[int, Gateway] = {}
        self._vehicles: dict[int, Vehicle] = {}
        