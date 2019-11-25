from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return 'result : %d' % (num1+num2)
    
@app.route('/add/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)