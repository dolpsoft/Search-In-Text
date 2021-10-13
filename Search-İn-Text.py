import os
import sys
from colorama import Back, init, Fore, Style


init(autoreset=True)
class Search:
    def __init__(self):
        self.text= input ("Enter the text:  ")
        self.search= input ("\nEnter the phrase you want to search: ")
     
    def text_operations (self):
     
        if  self.search in self.text :     
            print ("\nExpressions found:")
            print ("-"*50)
            self.text=self.text.replace(self.search,f"{Fore.GREEN}{self.search}{Style.RESET_ALL}")
            print(self.text)
            print ("-"*50)
      
        else:                 
           print ("-"*50)
           print("The phrase you are looking for was not found in the text you entered.  Please try again or enter another word.")
           print ("-"*50)
           
        object.exit_selection()
             
             
    def exit_selection (self):
          exit= input("Do you want to enter a new text? (Y/N): ")
          
          if exit== "Y" or exit== "y":
              os.system("cls" if os.name == "nt" else "clear")
              return
              
          else:
              print ("\n\nYou left from app.")
              sys.exit()
          
             
     
while True:
    object= Search()           
    object.text_operations()
    