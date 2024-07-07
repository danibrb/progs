"""flask example web application"""
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """create a page to say hello"""
    return """<html><body>
        <h1>Hello, world!</h1>
        The time is """ + str(datetime.now()) + """.
        </body></html>"""

if __name__ == "__main__":
   # Launch the Flask dev server
    app.run(host="localhost", debug=True)
