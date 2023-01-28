"""Sample implementation of a linked list node"""
from dataclasses import dataclass


@dataclass()
class node:
    id: int
    nextnode: None = None
    prevnode: None = None


# class node:
#     def __init__(self, id):
#         self.id = id
#         self.nextnode = None


#     def getid(self):
#         return self.id


def linklist():
    ll = node(1, nextnode=node(2, nextnode=node(3)))
    return ll


if __name__ == "__main__":
    ll = linklist()
    pointer = ll
    while pointer is not None:
        print(pointer.getid())
        pointer = pointer.nextnode
