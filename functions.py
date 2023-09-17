from logger import create_logger
from datetime import datetime
from pprint import pprint
import requests
import json
import time
import os

logger = create_logger(f"{__name__}", "logs.log")

def get_json(url: str, params: dict = None) -> list:
    """
    Send get request to url, using requests.get()
    """
    logger.info(f"get_json: started running, url {url}, params {params}")
    response = requests.get(url, params)

    # if succesful get json, else, return status_code, reason, url.
    if response.status_code == 200:
        logger.info(f"get_json: exiting function, status code {response.status_code}")
        return response.json()
    else:
        data = {"status_code": response.status_code, 
                "error_message": response.reason, 
                "url": response.url}
        logger.error(f"get_json error: exiting function, status code {response.status_code}, error_message {response.reason}")
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
            logger.error(f"get_input error: Error {e}")
            time_sleep(seconds)
            continue
        logger.info(f"get_input: exiting program {user_input}")
        return user_input

def create_folder(folder_name: str) -> str:
    """
    Create's a folder in ./ , if folder exists handles exception.
    """
    try:
        logger.info(f"create_folder: attempt to create folder {folder_name}")
        os.mkdir(folder_name)
    except Exception as e:
        logger.error(f"create_folder error: folder {folder_name} failed to create {e}")
        pass

    return folder_name
    
def write_to_json(data_select: str, data: list, filename: str = None, folder_name: str = "./data") -> str:
    """
    writes to json, save file as data_select(users, posts, comments, albums, photos, todos) + todays date
    data_select: (users, posts, comments, albums, photos, todos).
    data: json formated into dict or list of dicts.
    filename: specific name you want your file to be.
    folder_name: specific name you want your folder to be.

    """
    logger.info(f"write_to_json: started running, data selected {data_select}")
    if filename == None:
        filename = "{}-{:%Y-%m-%d_%H:%M:%S}".format(data_select, datetime.now())
    create_folder(folder_name)
    
    with open(folder_name + "/" + filename + ".json", "w") as file:
        file.write(json.dumps(data, indent=4))
    file.close()
    logger.info(f"write_to_json: exiting function, filename {filename}  data selected {data_select}")
    return filename

def write_to_json_repeated(data_select: str, data: list, wait_time: int = 90, repeat: int = -1) -> None:
    """
    takes write_to_json function and reapeats it (repeat :arg:) of times, with 90 seconds or (wait_time :arg:) pause periods. \n
    data_select: (users, posts, comments, albums, photos, todos).
    data: json formated into dict or list of dicts.
    repeat = -1, will reapeat forever.
    wait_time = period of seconds between function calls
    """
    logger.info(f"thread_func: started running collecting {data_select} data, repeat {repeat}")
    while repeat != 0:
        write_to_json(data_select, data)
        time.sleep(wait_time)
        repeat -= 1
        logger.info(f"thread_func: {repeat} reapeats left")
    logger.info(f"thread_func: exited collecting {data_select}")

def get_all_data(threading: bool, wait_time: int = 90, repeat: int = -1) -> list:
    """
    Get all data, as json files. creates new folder and stores all (get) data of API's all endpoints (I think so). \n
    Calls api endpoints total six times
    Threading support: if True will run as a thread
    repeat: -1 will run forever
    wait_time:  period of seconds between function calls
    """
    url = "https://jsonplaceholder.typicode.com/"
    
    logger.info(f"get_all_data: started running, repeat {repeat} wait_time {wait_time} threading {threading}")

    data_select_list = ["users", "posts", "comments", "albums", "photos", "todos"]
    filenames = []
    if threading:
        while repeat != 0:
            for data_select in data_select_list:
                logger.info(f"get_all_data: data selected {data_select}")
                temp_url = url + data_select
                try:
                    data = get_json(temp_url)
                except Exception as e:
                    logger.critical(f"get_all_data error: fatal {e}")
                    return
                filenames.append(write_to_json(data_select, data, filename=data_select, folder_name="./all_data"))
                
            repeat -= 1
            time.sleep(wait_time)
    else:
        for data_select in data_select_list:
            logger.info(f"get_all_data: data selected {data_select}")
            temp_url = url + data_select
            try:
                data = get_json(temp_url)
            except Exception as e:
                logger.critical(f"get_all_data error: fatal {e}")
                return
            filenames.append(write_to_json(data_select, data, filename=data_select, folder_name="./all_data"))
    logger.info(f"get_all_data: exiting function, return {filenames}")
    
    return filenames



            
            






