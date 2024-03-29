from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
    <head>
        <meta charset="utf-8">
        <title>로그인</title>
    </head>
    <body>
        <a href='http://localhost/login'> 로그인 </a>
    </body>
    </html>
    '''
@app.route('/login')
def abc():
    return render_template('./login.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/result',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('name')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug = True)