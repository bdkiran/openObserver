![observer eye](extras/eye.png)

# openObserver

OpenObserver is a platform for building and packaging intelligent IOT devices. It emphasizes performance for running machine learning models on resource constrained devices. 

## About openObserver

The openObserver platform is built to be modular and extensible. Different models and workloads require different needs. To accommodate this open observer has an architecture built around adding and number of steps to complete in any particular task. Drop in any onyx model and provide any pre-and post processing steps to achieve your goal.

## Getting Started

1. Create a new virtual environment

1. Download project dependencies `OpenCV`(install complete opencv)  and `apt-get install libzmq3-dev`

1. `pip3 install -r requirements.txt`

1. Download the yolov4 onnx model from the onnx [models](https://github.com/onnx/models/tree/master/vision/object_detection_segmentation/yolov4). Also retrieve the require `coco.names` and `yolov4_anchors.txt` file.

1. In the resources directory and places the files from the previous step in there.

1. From the root directory, run `python3 main.py`

## Roadmap

1. convert message que to C++ and Cython. This is under the directory supaque.

1. Provide object serialization to MessagePack, Cap'n Proto or Protobuff. The serialization framework will be decided later up to suggestions.

1. Update post processing code to C++.

1. Create an interface for sending data back to the server using RPC(encoding can be in JSON or protopbuf).

1. Allow the output to stream video over “web RTC”(probably not technically web RTC but something similar).

1. Create tests and increase code coverage significantly.

1. Sufficiently document each individual module or sub project.

## Special Thanks

This project was heavily inspired by the [openpilot](https://github.com/commaai/openpilot) project developed by comma.ai. It uses a lot of the same tools and architecture
