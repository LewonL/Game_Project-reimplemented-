import time
from Event_Class import *


class Node:
    def __init__(self, name, next_link, events, description):
        """
        __init__, all nodes have the attributes seen below
        @type self: Node
        # @type name: str
        @type next_link: list
        # @type description: str
        @type events: str
        @rtype: None
        >>Node32 = Node(name="Living_Room", next_link=[Node31, Node33], description="Contains: items", events="None")
        name = Living_Room
        next_link = room 32 - 33
        description: Contains: items
        events: None
        >>Node36 = Node(name="Backyard", next_link=36 , 37, description: contains: items, events: None)
        ERROR (next_link should be 'lst', description & events should be '=' not ':')
        """
        self.name = name
        self.next_link = next_link
        self.events = events
        self.description = description


Node1 = Node(name="Room.1", next_link=[], events="Event", description="Description")  # all nodes and details here
Node2 = Node(name="Room.2", next_link=[], events="Event", description="Description")
Node1.next_link.append(Node2)  # done in order to add Node2 inside of Node1 next_link
Node3 = Node(name="Room.3", next_link=[], events="Event", description="Description")
Node2.next_link.append(Node3)  # done in order to add Node3 inside of Node2 next_link
Node4 = Node(name="Room.4", next_link=[], events="Event", description="Description")
Node3.next_link.append(Node4)  # done in order to add Node4 inside of Node3 next_link
Node5 = Node(name="Room.5", next_link=[], events="Event", description="Description")
Node4.next_link.append(Node5)  # done in order to add Node5 inside of Node4 next_link
Node6 = Node(name="Room.6", next_link=[], events="Event", description="Description")
Node5.next_link.append(Node6)  # done in order to add Node6 inside of Node5 next_link
Node7 = Node(name="Room.7", next_link=[], events="Event", description="Description")
Node6.next_link.append(Node7)  # done in order to add Node7 inside of Node6 next_link
Node8 = Node(name="Room.8", next_link=[], events="Event", description="Description")
Node7.next_link.append(Node8)  # done in order to add Node8 inside of Node7 next_link
Node9 = Node(name="Room.9", next_link=[], events="Event", description="Description")
Node8.next_link.append(Node9)  # done in order to add Node9 inside of Node8 next_link
Node10 = Node(name="Room.10", next_link=[], events="Event", description="Description")
Node9.next_link.append(Node10)  # done in order to add Node10 inside of Node9 next_link

nodes = [Node1, Node2, Node3, Node4, Node5, Node6, Node7, Node8, Node9, Node10]


def create_linear():
    """
    this function makes a maze map where nodes and next_link randomly inputted and you can go back and forward
    @type self: Map
    @rtype: maze map
    >>Maps.create_maze(nodes)
    Node1(Node2) <-> Node3(Node 4) <-> Node2(Node1) <-> Node4
    >>Nodes.create_maze(nodes)
    ERROR ('Nodes' class does not have a function called 'create_linear')
    """
    if len(nodes) > 1:
        map_end = True
        n = nodes.pop(0)
        while map_end:
            input_next = input("\ntype ('next'): ")
            if n == Node10:
                print("You have reached the final room... And from there, you see the exit...")
                map_end = False
            elif input_next == "next":
                nnl = n.next_link.pop(0)
                print(nnl.name)
                ev.event_call()
                n = nnl
            else:
                print("Invalid decision.\n")
