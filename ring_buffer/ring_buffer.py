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
    pass

ring_buffer = RingBuffer(3)

ring_buffer.append('a')
ring_buffer.append('b')
print(ring_buffer.storage)
print(ring_buffer.current)
print(ring_buffer.capacity)