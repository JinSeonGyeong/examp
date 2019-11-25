from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask"

@app.route('/abc')
def abc():
    return render_template('./abc.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
