#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count=None):
        self.title = title
        self._page_count = page_count   # set default value for when get_page_count() is called, if not error

    
    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, count):
        if type(count) != int:
            print("page_count must be an integer")
        else:
            self._page_count = count   # count is a param we pass in
    

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    # page_count here is a property
    page_count = property(get_page_count, set_page_count)

