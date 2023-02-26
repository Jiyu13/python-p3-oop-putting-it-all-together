#!/usr/bin/env python3

class Shoe:
    
    
    def __init__(self, brand):
        self.brand = brand
        self.size = 0   # set to 0 by default, or AttributeError: 'Shoe' object has no attribute '_size'

    

    def set_color(self, color):
        self.color = color


    def get_size(self):
        return self._size

    
    def set_size(self, size_val):
        if type(size_val) == int:
            self._size = size_val
        else:
            print("size must be an integer")

    size = property(get_size, set_size)


    def set_material(self, material):
        self.material = material
    

    def set_condition(self, condition):
        self.condition = condition


    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

