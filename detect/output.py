import cv2
import logging as log

import queuer.subscriber as subscriber
import numpy as np
import time
from detect.yolov4_processing import postProcessFrameStream

from detect.sort import sort

def run_video_output():
    log.info("starting to run video")
    show_video = True

    mot_tracker = sort.Sort()

    og_frames_sub = subscriber.Subscriber('camera_frames')
    detect_sub = subscriber.Subscriber('detections')
    
    i = 0
    while True:
        t0 = time.time()
        log.info("Outputting frame: " + str(i))
        original_image = og_frames_sub.recieve_object()
        detections = detect_sub.recieve_object()

        image = postProcessFrameStream(detections, original_image, mot_tracker)
        
        if show_video:
            cv2.imshow("Frame", image)
            if cv2.waitKey(1) == 'q':
                break
        i += 1
        log.info(f'processing Done. ({time.time() - t0:.3f}s)')

    cv2.destroyAllWindows()