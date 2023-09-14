import functions
import os
from pprint import pprint

#   TODO:
#       explain functions.py, main.py
#       create functionality to get all posts, comments without userId
#       implement PyTest
#       create a function that send request every 90seconds
#       
#       optional create gui using PySimpleGui 
#       

#   global variables
url = "https://jsonplaceholder.typicode.com/"
params = {}

# If this file is called in terminal
if __name__ == "__main__":
    
    # Python terminal meniu,  
    while True:
        os.system("clear")

        # Main menu you select two menus from here:
        #   1-destination meniu: designed to manipulate the url and params 
        #   2-get data meniu: you can choose either print, or write to json file the data

        main_text = """
        current url: {}
        params: {}

        Welcome to jsonplaceholder API browser v0.01
              1 - destination 
              2 - get data
              0 - exit
        """.format(url, params)

        func_select = functions.get_input("What do you want to select? ", main_text, seconds=3)

        #   Destination meniu
        if func_select == 1:
            os.system("clear")

            #   Users will print all users avaivable in API.
            #   Posts will ask for userId and print all the posts that user has written.
            #   Comments will ask for userId, postId and print all the comments that user have writen on particular post.
            text1 = """
            current url: {}
            params: {}

            You selected destination:
                1 - users 
                2 - posts: need to set userId
                3 - comments: need to set postId and userId
                0 - go back
            """.format(url, params)

            input_select = functions.get_input("What do you want to select? ", text1)

            if input_select == 1:
                data_select = "users"
                url = f"https://jsonplaceholder.typicode.com/{data_select}"
            
            elif input_select == 2:
                data_select = "posts"
                url = f"https://jsonplaceholder.typicode.com/{data_select}"
                userId = functions.get_input("Enter userId: ")
                params["userId"] = userId

            elif input_select == 3:
                data_select = "comments"
                url = f"https://jsonplaceholder.typicode.com/{data_select}"
                userId = functions.get_input("Enter userId: ")
                params["userId"] = userId
                postId = functions.get_input("Enter postId: ")
                params["postId"]= postId

            elif input_select == 0:
                continue
        
        #   Data meniu
        elif func_select == 2:
            data = functions.get_json(url, params)
            
            url = "https://jsonplaceholder.typicode.com/"
            params = {}
            choise = functions.get_input("save to a file or print (1-yes/ any number key -print) ?: ")

            if choise == 1:
                functions.write_to_json(data_select, data)
                continue
            else:
                pprint(data)
                
                input("Press any key to continue")
                continue

        elif func_select == 0:
            os.system("clear")
            print("Have a wonderful day!")
            break

        else:
            print("Invalid input!")

