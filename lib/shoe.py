#!/usr/bin/env python3

class Shoe:
    
    
    def __init__(self, brand):
        self.brand = brand
        self._color = None  # set default value for when get_size() is called, if not error
        self._size = None


    def get_color(self):
        return self._color


    def set_color(self, color):
        self._color = color

    
    def get_size(self):
        return self._size
    
    def set_size(self, shoe_size):
        if type(shoe_size) != int:
            print("size must be an integer")
        else:
            self._size = shoe_size   
        

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"


    color = property(get_color, set_color)
    size = property(get_size, set_size)
    