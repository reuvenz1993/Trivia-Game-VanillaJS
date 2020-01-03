from trivia import app, db, socketio
import trivia.views

if __name__ == '__main__':
    socketio.run(app)
