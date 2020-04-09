class Node:
    def __init__(self, name, links, events, description):
        """
        __init__, all nodes have the attributes seen below
        @type self: Node
        @type name: str
        @type links: list
        @type description: str
        @type events: str
        @rtype: None
        >>Node32 = Node(name="Living_Room", links=[Node31, Node33], description="Contains: items", events="None")
        name = Living_Room
        links = room 32 - 33
        description: Contains: items
        events: None
        >>Node36 = Node(name="Backyard", links=36 , 37, description: contains: items, events: None)
        ERROR (links should be 'lst', description & events should be '=' not ':')
        """
        self.name = name
        self.links = links
        self.events = events
        self.description = description


Node1 = Node(name="Room.1", links=[], events="Event.1", description="Description.1")  # all nodes and details here
Node2 = Node(name="Room.2", links=[Node1], events="Event.2", description="Description.2")
Node1.links.append(Node2)  # done in order to add Node2 inside of Node1 links
Node3 = Node(name="Room.3", links=[Node2], events="Event.3", description="Description.3")
Node2.links.append(Node3)  # done in order to add Node3 inside of Node2 links
Node4 = Node(name="Room.4", links=[Node3], events="Event.4", description="Description.4")
Node3.links.append(Node4)  # done in order to add Node4 inside of Node3 links


nodes = [Node1, Node2, Node3, Node4]  # all nodes put in this list


class Maps:
    def __init__(self):
        """
        this function is the map that lays everything out and describes the position of the node
        @type self: Map
        @rtype: None
        """
        self.map = [1, 2, 3, 4]

    def create_linear(self):
        """
        this function makes a linear map where nodes and links are inputted in order. You cannot go back, only forward
        @type self: Map
        @rtype: linear map
        >>Maps.create_linear(nodes)
        Node1 = [__main__.Node2]
        Node2 = [__main__.Node1, __main__.Node3]
        Node3 = [__main__.Node2, __main__.Node4]
        Node4 = [__main__.Node3]
        >>Nodes.create_linear(nodes)
        ERROR ('Nodes' class does not have a function called 'create_linear')
        """
        if len(nodes) > 1:
            Node2.links.pop(0)
            Node3.links.pop(0)
            for i in range(len(nodes)):
                next = nodes[i]
                print(next.links)
                next.links = nodes[i+1]
        else:
            print("This linear map cannot be made because the map only consists of one/zero node(s).")

    def create_maze(self):
        """
        this function makes a maze map where nodes and links randomly inputted and you can go back and forward
        @type self: Map
        @rtype: maze map
        >>Maps.create_maze(nodes)
        Node1(Node2) <-> Node3(Node 4) <-> Node2(Node1) <-> Node4
        >>Nodes.create_maze(nodes)
        ERROR ('Nodes' class does not have a function called 'create_linear')
        """
        if len(nodes) > 1:
            input_next_or_last = input("next or last?: ")
            for i in range(len(nodes)):
                node_direction = nodes[i]
                if input_next_or_last == "next":
                    node_direction.links = nodes[i + 1]
                    print(node_direction.links)
                elif input_next_or_last == "last":
                    node_direction.links = nodes[i - 1]
                    print(node_direction.links)


print(Maps.create_linear(nodes))  # prints linear map
print(Maps.create_maze(nodes))  # prints maze map
