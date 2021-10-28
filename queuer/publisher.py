import zmq

from queuer.topics import get_port_by_topic

class Publisher:
    def __init__(self, topic):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        port = get_port_by_topic(topic)
        connection_address = "tcp://*:{port}".format(port=port)
        self.socket.bind(connection_address)
        self.topic = topic
    
    def publish_message(self, msg):
        self.socket.send_json({"message": msg})

    def publish_message_object(self, obj):
        self.socket.send_pyobj(obj)

