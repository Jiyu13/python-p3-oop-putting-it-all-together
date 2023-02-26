#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count=0):
        self.title = title
        self.page_count = page_count     # set it to 0 by default


    def get_author(self):
        return self.author

    def set_author(self, author_name):
        self.author = author_name


    def get_page_count(self):
        return self._page_count

    
    def set_page_count(self, pages):
        if type(pages) == int:
            self._page_count = pages
        else:
            print("page_count must be an integer")

    
    page_count = property(get_page_count, set_page_count)


    def get_genre(self):
        return self.genre
    

    def set_genre(self, genre):
        self.genre = genre


    # define instance method
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")