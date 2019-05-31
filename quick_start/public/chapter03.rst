===================
Chapter 3: Chatting
===================

Socketio Server
===============

Install Socketio Server
-----------------------

install::

    pip install python-socketio
    pip install eventlet

create `socketio_server.py`::

	import socketio
	import eventlet
	eventlet.monkey_patch()
	sio = socketio.Server()
	app = socketio.WSGIApp(sio, static_files={
	    '/': {'content_type': 'text/html', 'filename': 'index.html'}
	})
    
	@sio.on('connect')
	def connect(sid, environ):
	    print('connect ', sid)
    
	@sio.on('chat')
	def chat(sid, data):
	    sio.emit('chat', data)
    
	@sio.on('disconnect')
	def disconnect(sid):
	    print('disconnect ', sid)
    
	if __name__ == '__main__':
	    eventlet.wsgi.server(eventlet.listen(('', 8080)), app)

here take a look at chat emit function::

	@sio.on('chat')
	def chat(sid, data):
	    sio.emit('chat', data)

if a client send a message to suhail(to_user), they 
will emit chat. the server recieve those data and emit 
chat so that suhail will be notified

Socketio Client
===============

::

    private initSocketConnection(): void {
        this.socket = socketIo('http://localhost:8080');

        this.socket.on('chat', (data) => {
            if (data.to_user==this.userid) {
                const activechatuser = this.chat.to_user;
                // if current active chat user is equal to 
                // the from user of socket emitted data
                if (activechatuser == data.from_user) {
                   this.chats.push(data);
                } else {
                    // if inactive user equal to fromuser
                    // find that inactive user
                    let user = this.chatusers.find(o => o.id === data.from_user);
                    // increment unread
                    user['unread'] ++;
                    this.playAudio();
                    // console.log('Need to show notification for: ' + user.full_name);
                }
                
            }
        });
    }
    
    sendMessage(){
        if (this.chat.message){
            this.chatService.postChat(this.chat)
            .subscribe((response) => {
                this.chat.message = '';
                this.chats.push(response);
                this.socket.emit('chat', response);
            }, // success
            error => {
                alert(error.error);
            })
        }
    }
