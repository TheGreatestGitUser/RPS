from flask import Flask, redirect, send_file, render_template, request
import random
import requests
import io
app = Flask(__name__)

@app.route('/')
def index():
    data = [random.randint(1, 100) for i in range(0, 10)]
    return render_template('index.html', data = data)

# rock -> 0
# scissors -> 1
# paper -> 2


def winner (a, b):
    if a == b:
        return None
    elif a ==0 and b == 1:
        return True
    elif a ==1 and b == 2:
        return True
    elif a ==2 and b == 0:
        return True
    return False

@app.route('/rps')
def rps():
    move = int(request.args.get('move'))
    server_move = random.randint(0,3)
    result = winner(move, server_move)
    print (result)
    return render_template('rps.html', move=move, server_move=server_move, result=result)


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str(a + b)

@app.route('/xkcd')
def xkcd(): 
    data = requests.get('https://c.xkcd.com/random/comic/')
    data = requests.get("https://xkcd.com/" + data.url[17:-1] +"/info.0.json").json()
    data = requests.get(data['img'])
    return send_file(io.BytesIO(data.content), mimetype=data.headers['Content-Type'], attachment_filename='comic')

app.run('0.0.0.0', port = 8000)