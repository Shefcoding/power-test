# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def power():
    x=2
    y=2
    return x**y

@app.route('/cow')
def cow():
    return 'MOoooOoo!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')



