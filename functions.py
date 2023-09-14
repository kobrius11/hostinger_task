from datetime import datetime
import json
import requests
import time
import os

def get_json(url: str, params: dict) -> list:
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
    
def write_to_json(data_select: str, data: list) -> None:
    """
    writes to json
    """
    with open(f"{data_select}-{datetime.now()}.json", "w") as file:
        for element in data:
            file.write(json.dumps(element))
            file.write("\n")

