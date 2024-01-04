#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        dis = ""
        position = self.head
        while position:
            dis = dis + str(position.data) + "\n"
            position = position.next_node
        return dis[:-1]

    def sorted_insert(self, value):
        hold = Node(value)
        if not self.head:
            self.head = hold
        if value < self.head.data:
            hold.next_node = self.head
            self.head = hold
            return
        position = self.head
        while position.next_node and position.next_node.data < value:
            position = position.next_node
        if position.next_node:
            hold.next_node = position.next_node
        position.next_node = hold
