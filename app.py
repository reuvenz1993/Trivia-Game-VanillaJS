from trivia import app, db, socketio
import trivia.views
from flask_socketio import emit

@socketio.on('connect')
def test_connect():
    print ('new connection')
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

'''
@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


@socketio.on('my event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)
    '''

if __name__ == '__main__':
    socketio.run(app, debug = True, use_reloader = False, port=1111)