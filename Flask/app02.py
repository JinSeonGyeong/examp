from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/phone/<phone>')
def hello_phone(phone):
    return 'Your Phone Number is %s!' % phone

@app.route('/calculater/<number>')
def calculater(number):
    return '계산결과는 %.2f' % float(number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
