from flask import Flask, render_template, request
import json
import os
import logging
from logging import StreamHandler
from env import *


app = Flask(__name__)
app.debug = os.environ.get("DEBUG") == DEBUG

# The logs shouldn’t written to a file, but to the container output
logs = logging.getLogger()
logs.setLevel(logging.INFO)
stream = StreamHandler()
logs.addHandler(stream)

# It can easily be restarted without loss of data
# The application should be built in such a way that the database can easily be replaced (development with production instance)
FILE_PATH = DEVELOPMENT_PATH if os.environ.get("DEBUG") == "1" else PRODUCTION_PATH 
if os.path.exists(FILE_PATH):
    with open(FILE_PATH) as f:
        TODO_ITEMS = json.load(f)
else:
    TODO_ITEMS = []


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        TODO_ITEMS.append(content)
        adding_data_to_db()

    logging.info("LIST has been saved.")
    return render_template("index.html", todo_items=TODO_ITEMS)

# It can easily be restarted without loss of data
def adding_data_to_db():
    with open(FILE_PATH, "w") as f:
        json.dump(TODO_ITEMS, f)


if __name__ == "__main__":
    app.run(host="0.0.0.0")