#from threading import Thread
from detect import camera, output, onnx_runner
from multiprocessing import Process
import logging
# import time
# from queuer import publisher, subscriber

# def publishMsgTest(topic):
#     logging.info("publishing messages!")
#     pub = publisher.Publisher(topic)
#     i = 0 
#     while True:
#         msg = "Message " + str(i)
#         pub.publish_message(msg)
#         i += 1
#         time.sleep(1)

# def subscribeMsgTest(topic):
#     logging.info("recieving messages!")
#     sub = subscriber.Subscriber(topic)
#     while True:
#         msg = sub.recieve_message()
#         logging.info(msg)
        

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # p1 = multiprocessing.Process(target=publishMsgTest, args=("topic0", ))
    # p2 = multiprocessing.Process(target=publishMsgTest, args=("topic1", ))

    # p3 = multiprocessing.Process(target=subscribeMsgTest, args=("topic0", ))
    # p4 = multiprocessing.Process(target=subscribeMsgTest, args=("topic1", ))

    # p1.start()
    # p2.start()

    # p3.start()
    # p4.start()


    camera_capture_process = Process(target=camera.run_camera_capture)
    model_proccess = Process(target=onnx_runner.main)
    video_output = Process(target=output.run_video_output)

    camera_capture_process.start()
    model_proccess.start()
    video_output.start()

