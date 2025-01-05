


# class Queue:

#     def __init__(self):
#         self.items = []
    
#     def insert(self, value):
#         self.items.append(value)

#     def pop(self):
        
#         if self.is_empty():
#             print("Queue is empty")
#             return None
#         return self.items.pop(0)


#     def is_empty(self):
#         return len(self.items) == 0
    


# queue = Queue()
# queue.insert(5)
# queue.insert(10)
# print(queue.pop())
# print(queue.pop())
# print(queue.is_empty())



# import pickle

# class  QueueOutOfRangeException(Exception):
#     pass



# class Queue:

#     queues  = {}

#     def __init__(self, size, name):
#         self.items = []
#         self.size = size
#         self.name = name
#         Queue.queues[name] = self

    
#     def enqueue(self, item):

#         if len(self.items) >= self.size:
#             raise QueueOutOfRangeException(
#                 f"Queue '{self.name}' has reached its size limit of {self.size}."
#             )
#         self.items.append(item)



#     def dequeue(self):
        
#         if self.is_empty():
#             print("Queue is empty")
#             return None
#         return self.items.pop(0)
    
#     def is_empty(self):
#         return len(self.items) == 0
    

#     @classmethod
#     def get_queue(cls, name):
#         return cls.queues.get(name, None)


#     @classmethod
#     def save_queues(cls, filename):

#         with open(filename, 'wb') as file:
#             pickle.dump(cls.queues, file)
        
#         print("Queues saved successfully")



#     @classmethod
#     def load_queues(cls, filename):
#         try:
#             with open(filename, 'rb') as file:
#                 cls.queues = pickle.load(file)
#             print("Queues loaded successfully")
#         except FileNotFoundError:
#             print("No saved queues found")
#         except Exception as e:
#             print("An error occurred while loading queues")
#             print(e)


# if __name__ == "__main__":

#     try:
#         queue = Queue(3, "first")
#         queue.enqueue(5)
#         queue.enqueue(10)
#         queue.enqueue(15)
#         queue.enqueue(20)
#     except QueueOutOfRangeException as e:
#         print(e)


#     Queue.save_queues("queues.pkl")
#     Queue.queues.clear()
#     Queue.load_queues("queues.pkl")
#     print(Queue.queues)


 
