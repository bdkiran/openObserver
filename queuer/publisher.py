import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

def publish_message(topic, msg):
    topic = 'msg'
    socket.send_string(topic, zmq.SNDMORE)
    socket.send_json({"message": msg})

def publish_message_object(topic, obj):
    socket.send_string(topic, zmq.SNDMORE)
    socket.send_pyobj(obj)

