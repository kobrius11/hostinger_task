from datetime import datetime
import json
import requests
import time
import os


def get_json(url: str, params: dict = None) -> list:
    """
    Send get request to url, using requests.get()
    """

    response = requests.get(url, params)
    # if succesful get json, else, return status_code, reason, url.
    if response.status_code == 200:
        return response.json()
    else:
        data = {"status_code": response.status_code, 
                "error_message": response.reason, 
                "url": response.url}
        return data

def time_sleep(seconds: int) -> None:
    """
    time.sleep() function, wich prints remaining time.
    """
    for i in range(seconds, 0, -1):
        print("{:2d} seconds remaining till you can continue.".format(i))
        time.sleep(1)

def get_input(prompt: str, text: str = None, seconds: int = 3) -> int:
    """
    Python input function with error handling
    """
    while True:
        try:
            os.system("clear")
            if text:
                print(text)
            user_input = int(input(prompt))
        except Exception as e:
            os.system("clear")
            print("\033[0;31;40m Error: ", e, "\033[0;0m")
            time_sleep(seconds)
            continue

        return user_input
    
def write_to_json(data_select: str, data: list) -> str:
    """
    writes to json, save file as data_select(users, posts, comments) + todays date
    """
    filename = "{}-{:%Y-%m-%d_%H:%M:%S}.json".format(data_select, datetime.now())
    with open(filename, "w") as file:
        file.write(json.dumps(data, indent=4))
    file.close()

    return filename

def get_all_data(url: str) -> list:
    """
    Get all data, as json files. creates new folder and stores all (get) data of API's all endpoints (I think so).
    """
    folder_name = "./all_data-{:%Y-%m-%d_%H:%M:%S}".format(datetime.now())
    os.mkdir(folder_name)
    os.chdir(folder_name)

    data_select_list = ["users", "posts", "comments", "albums", "photos", "todos"]
    filenames = []

    for data_select in data_select_list:
        temp_url = url + data_select
        data = get_json(temp_url)
        filenames.append(write_to_json(data_select, data))

    return filenames





            
            






