# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Crocodile3'
__mtime__ = '2020/2/21'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
from notebook import Notebook,Note

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choice = {
            "1":self.show_notes,
            "2":self.search_notes,
            "3":self.modify_note,
            "4":self.quit,
        }
        
    def display_menu(self):
        print("""
        Notebook Menu
        
        1. show all Notes
        2.Search Notes
        3.Add Note
        4.Modify Note
        5.Quit
        """)
        
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option:")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
                
    def show_notes(self,notes=None):
        if not notes:
            notes = self.notebook.notes
            
        for note in notes:
            print("{0}:{1}\n{2}".format(note.id,note.tags,note.memo))
            
    def search_notes(self):
        filter = input("Search for :")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
        
    def add_note(self):
        id = input("Enter a note id:")
        memo = input("Enter a memo:")
        tags = input("Enter tags:")
        if memo:
            self.notebook.modify_memo(id,memo)
        if tags:
            self.notebook.modify_tags(id,tags)
            
    def modify_note(self):
        id = input("Enter a note id:")
        memo = input("Enter a memo:")
        tags = input("Enter tags:")
        if memo:
            self.notebook.modify_memo(id,memo)
        if tags:
            self.notebook.modify_tags(id,memo)
            
    def quit(self):
        print("Thank you for using your notebook today")
        sys.exit(0)
        
        
if __name__ == '__main__':
    Menu().run()
