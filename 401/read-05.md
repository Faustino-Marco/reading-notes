# Linked Lists

## Read

### [Big O: Analysis of Algorithm Efficiency](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/big_oh.html)
  - Running Time (efficiency/complexity)
  - Memory Space (amt of mem resources used to store data & instructions)
  - Worst case efficiency
    - Big O is for max time / space
  - 4 Key Areas for analysis
    - Input Size
      - `n`
        - higher > increase run time/mem
    - Units of Measurement
      - milliseconds
        - may vary by machine
      - number of operations
        - how many lines of code
      - number of "Basic Operations"
        - ref to the op that contributes the most to the total run time
        - usually the most time consuming op within the inner most loop
        - SPACE
          - code
            - num of bytes for chars in fn
          - input data
            - or additional mem
          - output
            - space needed
              - working space / stack space
    - Orders of Growth

![Orders of Growth](./img/OrdersOfGrowth.png) 

    - Best, Worst, Avg Case Scenarios
      - Big O: worst
      - Big Omega: Best
      - Big Theta: Avg 

### [Linked Lists](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html)
  - linked list
    - data structure that contains nodes that links/points to the next node in the list
  - singly
    - ref to num refs the node has
    - only one ref
  - doubly
    - 2 refs
      - next and previous
  - node
    - individual items/links contained
  - next
    - ref to next node
  - head
    - ref to first node in linked list
  - current
    - ref to node currently being looked at
  - no for or foreach loops
  - best approach: while loop
  - continually check node != null
  - traversing
  - end of list: current node == null
  - O(N) to add
    - unless add to head
  - then reassign head
  - edit linked list using nodes and links and where they point
  - When making Node class, consider requiring a value to be passed in to require that each node has a value.

### [What's a Linked List, Anyway? pt1](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)
  - linear data structure
  - like hopscotch
  - must go through list sequentially to get to n
  - arrays are static
  - linked lists can be dynamic(scattered bytes as long as they're linked)
  - nodes
    - start at head
    - end node points to null
    - when changing can just change ref to next node as oppposed to rewriting all
    - singly/doubly linked
      - next vs next & prev
    - circular

### [What's a Linked List, Anyway? pt2](https://medium.com/basecs/whats-a-linked-list-anyway-part-2-131d96f71996)
  - big O is all about the way algo grows with time
    - express how quickly runtime grows
  - space time complexities
    - O(N) etc
  - Growing a linked list
    - make new node
    - set pointer to current first node
    - reset head to point to new node
    - can repeat anywhere in sequence
  - efficient for adding/removing elements, very slow to search/find e's
![Linked List T Chart](./img/linked-list-T-chart.jpeg)

