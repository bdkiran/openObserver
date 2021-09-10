import requests
import logging as log

#(2) We need to package our detections to a file or json payload
# In the initial version I created, I have a object called detected objects
# Those detected objects are then sent back in our boat message type

# Do we want to generate the timestamp when we instanciate the object?
# Do we need a seperate class for this if we don't have any other methods? 
class DetectedObject:
  def __init__(self, object_id, timestamp, frame_number, item_class, xywh, accuracy):
    self.objectID = object_id
    self.timestamp = round(timestamp * 1000)
    self.frameNumber = frame_number
    self.itemClass = item_class
    self.x = xywh[0].item()
    self.y = xywh[1].item()
    self.width = xywh[2].item()
    self.height = xywh[3].item()
    self.accuracy = accuracy

class Boat:
  def __init__(self, device_id, frames_per_second, detected_objects=[]):
    self.deviceID = device_id
    self.detectedObjects = detected_objects
    self.fps = frames_per_second

  def addDetectedObjects(self, detected_objects):
    for detected_object in detected_objects:
        self.detectedObjects.append(detected_object)
    if len(self.detectedObjects) > 10:
        self.send()

  def reset(self):
    self.detectedObjects = []

  def jsonEncode(self):
    detectedData = [detectedObject.__dict__ for detectedObject in self.detectedObjects]
    payload = {
      "deviceID": self.deviceID,
      "FPS": self.fps,
      "detectedData": detectedData,
    }
    return payload

  def send(self):
    #url = "http://localhost:8080" #This value should be retrieved from env variables
    #payload = self.jsonEncode()
    print(self)
    self.reset()
    # for _ in range(3): #Retry the request 3 times
    #   response = requests.post(url, json=payload)
    #   if response.status_code == 201 or response.status_code == 200:
    #     self.reset()
    #     break
    #   else:
    #     log.error("Error sending request")
    #     # Retry tho...
