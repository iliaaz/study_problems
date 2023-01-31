"""Problems from Chapter 4 of Cracking the Coding Interview"""

import dataclasses
import random
from collections import deque


@dataclasses.dataclass
class node:
    """a node"""

    id: int
    visited: bool = False
    children: [] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class binarytree_node:
    """a node"""

    id: int
    left: None = None
    right: None = None


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


# def minimaltree(nums, tree=None):
#     midindex = len(nums)//2
#     if nums:
#         tree = insert_value(nums[midindex], tree)
#         tree = minimaltree(nums[:midindex], tree)
#         tree = minimaltree(nums[midindex+1:], tree)
#     return tree


def minimaltree(nums):
    if not nums:
        return None
    else:
        midindex = len(nums) // 2
        tree = binarytree_node(nums[midindex])
        tree.left = minimaltree(nums[:midindex])
        tree.right = minimaltree(nums[midindex + 1 :])
        return tree


if __name__ == "__main__":
    # graph = setupgraph()
    # print(routebetweennodes(graph))

    randomnums = sorted([random.randint(1, 50) for _ in range(11)])
    print(randomnums)
    print(minimaltree(randomnums))
