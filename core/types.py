from dataclasses import dataclass
from enum import Enum
from math import sqrt

# Enums
class VehicleStatus(Enum):
    MOVING = 1
    WAITING = 2
    
class VehiclePriority(Enum):
    NORMAL = 1
    EMERGENCY = 2
    
class NodeType(Enum):
    INTERSECTION = 1
    GATEWAY = 2
    
class SpawnDistribution(Enum):
    UNIFORM = 1,
    POISSON = 2,
    BURST = 3
    
#type
@dataclass(frozen=True)
class Point:
    x: float
    y: float
    
    def __add__(self, other : 'Point') -> 'Point':
        return Point(self.x + other.x , self.y + other.y)
    
    def __sub__(self ,other : 'Point') -> 'Point':
        return Point(self.x - other.x , self.y - other.y)
    
    def __mul__(self , scaler: float) -> 'Point' :
        return Point(self.x * scaler , self.y * scaler)
    
    
    def distance_to(self, other : 'Point') -> float:
        return  sqrt( (self.x - other.x)** 2 + (self.y - other.y)**2 )
        
    def to_tuple(self) -> tuple:
        return self.x , self.y



