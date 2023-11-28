class FSTState:
    def __init__(self):
        self.transitions = {}
        self.output = None
        self.is_final = False

class FST:
    def __init__(self):
        self.root = FSTState()
        self.states = {self.root}

    def insert_word(self, word, output):
        current = self.root
        for char in word:
            if char not in current.transitions:
                current.transitions[char] = FSTState()
            current = current.transitions[char]
        current.is_final = True
        current.output = output

    def find_minimized(self, state):
        for s in self.states:
            if s.transitions == state.transitions and s.output == state.output:
                return s
        self.states.add(state)
        return state

    def minimize_states(self, current, word, index):
        if index < len(word):
            char = word[index]
            if char in current.transitions:
                child_state = current.transitions[char]
                minimized_state = self.find_minimized(child_state)
                current.transitions[char] = minimized_state
                self.minimize_states(minimized_state, word, index + 1)

    def create_minimal_transducer(self, words, outputs):
        previous_word = ""
        for word, output in zip(words, outputs):
            common_prefix_len = len(os.path.commonprefix([previous_word, word]))
            self.minimize_states(self.root, previous_word, common_prefix_len)
            self.insert_word(word, output)
            previous_word = word
        self.minimize_states(self.root, previous_word, 0)