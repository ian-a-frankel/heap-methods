import random

class Min_heap:

    def __init__(self, orderable_list):
        self.heap = []
        for value in orderable_list:
            self.heap_append(value)

    @classmethod
    def parent_index(cls, index):
        return (index - 1) // 2
    
    @classmethod
    def children(cls, index, length):
        kids = []
        if 2 * index + 1 < length:
            kids.append(2 * index + 1)
        if 2 * index + 2 < length:
            kids.append(2 * index + 2)
        return kids

    def heap_append(self, value):
        current_index = len(self.heap)
        self.heap.append(value)
        while current_index > 0 and value < self.heap[self.parent_index(current_index)]:
            self.heap[current_index] = self.heap[self.parent_index(current_index)]
            self.heap[self.parent_index(current_index)] = value
            current_index = self.parent_index(current_index)

    def heap_pop(self):
        # This function will return the value of the root, and also convert heap_list to a heap consisting of all values except the original root.
        # swap first and last elements of heap_list

        #save value to return and value of last element

        value_to_pop = self.heap[0]
        value = self.heap[-1]

        kept_length = len(self.heap) - 1
        
        # set new value for root, to be pushed down until it has no smaller children
        
        self.heap[0] = value

        current_index = 0

        while current_index < kept_length:
            kids = self.children(current_index, kept_length)
            if len(kids) == 0:
                current_index = kept_length
            elif len(kids) == 1 or (self.heap[kids[0]] < self.heap[kids[1]]):
                if self.heap[kids[0]] < value:
                    self.heap[current_index] = self.heap[kids[0]]
                    self.heap[kids[0]] = value
                    current_index = kids[0]
                else:
                    current_index = kept_length
            else:
                if self.heap[kids[1]] < value:
                    self.heap[current_index] = self.heap[kids[1]]
                    self.heap[kids[1]] = value
                    current_index = kids[1]
                else:
                    current_index = kept_length
        
        self.heap.pop()
        return value_to_pop

    def heap_sort(self):

        sorted_values = []
        length = len(self.heap)
        for i in range(length):
            sorted_values.append( self.heap_pop() )
        self.heap = sorted_values

number_list = []
for i in range(10000):
    number_list.append(random.randint(1,10000))

print('Original List of numbers:')
print(number_list)

random_heap = Min_heap(number_list)

print('After min_heapifying:')
print(random_heap.heap)

print('After min_heap_sorting:')
random_heap.heap_sort()
print(random_heap.heap)