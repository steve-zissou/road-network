import random


'''Class to represent a road node'''
class Node:
    def _generate_node(self, x_max, y_max, z_max):
        x = '{:.1f}'.format(random.uniform(0, x_max))
        y = '{:.1f}'.format(random.uniform(0, y_max))
        z = '{:.1f}'.format(random.uniform(0, z_max))
        return [x, y, z]

    def __str__(self):
        return ','.join([self.x, self.y, self.z])

    def __init__(self, id, x_max=20, y_max=20, z_max=20):
        self.id = id
        self.x, self.y, self.z = self._generate_node(x_max, y_max, z_max)


def generate_road_network(node_count=5, x_max=20, y_max=20, z_max=20):
    nodes = []
    for index, item in enumerate(range(node_count)):
        nodes.append(Node(index))

    print(*nodes, sep='\n')

if __name__ == '__main__':
    generate_road_network(3)
