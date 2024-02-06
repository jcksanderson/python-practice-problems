class Empty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())

    def inorder(self):
        return []


class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self

    def inorder(self):
        if self.is_leaf():
            return [self.value]
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()

    def add_to_all(self, num):
        tree = self
        tree.value += num
        if not tree.right.is_empty():
            tree.right.add_to_all(num)
        if not tree.left.is_empty():
            tree.left.add_to_all(num)
        return tree

    def path_to_list(self, num):
        if num == self.value:
            return [self.value]
        elif num < self.value and not self.left.is_empty():
            return [self.value] + self.left.path_to_list(num)
        elif num > self.value and not self.right.is_empty():
            return [self.value] + self.right.path_to_list(num)
        else:
            return []

    def path_to(self, num):
        list = self.path_to_list(num)
        return " ".join(str(x) for x in list)

if __name__ == "__main__":
    bst = Empty().insert(42).insert(10).insert(15).insert(63)

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
    print(f"The values in order are: {bst.inorder()}")
    bst_new = bst.add_to_all(1)
    print(f"New values: {bst_new.inorder()}")
    print(f"Path to 63: {bst.path_to(64)}")
