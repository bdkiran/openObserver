
TOPICS = {"topic0": 5555, "topic1": 5556, "camera_frames": 5557, "processed_images": 5558, "detections": 5559}

def get_port_by_topic(topic):
    port = TOPICS[topic]
    if port == None:
        port = 0
    return port
