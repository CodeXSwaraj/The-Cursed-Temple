import tkinter as tk
from tkinter import messagebox

class TempleGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The Cursed Temple")

        self.game_state = {
            "player_health": 100,
            "player_location": "entrance",
            "inventory": [],
            "game_over": False
        }

        self.temple_layout = {
            "entrance": {
                "description": "You are standing at the entrance of the temple.",
                "exits": ["hallway"],
                "items": ["torch"]
            },
            "hallway": {
                "description": "You are in a long, dark hallway.",
                "exits": ["entrance", "chamber"],
                "items": []
            },
            "chamber": {
                "description": "You are in a grand chamber with a large stone door.",
                "exits": ["hallway", "treasury"],
                "items": ["key"]
            },
            "treasury": {
                "description": "You are in a room filled with treasure.",
                "exits": ["chamber"],
                "items": ["gold"]
            }
        }

        self.location_label = tk.Label(self.root, text="", wraplength=400)
        self.location_label.pack()

        self.exits_label = tk.Label(self.root, text="Exits:")
        self.exits_label.pack()

        self.exits_listbox = tk.Listbox(self.root)
        self.exits_listbox.pack()

        self.items_label = tk.Label(self.root, text="Items:")
        self.items_label.pack()

        self.items_listbox = tk.Listbox(self.root)
        self.items_listbox.pack()

        self.inventory_label = tk.Label(self.root, text="Inventory:")
        self.inventory_label.pack()

        self.inventory_listbox = tk.Listbox(self.root)
        self.inventory_listbox.pack()

        self.health_label = tk.Label(self.root, text="Health: 100")
        self.health_label.pack()

        self.command_entry = tk.Entry(self.root)
        self.command_entry.pack()

        self.command_button = tk.Button(self.root, text="Enter", command=self.handle_input)
        self.command_button.pack()

        self.update_game_state()

    def update_game_state(self):
        self.location_label.config(text=self.temple_layout[self.game_state["player_location"]]["description"])
        self.exits_listbox.delete(0, tk.END)
        for exit in self.temple_layout[self.game_state["player_location"]]["exits"]:
            self.exits_listbox.insert(tk.END, exit)
        self.items_listbox.delete(0, tk.END)
        for item in self.temple_layout[self.game_state["player_location"]]["items"]:
            self.items_listbox.insert(tk.END, item)
        self.inventory_listbox.delete(0, tk.END)
        for item in self.game_state["inventory"]:
            self.inventory_listbox.insert(tk.END, item)
        self.health_label.config(text=f"Health: {self.game_state['player_health']}")

    def handle_input(self):
        command = self.command_entry.get()
        self.command_entry.delete(0, tk.END)

        if command.startswith("go "):
            direction = command[3:]
            if direction in self.temple_layout[self.game_state["player_location"]]["exits"]:
                self.game_state["player_location"] = direction
            else:
                messagebox.showinfo("Error", "You can't go that way.")
        elif command.startswith("take "):
            item = command[5:]
            if item in self.temple_layout[self.game_state["player_location"]]["items"]:
                self.game_state["inventory"].append(item)
                self.temple_layout[self.game_state["player_location"]]["items"].remove(item)
            else:
                messagebox.showinfo("Error", "You can't take that.")
        elif command == "quit":
            self.game_state["game_over"] = True
            self.root.quit()
        else:
            messagebox.showinfo("Error", "Invalid command.")

        self.update_game_state()

        if self.game_state["player_location"] == "treasury":
            messagebox.showinfo("Congratulations", "You have reached the treasury!")
            self.game_state["game_over"] = True
            self.root.quit()

        if self.game_state["player_health"] <= 0:
            messagebox.showinfo("Game Over", "You have died. Game over.")
            self.game_state["game_over"] = True
            self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TempleGame()
    game.run()