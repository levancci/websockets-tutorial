import socketio
import eventlet
import eventlet.wsgi

sio = socketio.Server() 
app = socketio.WSGIApp(sio, static_files={'/': './public/'})

@sio.event
def connect(sid, environ):
    print(sid, 'connected')

@sio.event
def disconnect(sid):
    print(sid, 'disconnected') 


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)