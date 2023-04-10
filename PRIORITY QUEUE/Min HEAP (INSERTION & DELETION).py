class Innoskrit:

    minHeap = []

    def swap(parent, largestIndex):
        temp = Innoskrit.minHeap[parent]
        Innoskrit.minHeap[parent] = Innoskrit.minHeap[largestIndex]
        Innoskrit.minHeap[largestIndex] = temp

    def heapify(parent):
        size = len(Innoskrit.minHeap)
        left = 2 * parent + 1
        right = 2 * parent + 2
        
        largestIndex = parent

        if left < size and Innoskrit.minHeap[left] < Innoskrit.minHeap[largestIndex]:
            largestIndex = left

        if right < size and Innoskrit.minHeap[right] < Innoskrit.minHeap[largestIndex]:
            largestIndex = right

        if largestIndex != parent:
            Innoskrit.swap(parent, largestIndex)
            Innoskrit.heapify(largestIndex)

    def insert(data):
        Innoskrit.minHeap.append(data)
        size = len(Innoskrit.minHeap)
        child = size - 1
        parent = (child - 1)//2
        while parent >= 0 and Innoskrit.minHeap[child] < Innoskrit.minHeap[parent]:
            Innoskrit.swap(child, parent)
            child = parent
            parent = (child - 1)//2

    def delete():
        size = len(Innoskrit.minHeap)
        if size == 0:
            return -1
        element = Innoskrit.minHeap[0]
        Innoskrit.minHeap[0] = Innoskrit.minHeap[size - 1]
        Innoskrit.minHeap.pop()
        Innoskrit.heapify(0)
        return element
    
    def printHeap():
        print(Innoskrit.minHeap)

if __name__ == "__main__":
    Innoskrit.insert(98)
    Innoskrit.insert(87)
    Innoskrit.insert(86)
    Innoskrit.insert(44)
    Innoskrit.insert(40)
    Innoskrit.insert(32)
    Innoskrit.insert(33)
    Innoskrit.insert(20)
    Innoskrit.insert(21)
    print(Innoskrit.delete())
    Innoskrit.printHeap()
    Innoskrit.insert(100)
    Innoskrit.printHeap()