from flask import Flask, render_template, request
import database
import env

app = Flask(__name__)
app.debug = env.DEBUG


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        database.todo_items(content)

    return render_template("index.html", todo_items=database.TODO_ITEMS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6001, debug=True)
