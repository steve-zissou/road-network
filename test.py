"""Class and functions to generate a connected road network."""
import random


class Node:
    """Class to represent a road node."""

    def _generate_node(self, x_max, y_max, z_max):
        x = '{:.1f}'.format(random.uniform(0, x_max))
        y = '{:.1f}'.format(random.uniform(0, y_max))
        z = '{:.1f}'.format(random.uniform(0, z_max))
        return [x, y, z]

    def __str__(self):
        """Get the string representation of the node."""
        return ','.join([self.x, self.y, self.z])

    def __init__(self, id, x_max=20, y_max=20, z_max=20):
        """Create a Node.

        Keyword arguments:
        x_max -- the maximum x value for a node (default 20)
        y_max -- the maximum y value for a node (default 20)
        z_max -- the maximum z value for a node (default 20)
        """
        self.id = id
        self.x, self.y, self.z = self._generate_node(x_max, y_max, z_max)


def generate_road_network(node_count=5, x_max=20, y_max=20, z_max=20):
    """Generate a road network of the specified size.

    Keyword arguments:
    node_count -- the real part (default 5)
    x_max -- the maximum x value for a node (default 20)
    y_max -- the maximum y value for a node (default 20)
    z_max -- the maximum z value for a node (default 20)
    """
    nodes = []
    for index, item in enumerate(range(node_count)):
        nodes.append(Node(index))

    print(*nodes, sep='\n')


if __name__ == '__main__':
    generate_road_network(3)
