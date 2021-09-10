import onnxruntime
import logging as log
import time
from queuer import publisher, subscriber

def run_loop(sess):
	log.info("Starting inference loop")
	sub = subscriber.Subscriber('preprocessed_images')
	outputs = sess.get_outputs()
	output_names = list(map(lambda output: output.name, outputs))
	input_name = sess.get_inputs()[0].name
	
	while True:
		t0 = time.time()
		image_data = sub.recieve_object()
		detections = sess.run(output_names, {input_name: image_data})
		publisher.publish_message_object('detections', detections)
		log.info(f'Detections Done. ({time.time() - t0:.3f}s)')


def main():
	print(onnxruntime.get_available_providers())
	model = "./detect/resources/yolov4.onnx"
	session = onnxruntime.InferenceSession(model)
	run_loop(session)


