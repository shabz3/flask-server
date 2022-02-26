from flask import Flask
import os

app = Flask(__name__)

# create route to call function
@app.route('/')
def index():
    return os.environ.get("MY_MESSAGE")
    
app.run(host='0.0.0.0', port=81)