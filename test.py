"""Class and functions to generate a connected road network."""
import random


class Connection:
    """Class to represent a connection between nodes."""

    def __init__(self, start, end):
        """Create a Connection.

        Keyword arguments:
        start -- the start node id
        end -- the end node id
        """
        self.start = start
        self.end = end

    def __str__(self):
        """Get the string representation of the connection."""
        return '{},{}'.format(self.start, self.end)


class Node:
    """Class to represent a road node."""

    def __str__(self):
        """Get the string representation of the node."""
        return '{:.2f},{:.2f},{:.2f}'.format(self.x, self.y, self.z)

    def __init__(self, id, x, y, z):
        """Create a Node.

        Keyword arguments:
        id -- the node identifier
        x -- the x co-ordinate of the node
        y -- the y co-ordinate of the node
        z -- the z co-ordinate of the node
        """
        self.id = id
        self.x = x
        self.y = y
        self.z = z


def generate_road_nodes(node_count=5, x_max=20, y_max=20, z_max=20):
    """Generate road nodes of the specified size.

    Keyword arguments:
    node_count -- the number of nodes to create (default 5)
    x_max -- the maximum x value for a node (default 20)
    y_max -- the maximum y value for a node (default 20)
    z_max -- the maximum z value for a node (default 20)
    """
    nodes = []
    for index, item in enumerate(range(node_count)):
        x = random.uniform(0, x_max)
        y = random.uniform(0, y_max)
        z = random.uniform(0, z_max)
        nodes.append(Node(index, x, y, z))

    return nodes


def generate_road_connections(nodes, connection_count=5):
    """Generate road connections for the given nodes.

    Keyword arguments:
    nodes -- the road nodes
    connection_count -- the number of node connections to create (default 5)
    """
    node_ids = list(map(lambda node: node.id, nodes))

    if (connection_count > len(nodes)):
        connection_count = len(nodes)

    elif (connection_count < 0):
        connection_count = 0

    starts = random.sample(node_ids, connection_count)
    ends = random.sample(node_ids, connection_count)
    groups = zip(starts, ends)

    return list(map(lambda x: Connection(*x), groups))


def generate_road_network(node_count=5, x_max=20, y_max=20, z_max=20):
    """Generate a road network of the specified size.

    Keyword arguments:
    node_count -- the number of nodes to create (default 5)
    x_max -- the maximum x value for a node (default 20)
    y_max -- the maximum y value for a node (default 20)
    z_max -- the maximum z value for a node (default 20)
    """
    nodes = generate_road_nodes(node_count, x_max, y_max, z_max)
    connections = generate_road_connections(nodes)

    print(*nodes, sep='\n')
    print(*connections, sep='\n')


if __name__ == '__main__':
    generate_road_network()
