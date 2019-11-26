from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
   dict = {'물리':50,'화학':60,'수학':70}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug = True)