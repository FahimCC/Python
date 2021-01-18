import linked_list
from linked_list import *
ll = LinkedList()
ll.append(7)
ll.append(3)
ll.append(4)
ll.append(2)
ll.append(9)
print(ll)

ll.prepend(1)
ll.prepend(4)
print(ll)

print(ll.search(4))
ll.remove(4)
print(ll)

ll.insert(9, 10)
print(ll)
