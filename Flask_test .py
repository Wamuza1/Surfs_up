# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)




@app.route('/')
def hello_world():
    return 'Hello world'


if __name__ == "__main__":
    app.run(debug=True)