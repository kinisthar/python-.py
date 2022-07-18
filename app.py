from flask import flask
from config  import config 
app=flask(__name__)

@app.route('/')
 def index():
    return render_template('auth/login.html')
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app run()