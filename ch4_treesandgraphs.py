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


def inorder_traversal(tree):
    if tree is None:
        return []
    else:
        left_tree = inorder_traversal(tree.left)
        right_tree = inorder_traversal(tree.right)
        return left_tree + [tree.id] + right_tree


def preorder_traversal(tree):
    if tree is None:
        return []
    else:
        left_tree = preorder_traversal(tree.left)
        right_tree = preorder_traversal(tree.right)
        return [tree.id] + left_tree + right_tree


def postorder_traversal(tree):
    if tree is None:
        return []
    else:
        left_tree = postorder_traversal(tree.left)
        right_tree = postorder_traversal(tree.right)
        return left_tree + right_tree + [tree.id]


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
    """
                                    5
                                  /   \
                                 3     19
                                / \
                               2   17
                              /   /
                             1   4
    """
    btn = binarytree_node
    return btn(5, btn(3, btn(2, btn(1)), btn(17, btn(4))), btn(19))


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


def buildorder(projects, dependancies):
    """ Dependancies:
    Inputs: {'A': ['E', 'C'], 'B': ['C'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
    Outputs: {'A': [], 'B': [], 'C': ['B', 'A'], 'D': [], 'E': ['A'], 'F': ['C']}
    """
    dependancy_inputs = {}
    dependancy_outputs = {}
    for project in projects:
        dependancy_inputs[project] = []
        dependancy_outputs[project] = []
    for dependancy in dependancies:
        dependancy_inputs[dependancy[1]].append(dependancy[0])
        dependancy_outputs[dependancy[0]].append(dependancy[1])

    buildorder = []
    cyclic = False
    print(dependancy_inputs)
    print(dependancy_outputs)
    while not cyclic and dependancy_inputs:
        cyclic = True
        freeprojects = []
        for project, dependancies in dependancy_inputs.items():
            if not dependancies:
                cyclic = False
                freeprojects.append(project)
                buildorder.append(project)
        for freeproject in freeprojects:
            del dependancy_inputs[freeproject]
            for project in dependancy_outputs[freeproject]:
                dependancy_inputs[project].remove(freeproject)
    if cyclic:
        return []
    return buildorder


def find_paths(tree, value1, value2):
    path1 = None
    path2 = None
    tovisit = deque()
    tovisit.append((tree, []))
    while tovisit and (path1 is None or path2 is None):
        visiting = tovisit.pop()
        # print(visiting)
        if visiting[0] is not None:
            if visiting[0].id == value1:
                path1 = visiting[1] + [value1]
            elif visiting[0].id == value2:
                path2 = visiting[1] + [value2]
            leftnodetovisit = (visiting[0].left, visiting[1] + [visiting[0].id])
            rightnodetovisit = (visiting[0].right, visiting[1] + [visiting[0].id])
            tovisit.extendleft([leftnodetovisit, rightnodetovisit])
    return path1, path2


def lastcommonality(path1, path2):
    # [5, 3, 2, 1]
    # [5, 3, 17, 4, 8, 9, 27]
    set1 = set(path1)
    for node in reversed(path2):
        if node in set1:
            return node
    return None


def firstcommonancestor(tree, value1, value2):
           #      5
           #     / \
           #   11   7
           #  /  \
           # 3   13
           #    /  \
           #   2    1
    if tree is None:
        raise Exception("A tree of at least two nodes is required.")

    path1, path2 = find_paths(tree, value1, value2)
    if not (path1 and path2):
        raise Exception("A value does not have a path")
    return lastcommonality(path1, path2)
    

def bst_sequences(tree):
           #      11
           #     / \
           #    7   17
           #  /  \
           # 3    9
           #    /  \
           #   8    10

# [[3,8,10,17], [7,9], [11]]
    pass


def preorder_traversal(tree):
    if tree is None:
        return ["X"]
    else:
        left_tree = preorder_traversal(tree.left)
        right_tree = preorder_traversal(tree.right)
        return [str(tree.id)] + left_tree + right_tree


def check_subtree(tree1, tree2):
    tree1_traversal = preorder_traversal(tree1)
    tree2_traversal = preorder_traversal(tree2)
    return "".join(tree2_traversal) in "".join(tree1_traversal)


def tree_match(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif tree1 is None or tree2 is None:
        return False
    elif tree1.id != tree2.id:
        return False
    else:
        return tree_match(tree1.left, tree2.left) and tree_match(tree1.right, tree2.right)


def check_subtree_alt(tree1, tree2):
    if tree1 is None:
        return False
    elif tree1.id == tree2.id and tree_match(tree1, tree2):
        return True
    else:
        return check_subtree_alt(tree1.left, tree2) or check_subtree_alt(tree1.right, tree2)


def pathswithsum(tree, value):
    pathsums = []
    tovisit = deque()
    tovisit.append((tree,[]))
    while tovisit:
        visiting = tovisit.pop()
        path = [val + visiting[0].id for val in visiting[1]]
        path.append(visiting[0].id)
        pathsums.extend(path)
        if visiting[0].left is not None:
            tovisit.append((visiting[0].left, path))
        if visiting[0].right is not None:
            tovisit.append((visiting[0].right, path))
    return pathsums.count(value)


if __name__ == "__main__":
    # graph = setupgraph()
    # print(routebetweennodes(graph))

    randomnums = sorted([random.randint(1, 50) for _ in range(11)])
    bst = minimalbst(randomnums)
    # print(randomnums)
    # print(minimalbst(randomnums))
    # print(checkbalanced(minimalbst(randomnums)))
    # print(checkbalanced(setup_binarytree_imbalanced()))

    # print(is_bst(setup_binarytree_imbalanced()))

    # tree = generate_bst_withparents()
    # print(find_successor(tree, 22))

    # projects = ["A", "B", "C", "D", "E", "F", "H"]
    # dependancies = [("E", "A"), ("C", "B"), ("C", "A"), ("F", "C"), ("C", "E"), ("F", "D")]
    # print(buildorder(projects, dependancies))
    
    # binarytree = setup_binarytree_imbalanced()
    # print(firstcommonancestor(binarytree, 1, 5))
    
    # print(inorder_traversal(bst))
    # print(preorder_traversal(bst))
    # print(postorder_traversal(bst))

    tree1 = setup_binarytree_imbalanced()
    btn = binarytree_node
    tree2 = btn(17, btn(4))
    # tree2 = btn(17, None, btn(4))
    # print(check_subtree(tree1, tree2))
    # print(check_subtree_alt(tree1, tree2))

    print(pathswithsum(tree1, 5))
