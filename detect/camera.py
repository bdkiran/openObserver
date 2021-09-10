import cv2
import logging as log
import numpy as np
from detect.yolov4_processing import image_preprocess
import queuer.publisher as publisher

def run_camera_capture():
    log.info("Starting to run camera...")
    video_capture = cv2.VideoCapture(0)

    if not video_capture:
        log.error("Unable to open camera")

    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    log.info(fps)

    input_size = 416

    i = 0
    while True:
        log.info("Procces frame: " + str(i))
        ret, frame = video_capture.read()
    
        if not ret:
            log.warning("Stream has ended")
            break

        image_data = preprocess(frame, input_size)

        publisher.publish_message_object('camera_frames', frame)
        publisher.publish_message_object('preprocessed_images', image_data)
        i += 1
        
    video_capture.release()


def preprocess(original_image, input_size):
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    # #Preproccess images
    image_data = image_preprocess(np.copy(original_image), [input_size, input_size])
    image_data = image_data[np.newaxis, ...].astype(np.float32)
    return image_data
