import cv2
import logging as log
import numpy as np
from detect.resources.yolov4_processing import image_preprocess
from queuer.publisher import Publisher

def run_camera_capture():
    log.info("Starting to run camera...")
    video_capture = cv2.VideoCapture(0)

    if not video_capture:
        log.error("Unable to open camera")

    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    log.info(fps)

    input_size = 416

    camera_frame_pub = Publisher('camera_frames')
    processed_fram_pub = Publisher('processed_images')

    i = 0
    while True:
        log.info("Procces frame: " + str(i))
        ret, frame = video_capture.read()
    
        if not ret:
            log.warning("Stream has ended")
            break

        image_data = preprocess(frame, input_size)

        camera_frame_pub.publish_message_object(frame)
        processed_fram_pub.publish_message_object(image_data)
        i += 1
        
    video_capture.release()


def preprocess(original_image, input_size):
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    # #Preproccess images
    image_data = image_preprocess(np.copy(original_image), [input_size, input_size])
    image_data = image_data[np.newaxis, ...].astype(np.float32)
    return image_data
