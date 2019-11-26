from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hello')
def hello_world2():
   return 'hello world'

def hello_world3():
   return 'hello world'
app.add_url_rule('/hello2', 'hello', hello_world3)

@app.route('/hello3/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/cal_add/<int:num1>/<int:num2>')
def cal_add(num1, num2):
    return "결과값 : %d" % (num1+num2)

@app.route('/address/<addr1>')
def address(addr1):
    return "주소 : %s " % addr1

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)