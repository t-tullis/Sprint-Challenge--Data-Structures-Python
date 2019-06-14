class RingBuffer:
  def __init__(self, capacity):
    #capacity of ring buffer
    self.capacity = capacity
    #current # of items in ring buffer
    self.current = 0
    #generates array filled w/ none values multipled by the capacity
    self.storage = [None]*capacity

  def append(self, item):
    if self.current != self.capacity:
      self.storage[self.current] = item 
      self.current += 1
    else:
      self.current = 0
      self.append(item)

  def get(self):
    items = []
    for item in self.storage:
      if item != None:
        items.append(item)
      else:
        break
    return items

# ring_buffer = RingBuffer(3)

# ring_buffer.append('a')
# ring_buffer.append('b')
# ring_buffer.append('c')
# ring_buffer.append('d')
# print(ring_buffer.storage)
# print(ring_buffer.current)
# print(ring_buffer.capacity)
# print(ring_buffer.get())