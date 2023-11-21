# Some Heap Methods

This is an implementation of some heap methods. Here is each with a description

## The Min Heap Class

A heap is a data structure which combines the structure of a list and a binary tree with some extra conditions.

In particular, every node in the tree corresponds to an index in the list, and the parent of the item in position n is in position (n-1)/2 or (n-2)/2.

Furthermore, the value of a child must be greater than or equal to the value of its parent.

We save and maintain the heap as a list.

##

### Parent and Children Methods

These are class methods that tell for a given index what the parent and child index values are. The children method requires a list length.

##

### Heap Append

Adds a new item to the heap by putting it at the end of the heap. We repeatedly swap the place of this value with its parent until it is smaller than the value at its parent node.

##

### Heap Pop

Returns the smallest item from the top of the heap. Before returning, it also modifies the heap: first it removes the last value in the heap and moves it to the top; call this the terminal value. If the terminal value finds it has a smaller child, we swap places with its smallest child, and repeat this until it cannot be swapped with a smaller child.

##

### Heap Initialize

This takes an array of integers and initializes by heap appending one at a time.

##

### Heap Sort

This takes a heap and sorts it by heap popping its items one at a time, and saving the result as to a new list. Then the ordered list is saved as the heap's list.

##

#### Test Data

To test we create a random list of integers and sort them.