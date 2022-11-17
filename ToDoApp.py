from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Todo.html')


if __name__ == '__main__':
    app.run()