#!/usr/bin/env python3

class Book:
    
    def __init__(self, title):
        self.title = title

    
    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        self._page_count = page_count
    

    page_count = property(get_page_count, set_page_count)

