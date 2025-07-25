
class State:
    def __init__(self, config):
        self.config = config  
        self.blank = self.config.index('_')  

    def goalTest(self):
        return self.config == "WWW_EEE"

    def moveGen(self):
        children = []
        config = list(self.config)
        for i in range(len(config)):
            if config[i] == 'E':
                # E moves right
                if i+1 < 7 and config[i+1] == '_':
                    new_config = config[:]
                    new_config[i], new_config[i+1] = new_config[i+1], new_config[i]
                    children.append(State(''.join(new_config)))
                elif i+2 < 7 and config[i+2] == '_' and config[i+1] == 'W':
                    new_config = config[:]
                    new_config[i], new_config[i+2] = new_config[i+2], new_config[i]
                    children.append(State(''.join(new_config)))
            elif config[i] == 'W':
                # W moves left
                if i-1 >= 0 and config[i-1] == '_':
                    new_config = config[:]
                    new_config[i], new_config[i-1] = new_config[i-1], new_config[i]
                    children.append(State(''.join(new_config)))
                elif i-2 >= 0 and config[i-2] == '_' and config[i-1] == 'E':
                    new_config = config[:]
                    new_config[i], new_config[i-2] = new_config[i-2], new_config[i]
                    children.append(State(''.join(new_config)))
        return children

    def __eq__(self, other):
        return self.config == other.config

    def __hash__(self):
        return hash(self.config)

    def __str__(self):
        return self.config


class Search:
    def removeSeen(self, children, open, closed):
        open_nodes = [node for node, parent in open]
        closed_nodes = [node for node, parent in closed]
        return [node for node in children if node not in open_nodes and node not in closed_nodes]

    def reconstructPath(self, node_pair, closed):
        path = []
        node, parent = node_pair
        parent_map = {node: parent for node, parent in closed}
        path.append(node)
        while parent is not None:
            path.insert(0, parent)
            parent = parent_map.get(parent)
        print("->".join([str(n) for n in path]))
        return path

    def bfs(self, start):
        open = [(start, None)]
        closed = []
        while open:
            node_pair = open.pop(0)
            node, parent = node_pair
            if node.goalTest():
                print("Goal found")
                return self.reconstructPath(node_pair, closed)
            else:
                closed.append(node_pair)
                children = node.moveGen()
                new_nodes = self.removeSeen(children, open, closed)
                open.extend([(child, node) for child in new_nodes])
        print("Goal not found")

    def dfs(self, start):
        open = [(start, None)]
        closed = []
        while open:
            node_pair = open.pop()
            node, parent = node_pair
            if node.goalTest():
                print("Goal found")
                return self.reconstructPath(node_pair, closed)
            else:
                closed.append(node_pair)
                children = node.moveGen()
                new_nodes = self.removeSeen(children, open, closed)
                open.extend([(child, node) for child in new_nodes])
        print("Goal not found")


start_config = "EEE_WWW"
start_state = State(start_config)
search = Search()

print("BFS Path:")
search.bfs(start_state)

print("\nDFS Path:")
search.dfs(start_state)


## OUPUT


# BFS Path:
# Goal found
# EEE_WWW->EE_EWWW->EEWE_WW->EEWEW_W->EEW_WEW->E_WEWEW->_EWEWEW->WE_EWEW->WEWE_EW->WEWEWE_->WEWEW_E->WEW_WEE->W_WEWEE->WW_EWEE->WWWE_EE->WWW_EEE

# DFS Path:
# Goal found
# EEE_WWW->EEEW_WW->EE_WEWW->E_EWEWW->EWE_EWW->EWEWE_W->EWEWEW_->EWEW_WE->EW_WEWE->_WEWEWE->W_EWEWE->WWE_EWE->WWEWE_E->WWEW_EE->WW_WEEE->WWW_EEE