from flask import Flask
app = Flask(__name__)
  

@app.route('/',methods=['GET','POST'])

def hello_world():
    return 'Simple Machine Learning Project'
  

if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()