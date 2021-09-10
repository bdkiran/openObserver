from threading import Thread
from detect import camera, output, onnx_runner, onnx_runner
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    camera_capture_process = Thread(target=camera.run_camera_capture)
    model_proccess = Thread(target=onnx_runner.main)
    video_output = Thread(target=output.run_video_output)

    camera_capture_process.start()
    model_proccess.start()
    video_output.start()