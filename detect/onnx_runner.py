import onnxruntime
import logging as log
import time
from queuer import publisher, subscriber

def run_loop(sess):
	log.info("Starting inference loop")
	sub = subscriber.Subscriber('processed_images')
	pub = publisher.Publisher('detections')

	outputs = sess.get_outputs()
	output_names = list(map(lambda output: output.name, outputs))
	input_name = sess.get_inputs()[0].name
	
	while True:
		t0 = time.time()
		image_data = sub.recieve_object()
		detections = sess.run(output_names, {input_name: image_data})
		pub.publish_message_object(detections)
		log.info(f'Detections Done. ({time.time() - t0:.3f}s)')


def main():
	# Looks like changing the execution to a GPU does not impact performance positively
	# https://github.com/microsoft/onnxruntime/discussions/7665
	# https://github.com/microsoft/onnxruntime/issues/2373

	providers = [
		('CUDAExecutionProvider', {
			'device_id': 0,
			'arena_extend_strategy': 'kNextPowerOfTwo',
			'gpu_mem_limit': 2 * 1024 * 1024 * 1024,
			'cudnn_conv_algo_search': 'EXHAUSTIVE',
			'do_copy_in_default_stream': True,
		})
		#'CPUExecutionProvider'
	]

	print(onnxruntime.get_available_providers())
	print(onnxruntime.get_device())
	model = "./detect/resources/yolov4.onnx"
	session = onnxruntime.InferenceSession(model, providers=providers)
	run_loop(session)

