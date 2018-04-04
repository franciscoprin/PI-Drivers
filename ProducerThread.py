import threading
import time
from Producer import Producer
from Point import Point
import math

exitFlag = 0

class ProducerThread (threading.Thread):
   def __init__(self, semaphore):
      threading.Thread.__init__(self)
      self.semaphore = semaphore

   def run(self):
       # Setting producer.
       producer = Producer()
       producer.setPort(9092)
       producer.setIP("10.0.0.63")
       producer.startConnection()
       #sending messages.
       for x in range(0, 100):
           print("Send message....")
           self.semaphore.acquire()
           producer.sendMessage(Point(5*x,10*math.sin(5*x +10) + 40))
           self.semaphore.release()




