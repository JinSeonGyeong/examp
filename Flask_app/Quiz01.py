from flask import Flask, render_template
app = Flask(__name__)

@app.route('/where/<string:where>')
def hello_name(where):
   return render_template('./where.html', where = where)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug = True)