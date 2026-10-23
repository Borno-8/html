# Stationery Order Management App
 
# Import tkinter for GUI and ttk for improved widgets
import tkinter as tk
from tkinter import ttk, messagebox
 
 
# Define the StationeryOrderManagement class
class StationeryOrderManagement:
 
    # Initialize the application
    def __init__(self, root):
        self.root = root
        self.root.title("Back To School STATIONARIES! 🏫")
 
        # Store stationery items and their prices
        self.stationery_items = {
            "NOTEBOOK 📒": 3,
            "PENCIL BOX 👝": 3.5,
            "PEN HOLDER 🏮": 2,
            "ERASER ⬜": 1.5,
            "GEOMETRY BOX 📐📏": 3,
            "COLOUR PENCILS 🖍🖍🖍": 4.5
        }
 
        # Exchange rate for currency conversion
        self.exchange_rate = 82
 
        # Create a themed frame to hold the widgets
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
 
        # Heading label
        ttk.Label(
            frame,
            text="Back To School STATIONARIES! 🏫",
            font=("Bauhaus 93", 20, "bold")
        ).grid(
            row=0,
            columnspan=3,
            padx=10,
            pady=10
        )
 
        # Store references to labels and Entry widgets
        self.item_labels = {}
        self.item_quantities = {}
 
        # Create one row for every stationery item
        for index, (item, price) in enumerate(
            self.stationery_items.items(),
            start=1
        ):
            item_label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )
 
            item_label.grid(
                row=index,
                column=0,
                padx=10,
                pady=5
            )
 
            self.item_labels[item] = item_label
 
            quantity_entry = ttk.Entry(
                frame,
                width=5
            )
 
            quantity_entry.grid(
                row=index,
                column=1,
                padx=10,
                pady=5
            )
 
            self.item_quantities[item] = quantity_entry
 
        # Variable for storing the selected currency
        self.currency_var = tk.StringVar()
 
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(
            row=len(self.stationery_items) + 1,
            column=0,
            padx=10,
            pady=5
        )
 
        # Currency selection dropdown
        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR")
        )
 
        currency_dropdown.grid(
            row=len(self.stationery_items) + 1,
            column=1,
            padx=10,
            pady=5
        )
 
        # Select USD as the default currency
        currency_dropdown.current(0)
 
        # Update prices whenever the currency changes
        self.currency_var.trace(
            "w",
            self.update_item_prices
        )
 
        # Button to place the stationery order
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
 
        order_button.grid(
            row=len(self.stationery_items) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )


    # Update item prices according to the selected currency
    def update_item_prices(self, *args):
        currency = self.currency_var.get()
 
        # Pick values using the ternary operator
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
 
        for item, label in self.item_labels.items():
            price = self.stationery_items[item] * rate
 
            label.config(
                text=f"{item} ({symbol}{price}):"
            )
 
    # Read quantities and place the order
    def place_order(self):
        total_cost = 0
        order_summary = "Stationery Order Summary:\n"
 
        currency = self.currency_var.get()
 
        # Pick values using the ternary operator
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
 
        for item, entry in self.item_quantities.items():
            quantity = entry.get()
 
            # Validate that the quantity contains digits
            if quantity.isdigit():
                quantity = int(quantity)
 
                price = self.stationery_items[item] * rate
                cost = quantity * price
                total_cost += cost
 
                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x "
                        f"{symbol}{price} = {symbol}{cost}\n"
                    )
 
        if total_cost > 0:
            order_summary += (
                f"\nTotal Cost: {symbol}{total_cost}"
            )
 
            messagebox.showinfo(
                "Order Placed",
                order_summary
            )
 
        else:
            messagebox.showerror(
                "Error",
                "Please order at least one stationery item."
            )
 
 
# Main block to run the application
if __name__ == "__main__":
    root = tk.Tk()
 
    app = StationeryOrderManagement(root)
 
    root.geometry("800x600")
 
    # Start the GUI event loop
    root.mainloop()
