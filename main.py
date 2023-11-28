import tkinter as tk
from tkinter import Listbox, Entry, Label, Frame
import time
import tracemalloc
import fst
import trie

class AutocompleteApplication:
    def __init__(self, master):
        self.master = master
        self.setup_ui()
        self.fst = fst.FST()
        self.trie = trie.Trie()
        self.load_dictionary('./dicionario/words.txt')

    def setup_ui(self):
        Label(self.master, text="Digite o Prefixo:").pack()
        self.input_entry = Entry(self.master)
        self.input_entry.pack()
        self.input_entry.bind('<KeyRelease>', self.on_keyrelease)

        self.fst_frame = Frame(self.master)
        self.fst_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.trie_frame = Frame(self.master)
        self.trie_frame.pack(side=tk.LEFT, padx=10, pady=10)

        Label(self.fst_frame, text="FST Autocomplete:").pack()
        self.fst_listbox = Listbox(self.fst_frame)
        self.fst_listbox.pack()

        Label(self.trie_frame, text="Trie Autocomplete:").pack()
        self.trie_listbox = Listbox(self.trie_frame)
        self.trie_listbox.pack()

        self.fst_stats_label = Label(self.fst_frame, text="")
        self.fst_stats_label.pack()

        self.trie_stats_label = Label(self.trie_frame, text="")
        self.trie_stats_label.pack()

    def on_keyrelease(self, event):
        prefix = self.input_entry.get()
        self.perform_autocomplete(prefix, self.fst, self.fst_listbox, self.fst_stats_label)
        self.perform_autocomplete(prefix, self.trie, self.trie_listbox, self.trie_stats_label)

    def perform_autocomplete(self, prefix, structure, listbox, stats_label):
        tracemalloc.start()
        start_time = time.time()

        suggestions = structure.autocomplete(prefix)

        elapsed_time = time.time() - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        listbox.delete(0, tk.END)
        for suggestion in suggestions:
            listbox.insert(tk.END, suggestion)

        stats_label.config(text=f"Tempo: {elapsed_time:.6f} s \n Memória: {current / 10**6:.6f} MB \n (Pico: {peak / 10**6:.6f} MB)")

    def load_dictionary(self, path):
        with open(path, 'r') as file:
            words = file.read().splitlines()
        for word in words:
            self.fst.insert_word(word)
            self.trie.insert_word(word)

def main():
    root = tk.Tk()
    root.title("Autocomplete Comparação")
    app = AutocompleteApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
