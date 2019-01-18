from flask import Flask

app = Flask(__name__)

# http://localhost:5000/
@app.route('/')
def index():
    return 'Hello Flask!'


# http://localhost:5000/abc 요청을 처리
@app.route('/abc')
def abc():
    return 'abc를 요청하셨군요.'

# http://localhost:5000/def
@app.route('/ccc')
def ccc():
    return 'ccc를 요청하셨군요'

if __name__ == '__main__':
    app.run(debug=True)
