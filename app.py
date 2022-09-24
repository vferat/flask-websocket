from distutils.debug import DEBUG
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

import random



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, logger=True, engineio_logger=True)


@app.route('/home')
def home():
    return render_template("page.html")

@socketio.on('my event')
def handle_message():
    x = random.randint(0,240)
    emit("feedback", x)

if __name__ == '__main__':
    socketio.run(app, debug=True)