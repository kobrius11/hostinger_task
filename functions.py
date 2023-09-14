from datetime import datetime
from pprint import pprint
import requests
import json
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
        pprint(data)
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
    
def write_to_json(data_select: str, data: list, filename: str = None) -> str:
    """
    writes to json, save file as data_select(users, posts, comments, albums, photos, todos) + todays date
    """
    if filename == None:
        filename = "{}-{:%Y-%m-%d_%H:%M:%S}".format(data_select, datetime.now())

    with open(filename + ".json", "w") as file:
        file.write(json.dumps(data, indent=4))
    file.close()
    return filename

def get_all_data(url: str, wait_time: int = 90, times: int = 5, threading: bool = False) -> list:
    """
    Get all data, as json files. creates new folder and stores all (get) data of API's all endpoints (I think so). \n
    Calls api endpoints total six times
    Threading support: if True will run as a thread
    """
    folder_name = "./all_data"
    try:
        os.mkdir(folder_name)
    except Exception:
        pass
    os.chdir(folder_name)

    data_select_list = ["users", "posts", "comments", "albums", "photos", "todos"]
    filenames = []
    while times > 0:
        for data_select in data_select_list:
            temp_url = url + data_select
            data = get_json(temp_url)
            filenames.append(write_to_json(data_select, data, filename=data_select))
        times -= 1
        if threading:
            time.sleep(wait_time)
    os.chdir("..")
    return filenames

def thread_func(data_select: str, data: list, wait_time: int = 90, repeat: int = 5) -> None:
    """
    takes write_to_json function and it interval and repeat variable. \n
    repeat = -1, will reapeat forever.
    """
    while repeat > 0:
        write_to_json(data_select, data)
        time.sleep(wait_time)
        repeat -= 1






            
            






