class RingBuffer:
  def __init__(self, capacity):
    #capacity of ring buffer
    self.capacity = capacity
    #current # of items in ring buffer
    self.current = 0
    #generates array filled w/ none values multipled by the capacity
    self.storage = [None]*capacity

  def append(self, item):
    #if current is not equal to capacity
    if self.current != self.capacity:
      #then set storage[current] equal to item
      self.storage[self.current] = item 
      #then increment current by 1
      self.current += 1
    else:
      #current = 0
      self.current = 0
      #then append item 
      self.append(item)

  def get(self):
    #create empty item list
    items = []
    #for every item in storage
    for item in self.storage:
      #if the item is not equal to None
      if item != None:
        #then append the item to the items list
        items.append(item)
      else:
        #break out of the for loop 
        break
     #and return the array of items which will not contain "None"   
    return items

ring_buffer = RingBuffer(3)

ring_buffer.append('a')
ring_buffer.append('b')
# ring_buffer.append('c')
# ring_buffer.append('d')
print(ring_buffer.storage)
print(ring_buffer.current)
print(ring_buffer.capacity)
print(ring_buffer.get())