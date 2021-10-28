import zmq

from queuer.topics import get_port_by_topic

# context = zmq.Context()
# socket = context.socket(zmq.SUB)
# socket.connect("tcp://localhost:5555")


class Subscriber:
    def __init__(self, topic):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        port = get_port_by_topic(topic)
        connection_address = "tcp://localhost:{port}".format(port=port)
        self.socket.connect(connection_address)
        topic_bytes = bytes("", encoding="ascii")
        self.socket.setsockopt(zmq.SUBSCRIBE, topic_bytes)
    
    def recieve_message(self):
        message = self.socket.recv_json()
        return message
    
    def recieve_object(self):
        message_object = self.socket.recv_pyobj()
        return message_object 
