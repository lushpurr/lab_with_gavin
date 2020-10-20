class BusStop:
    def __init__(self, name, length_of_queue):
        self.name = name
        self.length_of_queue = []

    def add_to_queue(self, name):
        self.queue.append(name)

    def queue_length(self):
        return len(self.length_of_queue)

    
