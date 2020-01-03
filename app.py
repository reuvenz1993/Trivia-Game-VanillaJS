from trivia import app, db, socketio
import trivia.views
from flask_socketio import SocketIO

socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)
