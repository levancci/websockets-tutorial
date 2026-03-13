import socketio

sio = socketio.AsyncServer(async_mode='asgi') 
app = socketio.ASGIApp(sio, static_files={'/': './public/'})

client_count = 0

async def task(sid):
    await sio.sleep(5)
    result= await sio.call('mult', {'numbers': [4, 3]}, to=sid)
    print(result)

@sio.event
async def connect(sid, environ):
    global client_count
    client_count += 1
    print(sid, 'connected')
    sio.start_background_task(task, sid)
    await sio.emit('client_count', client_count)

@sio.event
async def disconnect(sid):
    global client_count
    client_count -= 1
    sio.emit('client_count', client_count)
    print(sid, 'disconnected') 


# @sio.event
# async def sum(sid, data):
#     result = data['numbers'][0] + data['numbers'][1]
#     # await sio.emit('sum_result', {'result': result}, to=sid)
#     return {'result': result}

