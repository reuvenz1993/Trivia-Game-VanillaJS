from trivia import app, db, socketio
import trivia.views
from flask_socketio import emit, send
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
    try:
        ar = json.loads(message)
        print (ar)
    except:
        print("not json")
    print('received message: ' + message)
    send(message)


@socketio.on('json')
def handle_json(json):
    try:
        jsondata = json
        print (jsondata)
    except:
        jsondata_2 = json.loads(json)
    print('received json: ' + str(json))
    return 'one', 2



@socketio.on('my_event')
def handle_my_custom_event(data):
    print('received args: ' + data)
    send(data)


if __name__ == '__main__':
    socketio.run(app, debug = True, use_reloader = False, port=1111)