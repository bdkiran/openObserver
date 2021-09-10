import zmq

# context = zmq.Context()
# socket = context.socket(zmq.SUB)
# socket.connect("tcp://localhost:5555")


class Subscriber:
    def __init__(self, topic):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect("tcp://localhost:5555")
        topic_bytes = bytes(topic, encoding="ascii")
        self.socket.setsockopt(zmq.SUBSCRIBE, topic_bytes)
    
    def recieve_message(self):
        topicRecieved = self.socket.recv_string()
        message = self.socket.recv_json()
        return message
    
    def recieve_object(self):
        topicRecieved = self.socket.recv_string()
        message_object = self.socket.recv_pyobj()
        return message_object 
