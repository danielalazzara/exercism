class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    
    def value(self):
        return self._value

    
    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._len = 0
        for value in values:
            self.push(value)

    
    def __len__(self):
        return self._len

    
    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    
    def push(self, value):
        self._head = Node(value, self._head)
        self._len += 1

    
    def pop(self):
        self._head, popped = self.head().next(), self.head()
        self._len -= 1
        return popped.value()

      
    def __iter__(self):
        cursor = self._head
        while cursor:
            yield cursor.value()
            cursor = cursor.next()


    def reversed(self):
        return LinkedList(self)


class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
        
