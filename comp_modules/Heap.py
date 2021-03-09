# Implementation of Min/Max Heap with Heapsort Support
class PriorityHeap:
    def __init__(self, mode='max', name=None):
        self.name = name
        self.mode = mode
        self.heap = []
    
    def __repr__(self):
        return self.name

    def fatherOf(self, position):
        father_position = (position - 1) // 2
        try:
            return self.heap[father_position]
        except IndexError:
            print(f"{father_position} index out of bounds")

    def leftChildOf(self, position):
        left_child_position = (position * 2) + 1
        try:
            return self.heap[left_child_position]
        except IndexError:
            return None

    def rightChildOf(self, position):
        right_child_position = (position + 1) * 2
        try:
            return self.heap[right_child_position]
        except IndexError:
            return None

    def inspect(self):
        if len(self.heap) == 0:
            return None
        else:
            return self.heap[0]
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        else:
            to_pop = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap = self.heap[0:-1]
            self.combine(at_node=0)
        return to_pop

    def swap(self, pos_a, pos_b):
        self.heap[pos_a], self.heap[pos_b] = self.heap[pos_b], self.heap[pos_a]
        return
    
    def combine(self, at_node):
        lcp = (at_node * 2) + 1
        rcp = (at_node + 1) * 2
        if self.mode == 'max':
            if lcp < len(self.heap)  and self.heap[at_node] < self.leftChildOf(at_node) :
                # Need to Swap
                self.swap(at_node, lcp)
                self.combine(at_node=lcp)
                
            if rcp < len(self.heap)  and self.heap[at_node] < self.rightChildOf(at_node):
                # Need to Swap
                self.swap(at_node, rcp)
                self.combine(at_node=rcp)
                
        elif self.mode == 'min':
            if lcp < len(self.heap) and self.heap[at_node] > self.leftChildOf(at_node):
                # Need to Swap
                self.swap(at_node, lcp)
                self.combine(at_node=lcp)
                
            elif rcp < len(self.heap) and self.heap[at_node] > self.rightChildOf(at_node):
                # Need to Swap
                self.swap(at_node, rcp)
                self.combine(at_node=rcp)

    def insert(self, value):
        self.heap.append(value)
        # Bubble up to correct position
        current_pos = len(self.heap) - 1
        print("Current Position is", current_pos)
        if self.mode == 'max':
            father_pos = (current_pos - 1) // 2
            print("Father Position is", father_pos)
            while current_pos > 0 and self.heap[current_pos] > self.fatherOf(current_pos):
                self.swap(current_pos, father_pos)
                print(f"Swapped {self.heap[current_pos]} with {self.heap[father_pos]}")
                current_pos = father_pos
                father_pos = (current_pos - 1) // 2
        elif self.mode == 'min':
            father_pos = (current_pos - 1) // 2
            while current_pos > 0 and self.heap[current_pos] < self.fatherOf(current_pos):
                self.swap(current_pos, father_pos)
                current_pos = father_pos
                father_pos = (current_pos - 1) // 2
                
                
    def heapFromIterable(self, iterable):
        self.heap = iterable
        for i in range((len(self.heap) // 2 - 1), -1, -1):
            self.combine(at_node=i)
            
    def sort(self):
        for i in range((len(self.heap) - 1), 0, -1):
            self.combine(at_node=i)
            self.swap(0,i)
            self.combine(at_node=0)
    
    def heapsort(self, iterable):
        self.heapFromIterable(iterable)
        self.sort()
