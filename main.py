from ProducerThread import ProducerThread
from Button import Button
import threading
semaphore = threading.Semaphore(1)

producer = ProducerThread(semaphore)
button = Button(semaphore)

producer.start()
button.start()
producer.join()
button.join()

print ("Exiting Main Thread")