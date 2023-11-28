class FSTState:
    def __init__(self, id):
        self.id = id
        self.transitions = {}
        self.outputs = {}
        self.is_final = False

class FST:
    def __init__(self):
        self.next_state_id = 0
        self.root = self.create_state()
        self.states = {self.root.id: self.root}

    def create_state(self):
        state = FSTState(self.next_state_id)
        self.next_state_id += 1
        return state

    def insert_word(self, word, output):
        current = self.root
        for char in word:
            if char not in current.transitions:
                next_state = self.create_state()
                self.states[next_state.id] = next_state
                current.transitions[char] = next_state.id
                current.outputs[char] = output
            else:
                current.outputs[char] = min(current.outputs[char], output)
            current = self.states[current.transitions[char]]
        current.is_final = True

    def minimize(self):
        # Placeholder for the minimize algorithm
        # This should be replaced with the actual minimization code
        pass