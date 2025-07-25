from collections import deque
import itertools

class State:
    def __init__(self, left, right, umbrella_side, time):
        self.left = left
        self.right = right
        self.umbrella = umbrella_side
        self.time = time
        self.parent = None

    def is_goal(self):
        return len(self.left) == 0 and self.umbrella == 'R'

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right and self.umbrella == other.umbrella and self.time == other.time

    def __hash__(self):
        return hash((tuple(sorted(self.left)), tuple(sorted(self.right)), self.umbrella, self.time))

    def __str__(self):
        return f"Left: {self.left}, Right: {self.right}, Umbrella: {self.umbrella}, Time: {self.time} min"

class Search:
    def __init__(self):
        self.times = {'Amogh': 5, 'Ameya': 10, 'Grandmother': 20, 'Grandfather': 25}

    def get_successors(self, state):
        successors = []
        if state.umbrella == 'L':
            for pair in itertools.combinations(state.left, 2):
                new_left = list(state.left)
                new_right = list(state.right)
                new_left.remove(pair[0])
                new_left.remove(pair[1])
                new_right += [pair[0], pair[1]]
                time_taken = max(self.times[pair[0]], self.times[pair[1]])
                new_state = State(new_left, new_right, 'R', state.time + time_taken)
                new_state.parent = state
                if new_state.time <= 60:
                    successors.append(new_state)
        else:
            for person in state.right:
                new_left = list(state.left)
                new_right = list(state.right)
                new_right.remove(person)
                new_left.append(person)
                time_taken = self.times[person]
                new_state = State(new_left, new_right, 'L', state.time + time_taken)
                new_state.parent = state
                if new_state.time <= 60:
                    successors.append(new_state)
        return successors

    def reconstruct_path(self, state):
        path = []
        while state:
            path.append(state)
            state = state.parent
        path.reverse()
        for step in path:
            print(step)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            current = queue.popleft()
            if current.is_goal():
                print("\nBFS Solution Path:")
                self.reconstruct_path(current)
                return
            visited.add(current)
            for successor in self.get_successors(current):
                if successor not in visited:
                    queue.append(successor)
        print("No solution found within 60 minutes using BFS.")

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            current = stack.pop()
            if current.is_goal():
                print("\nDFS Solution Path:")
                self.reconstruct_path(current)
                return
            visited.add(current)
            for successor in self.get_successors(current):
                if successor not in visited:
                    stack.append(successor)
        print("No solution found within 60 minutes using DFS.")




if __name__ == "__main__":
    initial_state = State(
        left=['Amogh', 'Ameya', 'Grandmother', 'Grandfather'],
        right=[],
        umbrella_side='L',
        time=0
    )
    search = Search()
    search.bfs(initial_state)
    search.dfs(initial_state)




## OUTPUT 

# BFS Solution Path:
# Left: ['Amogh', 'Ameya', 'Grandmother', 'Grandfather'], Right: [], Umbrella: L, Time: 0 min
# Left: ['Grandmother', 'Grandfather'], Right: ['Amogh', 'Ameya'], Umbrella: R, Time: 10 min
# Left: ['Grandmother', 'Grandfather', 'Amogh'], Right: ['Ameya'], Umbrella: L, Time: 15 min
# Left: ['Amogh'], Right: ['Ameya', 'Grandmother', 'Grandfather'], Umbrella: R, Time: 40 min
# Left: ['Amogh', 'Ameya'], Right: ['Grandmother', 'Grandfather'], Umbrella: L, Time: 50 min
# Left: [], Right: ['Grandmother', 'Grandfather', 'Amogh', 'Ameya'], Umbrella: R, Time: 60 min

# DFS Solution Path:
# Left: ['Amogh', 'Ameya', 'Grandmother', 'Grandfather'], Right: [], Umbrella: L, Time: 0 min
# Left: ['Grandmother', 'Grandfather'], Right: ['Amogh', 'Ameya'], Umbrella: R, Time: 10 min
# Left: ['Grandmother', 'Grandfather', 'Ameya'], Right: ['Amogh'], Umbrella: L, Time: 20 min
# Left: ['Ameya'], Right: ['Amogh', 'Grandmother', 'Grandfather'], Umbrella: R, Time: 45 min
# Left: ['Ameya', 'Amogh'], Right: ['Grandmother', 'Grandfather'], Umbrella: L, Time: 50 min
# Left: [], Right: ['Grandmother', 'Grandfather', 'Ameya', 'Amogh'], Umbrella: R, Time: 60 min

