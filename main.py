import functions
import os
from pprint import pprint

#   TODO:
#       explain functions.py, main.py
#       create functionality to get all posts, comments without userId - Done
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
        Currently selected:
            Url: {}
            Params: {}

        Welcome to jsonplaceholder API browser v0.02
              1 - destination
              2 - set params 
              3 - get data

              0 - exit
        """.format(url, params)

        func_select = functions.get_input("What do you want to select? ", main_text, seconds=3)

        #   Destination meniu
        if func_select == 1:
            os.system("clear")

            #   Users will print all users avaivable in API.
            #   Posts will ask for userId and print all the posts that user has written.
            #   Comments will ask for userId, postId and print all the comments that user have writen on particular post.
            set_destination_text = """
            Currently selected:
                Url: {}
                Params: {}

            Select destination:
                1 - users
                2 - posts   : params that can be set: userId
                3 - comments: params that can be set: postId and userId
                4 - albums
                5 - photos  : params that can be set: albumId
                6 - todos   : params that can be set: userId

                0 - go back
            """.format(url, params)

            input_select = functions.get_input("What do you want to select? ", set_destination_text)
            
            if input_select == 1:
                data_select = "users"
            
            elif input_select == 2:
                data_select = "posts"

            elif input_select == 3:
                data_select = "comments"
            
            elif input_select == 4:
                data_select = "albums"

            elif input_select == 5:
                data_select = "photos"

            elif input_select == 6:
                data_select = "todos"
            
            if data_select:
                url = f"https://jsonplaceholder.typicode.com/{data_select}"

            elif input_select == 0:
                continue
        
        elif func_select == 2:
            os.system("clear")

            set_params_text = """
            Currently selected:
                Url: {}
                Params: {}

            Select param to set:
                1 - set userId 
                2 - set postId
                3 - set albumId
                4 - clear params
                
                0 - go back
            """.format(url, params)
            
            input_select = functions.get_input("What do you want to select? ", set_params_text)

            if input_select == 1:
                userId = functions.get_input("Enter userId: ")
                params["userId"] = userId
            
            elif input_select == 2:
                postId = functions.get_input("Enter postId: ")
                params["postId"]= postId
            
            elif input_select == 3:
                albumId = functions.get_input("Enter albumId: ")
                params["albumId"]= albumId
                
            elif input_select == 4:
                params = {}
            
            elif input_select == 0:
                continue

        
        #   Data meniu
        elif func_select == 3:
            #   Error handle if no data provided
            try:
                data = functions.get_json(url, params)
            except Exception as e:
                print("\033[0;31;40m Error: ", e, "\033[0;0m")
                functions.time_sleep(3)
                continue
            
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

