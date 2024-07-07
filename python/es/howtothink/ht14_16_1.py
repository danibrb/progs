"""flask example web application"""
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """main page"""
    return HELLO_HTML

HELLO_HTML = """
    <html><body>
        <h1>Hello, world!</h1>
        Click <a href="/time">here</a> for the time.
    </body></html>
    """

@app.route('/time')
def time():
    """time page"""
    return TIME_HTML.format(datetime.now())

TIME_HTML = """
    <html><body>
        The time is {0}.
    </body></html>
    """

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)
