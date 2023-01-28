"""Practice problems for chapter 2 of Cracking the Coding Interview"""
from linkedlist import node
import random


def setup_ll(length=5, max=10):
    first = node(random.randint(0, max))
    cursor = first
    for _ in range(1, length):
        cursor.nextnode = node(random.randint(0, max))
        cursor = cursor.nextnode
    return first


def removedups(ll):
    if ll is None:
        return None

    ids = {ll.id}
    cursor = ll
    advance = ll.nextnode
    while advance is not None:
        if advance.id in ids:
            cursor.nextnode = advance.nextnode
        else:
            ids.add(advance.id)
            cursor = cursor.nextnode
        advance = advance.nextnode
    return ll


def removedups_nobuffer(ll):
    if ll is None:
        return None

    cursor = ll

    while cursor is not None:
        advance = cursor
        while advance.nextnode is not None:
            if advance.nextnode.id == cursor.id:
                advance.nextnode = advance.nextnode.nextnode
            else:
                advance = advance.nextnode
        cursor = cursor.nextnode
    return ll


def kthtolast(ll, k):
    if ll is None:
        return None

    cursor = ll
    for _ in range(k):
        cursor = cursor.nextnode

    trailing = ll
    while cursor is not None:
        cursor = cursor.nextnode
        trailing = trailing.nextnode

    return trailing.id


def deleteid(ll, id):
    if ll is None:
        return None

    cursor = ll
    while cursor.nextnode is not None:
        if cursor.nextnode.id == id:
            cursor.nextnode = cursor.nextnode.nextnode
        else:
            cursor = cursor.nextnode
    return ll


def deletemidnode(node):
    node.id = node.nextnode.id
    node.nextnode = node.nextnode.nextnode


def partitionll(ll, value):
    head = ll
    pivot = ll

    while pivot is not None and pivot.id < value:
        pivot = pivot.nextnode

    if pivot is None:
        return ll

    cursor = pivot
    while cursor.nextnode is not None:
        if cursor.nextnode.id < value:
            newhead = cursor.nextnode
            cursor.nextnode = cursor.nextnode.nextnode
            newhead.nextnode = head
            head = newhead
        else:
            cursor = cursor.nextnode
    return head


def sumlists(ll1, ll2):
    if ll1 is None:
        return ll2
    if ll2 is None:
        return ll1

    sum_ll_head = None
    carryover = 0
    while (ll1 is not None and ll2 is not None) or carryover > 0:
        digitsum = carryover
        if ll1 is not None:
            digitsum += ll1.id
        if ll2 is not None:
            digitsum += ll2.id
        carryover = digitsum // 10
        digitsum = digitsum % 10

        if sum_ll_head is None:
            sum_ll_head = node(digitsum)
            sum_ll_cursor = sum_ll_head
        else:
            sum_ll_cursor.nextnode = node(digitsum)
            sum_ll_cursor = sum_ll_cursor.nextnode
        if ll1 is not None:
            ll1 = ll1.nextnode
        if ll2 is not None:
            ll2 = ll2.nextnode

    if ll1 is None:
        sum_ll_cursor.nextnode = ll2
    if ll2 is None:
        sum_ll_cursor.nextnode = ll1

    return sum_ll_head


if __name__ == "__main__":
    # ll = setup_ll(10)
    # print(ll)

    # removedups_nobuffer(ll)
    # print(ll)

    # print(kthtolast(ll,10))

    # deletemidnode(ll.nextnode.nextnode.nextnode)

    # print(partitionll(ll, 5))

    ll1 = setup_ll(5)
    print(ll1)
    ll2 = setup_ll(5)
    print(ll2)
    print(sumlists(ll1, ll2))
