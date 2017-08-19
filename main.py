import linkedlist
import element

e1 = element.Element(5)
e2 = element.Element(10)
e3 = element.Element(15)

list = linkedlist.LinkedList(e1)
list.append(e2)
list.append(e3)

list.delete(15)

print list.get_position(3).value