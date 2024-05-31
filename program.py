import tkinter as tk
from tkinter import ttk
import pandas as pd

data = pd.read_csv('JioMart.csv')

class GreedySelectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Penerapan Algoritma Greedy")
        self.create_widgets()

    def create_widgets(self):
        self.budget_label = tk.Label(self.root, text="Masukkan Anggaran:")
        self.budget_label.pack()
        self.budget_entry = tk.Entry(self.root)
        self.budget_entry.pack()

        self.weight_label = tk.Label(self.root, text="Masukkan Bobot:")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.pack()

        self.budget_button = tk.Button(self.root, text="Simpan Anggaran", command=self.apply_budget_constraint)
        self.budget_button.pack()

        self.weight_button = tk.Button(self.root, text="Simpan Bobot", command=self.apply_weight_constraint)
        self.weight_button.pack()

        self.discount_button = tk.Button(self.root, text="Simpan Anggaran Diskon", command=self.apply_discount_constraint)
        self.discount_button.pack()

        self.tree = ttk.Treeview(self.root, columns=('Nama', 'Harga', 'Harga Diskon', 'Bobot', 'Tipe Barang'), show='headings')
        self.tree.heading('Nama', text='Nama Barang')
        self.tree.heading('Harga', text='Harga')
        self.tree.heading('Harga Diskon', text='Harga Diskon')
        self.tree.heading('Bobot', text='Bobot')
        self.tree.heading('Tipe Barang', text='Tipe Barang')
        self.tree.pack()

        self.total_label = tk.Label(self.root, text="")
        self.total_label.pack()

    def apply_budget_constraint(self):
        budget = float(self.budget_entry.get())
        filtered_data = data.sort_values(by='Harga')
        selected_items = []
        total_cost = 0
        total_discount_cost = 0
        total_weight = 0

        for _, row in filtered_data.iterrows():
            if total_cost + row['Harga'] <= budget:
                selected_items.append(row)
                total_cost += row['Harga']
                total_discount_cost += row['Harga Diskon']
                total_weight += row['Bobot']
        
        self.display_items(selected_items, total_cost, total_discount_cost, total_weight)

    def apply_weight_constraint(self):
        weight_limit = float(self.weight_entry.get())
        filtered_data = data.sort_values(by='Bobot')
        selected_items = []
        total_cost = 0
        total_discount_cost = 0
        total_weight = 0

        for _, row in filtered_data.iterrows():
            if total_weight + row['Bobot'] <= weight_limit:
                selected_items.append(row)
                total_cost += row['Harga']
                total_discount_cost += row['Harga Diskon']
                total_weight += row['Bobot']
        
        self.display_items(selected_items, total_cost, total_discount_cost, total_weight)

    def apply_discount_constraint(self):
        budget = float(self.budget_entry.get())
        filtered_data = data.sort_values(by='Harga Diskon')
        selected_items = []
        total_cost = 0
        total_discount_cost = 0
        total_weight = 0

        for _, row in filtered_data.iterrows():
            if total_discount_cost + row['Harga Diskon'] <= budget:
                selected_items.append(row)
                total_cost += row['Harga']
                total_discount_cost += row['Harga Diskon']
                total_weight += row['Bobot']
        
        self.display_items(selected_items, total_cost, total_discount_cost, total_weight)

    def display_items(self, items, total_cost, total_discount_cost, total_weight):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        for item in items:
            self.tree.insert('', tk.END, values=(item['Nama'], item['Harga'], item['Harga Diskon'], item['Bobot'], item['Tipe Barang']))
        
        self.total_label.config(text=f"Total Harga: {total_cost:.2f}, Total Harga Diskon: {total_discount_cost:.2f}, Total Bobot: {total_weight:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GreedySelectionApp(root)
    root.mainloop()
