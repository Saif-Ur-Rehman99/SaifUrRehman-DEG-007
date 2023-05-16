import json
import requests
import env

#import logging
# import threading
# import time
import os

class TODO_Item:
    def __init__(self, id: int, content:str) -> None:
        self.id = id
        self.content = content


def get_todo_items() -> list:
    url = 'http://localhost:8000/data'
    response = requests.get(url)
    data = json.loads(response.content)
    return [TODO_Item(id=item['id'], content=item['content']) for item in data]

def add_todo_items(content:str):
    url = 'http://localhost:8000/data'
    data = {'content': content}
    requests.post(url, data=data)

# logging.basicConfig(
#     filename="logs.txt",
#     filemode="a",
#     format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
#     datefmt="%H:%M:%S",
# )


# TODO_FILE_NAME = "todo.json"
# if os.path.exists(TODO_FILE_NAME):
#     with open(TODO_FILE_NAME) as f:
#         TODO_ITEMS = json.load(f)
# else:
#     TODO_ITEMS = []


# def todo_items():
#     #time.sleep(10)
#     with open(TODO_FILE_NAME, "w") as f:
#         json.dump(TODO_ITEMS, f)


#saving_thread = threading.Thread(target=todo_items)
#saving_thread.start()
