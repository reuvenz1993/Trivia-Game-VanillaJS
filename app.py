from trivia import app, db, socketio
import trivia.views
from flask_socketio import emit
import json

@socketio.on('connect')
def test_connect():
    print ('new connection')
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('message')
def handle_message(message):
    r = message
    print (r)
    print ('handle_message function run')
    ar = json.loads(message)
    print (ar)
    print('received message: ' + message)


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))



@socketio.on('my event')
def handle_my_custom_event(data):
    print('received args: ' + data)


if __name__ == '__main__':
    socketio.run(app, debug = True, use_reloader = False, port=1111)