from typing import Optional, TypeVar, Generic, List

###############
# Binary Tree #
###############

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(
        self,
        value: Optional[T] = None,
        left: Optional["Node[T]"] = None,
        right: Optional["Node[T]"] = None
    ):
        self.left = left
        self.right = right
        self.value = value

class BinaryTree:
    def __init__(self, node: Optional[Node[float]] = None):
        self.root = node


def bfs_print_binary_tree(n: Node):
    q = []
    q.append(n)
    while len(q) != 0:
        new_node = q.pop(0)
        print(new_node.value)
        if new_node.left is not None:
            q.append(new_node.left)
        if new_node.right is not None:
            q.append(new_node.right)


def dfs_print_binary_tree(n: Node):
    print(n.value)
    if n.left is not None:
        dfs_print_binary_tree(n.left)
    if n.right is not None:
        dfs_print_binary_tree(n.right)


def binary_tree_builder() -> BinaryTree:
    return BinaryTree(
            Node(1,
                Node(2,
                     Node(3, None, None),
                     Node(7, None, None)
                    ),
                Node(4,
                     None,
                     Node(5,
                        Node(8,
                             Node(9, None, None),
                             None
                            ),
                        Node(6, None, None))
                    )
                )
        )


################
# General Tree #
################


class GeneralNode(Generic[T]):
    def __init__(
        self,
        value: Optional[T] = None,
        children: Optional[List["Node[T]"]] = None 
    ):
        self.value = value
        self.children = [] if children is None else children


class GeneralTree:
    def __init__(self, node: Optional[GeneralNode[float]] = None):
        self.root = node


def general_tree_print_dfs(n: GeneralNode):
    print(n.value)
    for child in n.children:
        general_tree_print_dfs(child)


def gen_tree_builder() -> GeneralTree:
    return GeneralTree(
        GeneralNode(1,
                    [
                        GeneralNode(2,
                            [GeneralNode(5, [])]
                        ),
                        GeneralNode(3,
                            [
                                GeneralNode(6, []),
                                GeneralNode(7, [])
                            ]
                        ),
                        GeneralNode(4,
                            []
                        )
                    ]
    ))


###############
#    Graph    #
###############

class GraphNode(Generic[T]):
    def __init__(
        self,
        value: Optional[T] = None,
        neighbors: Optional[List["Node[T]"]] = None
    ):
        self.value = value
        self.neighbors = neighbors


class Graph:
    def __init__(self, node: GraphNode):
        self.node = node

def graph_print_dfs(node: GraphNode[T]):
    print(node.value)
    visited = set([node])

    def dfs(node: GraphNode[T]):
        if node in visited:
            return
        visited.add(node)
        print(node.value)
        for neighbor in node.neighbors:
            dfs(neighbor)

    for node in node.neighbors:
        if node not in visited:
            dfs(node)



def graph_builder() -> Graph:
    return Graph(GraphNode(1, [GraphNode(2, [GraphNode(3, []), GraphNode(4, [GraphNode(5, [])])]), GraphNode(6, [])]))


def main():
    # Binary tree
    # bin_tree = binary_tree_builder()
    # bfs_print_binary_tree(bin_tree.root)
    # print()
    # dfs_print_binary_tree(bin_tree.root)

    # General tree
    # gen_tree = gen_tree_builder()
    # general_tree_print_dfs(gen_tree.root)

    # Graph
    g = graph_builder()
    graph_print_dfs(g.node)


if __name__ == "__main__":
    main()
