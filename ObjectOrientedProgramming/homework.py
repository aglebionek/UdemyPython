#%%
class Line():
    def __init__(self, coordinates1: tuple, coordinates2: tuple) -> None:
        '''
        A line class, takes two points in form of tuples as parimeters.
        '''
        self.coordinates1 = coordinates1
        self.coordinates2 = coordinates2

    def distance(self) -> float:
        '''
        Returns the length of the line.
        '''
        return ((self.coordinates2[0]-self.coordinates1[0])**2 + (self.coordinates2[1]-self.coordinates1[1])**2)**0.5

    def slope(self) -> float:
        '''
        Returns the slope of the line.
        '''
        return (self.coordinates2[1] - self.coordinates1[1]) / (self.coordinates2[0] - self.coordinates1[0])

l = Line((3,2), (8, 10))
print(l.distance())
print(l.slope())


#%%
class Cylinder():
    from math import pi
    def __init__(self, height: float=1, radius: float=1) -> None:
        '''
        A cylinder class, takes height and radius as parameters with 1 as their default values.
        '''
        self.height = height
        self.radius = radius

    def volume(self) -> float:
        '''
        Returns the volume of the cylinder.
        '''
        return Cylinder.pi*(self.radius**2)*self.height

    def surface_area(self) -> float:
        '''
        Returns the surface area of the cylinder.
        '''
        return 2*Cylinder.pi*self.radius*self.height + 2*Cylinder.pi*(self.radius**2)

c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
# %%
