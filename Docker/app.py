from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return "Hello, Flask is running inside a container! by Monali"
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

