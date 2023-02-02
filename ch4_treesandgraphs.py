"""Problems from Chapter 4 of Cracking the Coding Interview"""

import dataclasses
import random
from collections import deque


@dataclasses.dataclass
class node:
    id: int
    visited: bool = False
    children: [] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class binarytree_node:
    id: int
    left: None = None
    right: None = None
    parent: None = None

    def isleaf(self):
        return self.left is None and self.right is None


def setupgraph():
    nodes = {}

    for i in range(26):
        char = chr(ord("A") + i)
        nodes[char] = node(char)

    nodes["S"].children.extend([nodes["A"], nodes["B"]])
    nodes["A"].children.extend([nodes["C"], nodes["D"]])
    nodes["B"].children.extend([nodes["E"]])
    nodes["C"].children.extend([nodes["A"], nodes["B"]])
    return nodes


def dfs(node, target, graph):
    print(f"Exploring {node.id}")
    node.visited = True
    if node.id == target:
        return True
    else:
        for node in graph[node.id].children:
            if not node.visited:
                if dfs(node, target, graph):
                    return True
    return False


def bfs(node, target, graph):
    tovisit = deque([node])
    while tovisit:
        visiting = tovisit.pop()
        visiting.visited = True
        if visiting.id == target:
            return True
        tovisit.extendleft(visiting.children)
    return False


def routebetweennodes(graph):
    return dfs(graph["S"], "E", graph)
    return bfs(graph["S"], "E", graph)


def insert_value(value, tree):
    if tree is None:
        return binarytree_node(value)
    else:
        cursor = tree
        while True:
            if value <= cursor.id:
                if cursor.left is None:
                    cursor.left = binarytree_node(value)
                    return tree
                else:
                    cursor = cursor.left
            else:
                if cursor.right is None:
                    cursor.right = binarytree_node(value)
                    return tree
                else:
                    cursor = cursor.right


# def minimalbst(nums, tree=None):
#     midindex = len(nums)//2
#     if nums:
#         tree = insert_value(nums[midindex], tree)
#         tree = minimalbst(nums[:midindex], tree)
#         tree = minimalbst(nums[midindex+1:], tree)
#     return tree


def minimalbst(nums):
    if not nums:
        return None
    else:
        midindex = len(nums) // 2
        tree = binarytree_node(nums[midindex])
        tree.left = minimalbst(nums[:midindex])
        tree.right = minimalbst(nums[midindex + 1:])
        return tree


def setup_binarytree_imbalanced():
    btn = binarytree_node
    return btn(5, btn(3, btn(2, btn(1))), btn(19))


def treedepth(tree):
    if tree is None:
        return 0
    left_depth = treedepth(tree.left)
    right_depth = treedepth(tree.right)
    return max(left_depth, right_depth) + 1


def checkbalanced(tree):
    if tree is None or tree.isleaf():
        return True

    if tree.left is not None:
        if tree.left.isleaf() is False and tree.right is None:
            return False
    if tree.right is not None:
        if tree.right.isleaf() is False and tree.left is None:
            return False

    return checkbalanced(tree.left) and checkbalanced(tree.right)


def is_bst(tree):
    if tree is None:
        return True

    if tree.left is not None and tree.left.id > tree.id:
        return False
    if tree.right is not None and tree.right.id < tree.id:
        return False

    return is_bst(tree.left) and is_bst(tree.right)


def find_smallest(tree):
    if tree is None:
        raise Exception("Don't look for what doesn't exist")
    if tree.left is None:
        return tree.id

    return find_smallest(tree.left)


def find_node(tree, value):
    # cursor = tree
    # while cursor is not None:
    #     if cursor.id == value:
    #         return cursor
    #     if cursor.id > value:
    #         cursor = cursor.left
    #     else:
    #         cursor = cursor.right
    # return cursor

    if tree is None or tree.id == value:
        return tree
    if value < tree.id:
        return find_node(tree.left, value)
    else:
        return find_node(tree.right, value)


def find_successor(tree, value):
    target_node = find_node(tree, value)
    if target_node is None:
        raise Exception("Get better trees")

    if (
        target_node.right is None and
        target_node.parent is not None and
        target_node.parent.id > value
    ):
        return target_node.parent.id

    return find_smallest(target_node.right)


def generate_bst_withparents():
    btn = binarytree_node
    tree = btn(5, btn(3), btn(17))
    tree.left.parent = tree
    tree.right.parent = tree
    cursor = tree.right
    cursor.left = btn(11)
    cursor.right = btn(23)
    cursor.left.parent = cursor
    cursor.right.parent = cursor
    return tree


if __name__ == "__main__":
    # graph = setupgraph()
    # print(routebetweennodes(graph))

    # randomnums = sorted([random.randint(1, 50) for _ in range(11)])
    # print(randomnums)
    # print(minimalbst(randomnums))
    # print(checkbalanced(minimalbst(randomnums)))
    # print(checkbalanced(setup_binarytree_imbalanced()))

    # print(is_bst(setup_binarytree_imbalanced()))

    tree = generate_bst_withparents()
    print(find_successor(tree, 22))
