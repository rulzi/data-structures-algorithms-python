from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
'''
Design a food ordering system where your python program will run two threads,

1. Place Order: This thread will be placing an order and inserting that into a queue.
   This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
2. Serve Order: This thread will server the order.
   All you need to do is pop the order out of the queue and print it.
   This thread serves an order every 2 seconds.
   Also start this thread 1 second after place order thread is started.
'''

q = Queue()

def place_order(orders):
    for order in orders:
        q.enqueue(order)
        print("Order", order)
        time.sleep(0.5)
        
def serve_order():
    time.sleep(1)
    while not q.is_empty():
        print("Serve", q.dequeue())
        time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']


place = threading.Thread(target=place_order, args=(orders,))
serve = threading.Thread(target=serve_order, args=())

place.start()
serve.start()

place.join()
serve.join()

time_start = time.time()
print("Order done in", time.time() - time_start)
