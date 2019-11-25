from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
    <head>
        <meta charset="utf-8">
        <title>첫번째 과제</title>
    </head>
    <body>
        <a href='http://localhost/abc'> 첫번째 과제 </a>
    </body>
    '''
@app.route('/abc')
def abc():
    return render_template('./abc.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
