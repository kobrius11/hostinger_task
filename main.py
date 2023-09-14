from pprint import pprint
import functions
import threading
import os


#   TODO:
#       explain functions.py, main.py - Done
#       create functionality to get all posts, comments without userId - Done
#       implement PyTest
#       implement logger
#       create a function that send request every 90seconds - Done
#       
#       optional create gui using PySimpleGui 
#       

#   global variables
url = "https://jsonplaceholder.typicode.com/"
params = {}

def main(url: str, params: dict, threads: bool = False):
    const_url = "https://jsonplaceholder.typicode.com/"
    while True:
        running_threads = {thread.name for thread in threading.enumerate()}
        stop_threads = False
        os.system("clear")

        # Main menu you select two menus from here:
        #   1-destination meniu: designed to manipulate the url and params 
        #   2-set url parameters
        #   3-get data meniu: you can choose either print, or write to json file the data
        main_text = """
        Currently selected:
            Url: {}
            Params: {}
            Run threading: {}
            Running threads: {}

        Welcome to jsonplaceholder API browser v0.03
              1 - set destination
              2 - set params
              3 - get data
              4 - get all data

              5 - set threading
              0 - exit
        """.format(url, params, threads, running_threads)

        func_select = functions.get_input("What do you want to select? ", main_text, seconds=3)

        #   Destination meniu
        if func_select == 1:
            os.system("clear")

            set_destination_text = """
            Currently selected:
                Url: {}
                Params: {}
                Run threading: {}
                Running threads: {}

            Select destination:
                1 - users
                2 - posts   : params that can be set: userId
                3 - comments: params that can be set: postId and userId
                4 - albums
                5 - photos  : params that can be set: albumId
                6 - todos   : params that can be set: userId

                0 - go back
            """.format(url, params, threads, running_threads)

            input_select = functions.get_input("What do you want to select? ", set_destination_text)
            #   Set users
            if input_select == 1:
                data_select = "users"
            
            #   Set posts
            elif input_select == 2:
                data_select = "posts"

            #   Set comments
            elif input_select == 3:
                data_select = "comments"
            
            #   Set albums
            elif input_select == 4:
                data_select = "albums"

            #   Set photos
            elif input_select == 5:
                data_select = "photos"

            #   Set todos
            elif input_select == 6:
                data_select = "todos"
            
            #   If data_select was selected(exist), set url approatly
            if data_select:
                url = f"https://jsonplaceholder.typicode.com/{data_select}"

            #   Go back to main menu
            elif input_select == 0:
                continue
        
        #   Set params menu
        elif func_select == 2:
            os.system("clear")

            set_params_text = """
            Currently selected:
                Url: {}
                Params: {}
                Run threading: {}
                Running threads: {}


            Select param to set:
                1 - set userId 
                2 - set postId
                3 - set albumId
                4 - clear params
                
                0 - go back
            """.format(url, params, threads, running_threads)
            
            input_select = functions.get_input("What do you want to select? ", set_params_text)

            #   set userId
            if input_select == 1:
                userId = functions.get_input("Enter userId: ")
                params["userId"] = userId
            
            #   Set postId
            elif input_select == 2:
                postId = functions.get_input("Enter postId: ")
                params["postId"]= postId
            
            #   Set albumId
            elif input_select == 3:
                albumId = functions.get_input("Enter albumId: ")
                params["albumId"]= albumId
            
            #   Clear
            elif input_select == 4:
                params = {}
            
            #   Exit
            elif input_select == 0:
                continue

        
        #   Get data meniu
        elif func_select == 3:
            #   Error handle if no data provided
            try:
                data = functions.get_json(url, params)
            except Exception as e:
                print("\033[0;31;40m Error: ", e, "\033[0;0m")
                functions.time_sleep(3)
                continue
            get_data_text ="""
            Currently selected:
                Url: {}
                Params: {}
                Run threading: {}
                Running threads: {}

            Select data to get:
                1 - get json file 
                2 - print to console
                3 - get all data
                
                0 - go back
            """.format(url, params, threads, running_threads)
            
            input_select = functions.get_input("What do you want to select? ", get_data_text)
                
            #   write data to file
            if input_select == 1:
                if threads == True:
                    thread = threading.Thread(target=functions.thread_func, args=(data_select, data,), name=data_select)
                    thread.start()
                    continue
                else:
                    functions.write_to_json(data_select, data)
                    continue
            
            #   print data, and go back to main menu
            elif input_select == 2:
                pprint(data) 
                input("Press any key to continue")
                continue
        
        #   Get all data
        elif func_select == 4:
                if threads == True:
                    thread = threading.Thread(target=functions.get_all_data, args=(const_url), kwargs={"threading": True}, name="all_data")
                    thread.start()
                    continue
                else:
                    functions.get_all_data(const_url)
                    continue
 
        #   Set Run threading
        elif func_select == 5:
            if threads == False:
                threads = True
            else:
                threads = False
            continue

        #   Exit program
        elif func_select == 0:
            os.system("clear")
            print("Have a wonderful day!")
            print("you have to press ctrc + c since threading")
            break

        #   Error handle, if invalid input eg.: 10
        else:
            print("Invalid input!")

# If this file is called in terminal
if __name__ == "__main__":
    main(url, params)


