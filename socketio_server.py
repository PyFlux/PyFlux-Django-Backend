import socketio
import eventlet
eventlet.monkey_patch()

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.on('connect')
def connect(sid, environ):
    print('+'*20)
    print('connect ', sid)

@sio.on('chat')
def chat(sid, data):
    print('='*20)
    # data -> {'from': {'id': 631174, 'avatar': 'https://api.adorable.io/avatars/285/631174.png', 'name': 'sumee'}, 'content': 'sadf'}
    sio.emit('chat', data)

# @sio.on('join')
# def join(sid, data):
#     sio.join(data)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8080)), app)
    # eventlet.wsgi.server(eventlet.listen(('178.128.64.194', 8080)), app)
