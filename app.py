from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')     # Entry point | the / means the root
def index():        # name we give the route, this one is index
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

if __name__ == '__main__':      #runs the web server and the app
    app.run(debug=True, host='0.0.0.0') # 0.0.0.0 makes it accessible to any device on the network
