"""Week 9: Tkinter GUI that reuses the CameraKit and RentalItem classes.

From this folder:
    python3 rental_gui.py
"""

import tkinter as tk
from tkinter import ttk

from camera_kit import CameraKit


class RentalApp:
    """The GUI handles clicks and displays results; CameraKit handles rental rules."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("Camera Kit Rental | Week 9")
        root.geometry("640x560")
        root.minsize(470, 400)

        # Each item is an object of our existing Week 8 class.
        self.kits = {
            "Canon R6 (CAM-001)": CameraKit(
                "Canon", "R6", "CAM-001", "Mirrorless", 45.00
            ),
            "Sony A7 IV (CAM-002)": CameraKit(
                "Sony", "A7 IV", "CAM-002", "Mirrorless", 55.00
            ),
            "Nikon Z6 II (CAM-003)": CameraKit(
                "Nikon", "Z6 II", "CAM-003", "Full frame", 40.00
            ),
        }

        self.selected = tk.StringVar(value=next(iter(self.kits)))
        self.days = tk.StringVar(value="3")
        self.description = tk.StringVar()
        self.booking_status = tk.StringVar()
        self.total_price = tk.StringVar(value="—")
        self.message = tk.StringVar(value="Choose an item and a rental duration.")

        style = ttk.Style(root)
        if "clam" in style.theme_names():
            style.theme_use("clam")
        style.configure("Heading.TLabel", font=("Sans", 18, "bold"))
        style.configure("Subheading.TLabel", font=("Sans", 10))
        style.configure("Status.TLabel", font=("Sans", 11, "bold"))
        style.configure("Total.TLabel", font=("Sans", 16, "bold"))

        content = ttk.Frame(root, padding=22)
        content.pack(fill="both", expand=True)

        ttk.Label(content, text="Camera Kit Rental", style="Heading.TLabel").pack(anchor="w")
        ttk.Label(
            content, text="Week 9 • Tkinter + object-oriented Python",
            style="Subheading.TLabel"
        ).pack(anchor="w", pady=(2, 16))

        form = ttk.LabelFrame(content, text="Rental details", padding=14)
        form.pack(fill="x")

        ttk.Label(form, text="Camera kit").grid(row=0, column=0, sticky="w", pady=5)
        self.camera_combo = ttk.Combobox(
            form, textvariable=self.selected,
            values=list(self.kits), state="readonly", width=27
        )
        self.camera_combo.grid(row=0, column=1, sticky="ew", padx=(10, 0), pady=5)
        self.camera_combo.bind("<<ComboboxSelected>>", self.on_selection_changed)

        ttk.Label(form, text="Rental days").grid(row=1, column=0, sticky="w", pady=5)
        self.days_spin = ttk.Spinbox(
            form, from_=1, to=365, textvariable=self.days, width=8
        )
        self.days_spin.grid(row=1, column=1, sticky="w", padx=(10, 0), pady=5)
        form.columnconfigure(1, weight=1)

        info = ttk.Frame(content, padding=(2, 16, 2, 6))
        info.pack(fill="x")
        ttk.Label(info, textvariable=self.description, wraplength=470).pack(anchor="w")
        ttk.Label(info, textvariable=self.booking_status, style="Status.TLabel").pack(
            anchor="w", pady=(6, 0)
        )

        actions = ttk.Frame(content)
        actions.pack(fill="x", pady=(12, 8))
        actions.columnconfigure((0, 1, 2), weight=1)
        ttk.Button(
            actions, text="Calculate price", command=self.calculate_price
        ).grid(row=0, column=0, sticky="ew", padx=(0, 6))
        self.book_button = ttk.Button(
            actions, text="Book camera", command=self.book_camera
        )
        self.book_button.grid(row=0, column=1, sticky="ew", padx=3)
        self.return_button = ttk.Button(
            actions, text="Return camera", command=self.return_camera
        )
        self.return_button.grid(row=0, column=2, sticky="ew", padx=(6, 0))

        totals = ttk.LabelFrame(content, text="Estimated cost", padding=12)
        totals.pack(fill="x", pady=(5, 8))
        ttk.Label(totals, textvariable=self.total_price, style="Total.TLabel").pack(
            anchor="w"
        )
        ttk.Label(
            content, textvariable=self.message, wraplength=470, justify="left"
        ).pack(fill="x", anchor="w", pady=(5, 0))

        self.refresh_display()

    def current_kit(self) -> CameraKit:
        """Return the object selected in the drop-down menu."""
        return self.kits[self.selected.get()]

    def read_days(self) -> int | None:
        """Validate text from the GUI before passing it to our model."""
        try:
            days = int(self.days.get().strip())
        except ValueError:
            self.message.set("Enter a whole number of days (1–365).")
            return None
        if not 1 <= days <= 365:
            self.message.set("Rental days must be between 1 and 365.")
            return None
        return days

    def refresh_display(self) -> None:
        """Update what the user sees, using the object's current state."""
        kit = self.current_kit()
        self.description.set(
            f"{kit.brand} {kit.model} • {kit.kit_type} • "
            f"€{kit.check_rate():.2f} per day"
        )
        booked = kit.is_booked()
        self.booking_status.set("Status: Booked" if booked else "Status: Available")
        self.book_button.state(["disabled"] if booked else ["!disabled"])
        self.return_button.state(["!disabled"] if booked else ["disabled"])

    def on_selection_changed(self, event: tk.Event) -> None:
        """A Tkinter event runs when a different camera is selected."""
        self.total_price.set("—")
        self.message.set("Camera selection changed.")
        self.refresh_display()

    def calculate_price(self) -> None:
        days = self.read_days()
        if days is None:
            return
        kit = self.current_kit()
        total = kit.calculate_cost(days)
        self.total_price.set(f"€{total:.2f}")
        self.message.set(f"{days} day(s) at €{kit.check_rate():.2f} per day.")

    def book_camera(self) -> None:
        days = self.read_days()
        if days is None:
            return
        kit = self.current_kit()
        if kit.book():
            total = kit.calculate_cost(days)
            self.total_price.set(f"€{total:.2f}")
            self.message.set(f"Booking successful for {days} day(s)!")
        else:
            self.message.set("This camera is already booked.")
        self.refresh_display()

    def return_camera(self) -> None:
        kit = self.current_kit()
        if kit.is_booked():
            kit.return_item()
            self.message.set("Camera returned successfully.")
        else:
            self.message.set("This camera is already available.")
        self.refresh_display()


def main() -> None:
    root = tk.Tk()
    RentalApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
