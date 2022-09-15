# Trees

[Trees](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)

## Structure
```
Node - A Tree node is a component which may contain its own values, and references to other nodes

Root - The root is the node at the beginning of the tree

K - A number that specifies the maximum number of children any node may have in a k-ary tree. In a binary tree, k = 2.

Left - A reference to one child node, in a binary tree

Right - A reference to the other child node, in a binary tree

Edge - The edge in a tree is the link between a parent and child node

Leaf - A leaf is a node that does not have any children

Height - The height of a tree is the number of edges from the root to the furthest leaf
```

## Traversals
Search for a node, print contents of a tree, + more
Two categories:

### Depth First
- prioritize going through the depth (height) first
  - pre-order
    - root>>left>>right
  - in-order
    - left>>root>>right
  - post-order
    - left>>right>>root
- store pops in a stack


### Breadth First
- output: abcdef
- store in a queue

### Binary Tree vs Knary Tree