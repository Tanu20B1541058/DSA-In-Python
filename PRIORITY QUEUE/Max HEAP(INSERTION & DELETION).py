class Max_heap:

    maxHeap = []

    def swap(parent, largestIndex):
        temp = Max_heap.maxHeap[parent]
        Max_heap.maxHeap[parent] = Max_heap.maxHeap[largestIndex]
        Max_heap.maxHeap[largestIndex] = temp

    def heapify(parent):
        size = len(Max_heap.maxHeap)
        left = 2 * parent + 1
        right = 2 * parent + 2
        
        largestIndex = parent

        if left < size and Max_heap.maxHeap[left] > Max_heap.maxHeap[largestIndex]:
            largestIndex = left

        if right < size and Max_heap.maxHeap[right] > Max_heap.maxHeap[largestIndex]:
            largestIndex = right

        if largestIndex != parent:
            Max_heap.swap(parent, largestIndex)
            Max_heap.heapify(largestIndex)

    def insert(data):
        Max_heap.maxHeap.append(data)
        size = len(Max_heap.maxHeap)
        child = size - 1
        parent = (child - 1)//2
        while parent >= 0 and Max_heap.maxHeap[child] > Max_heap.maxHeap[parent]:
            Max_heap.swap(child, parent)
            child = parent
            parent = (child - 1)//2

    def delete():
        size = len(Max_heap.maxHeap)
        if size == 0:
            return -1
        element = Max_heap.maxHeap[0]
        Max_heap.maxHeap[0] = Max_heap.maxHeap[size - 1]
        Max_heap.maxHeap.pop()
        Max_heap.heapify(0)
        return element
    
    def printHeap():
        print(Max_heap.maxHeap)

if __name__ == "__main__":
    Max_heap.insert(98)
    Max_heap.insert(87)
    Max_heap.insert(86)
    Max_heap.insert(44)
    Max_heap.insert(40)
    Max_heap.insert(32)
    Max_heap.insert(33)
    Max_heap.insert(20)
    Max_heap.insert(21)
    print(Max_heap.delete())
    Max_heap.printHeap()
    Max_heap.insert(100)
    Max_heap.printHeap()