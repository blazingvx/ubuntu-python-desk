
import tkinter as tk
from tkinter import messagebox


APP_NAME = "Ubuntu Python Desk"


class DesktopApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("540x340")
        self.root.minsize(400, 280)

        self.name_var = tk.StringVar()
        self.status_var = tk.StringVar(
            value="Ready — your application is running."
        )

        self._build_menu()
        self._build_interface()

    def _build_menu(self) -> None:
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=False)
        file_menu.add_command(
            label="Clear",
            command=self.clear_input,
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Exit",
            command=self.root.destroy,
        )
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menu_bar, tearoff=False)
        help_menu.add_command(
            label="About",
            command=self.show_about,
        )
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.configure(menu=menu_bar)

    def _build_interface(self) -> None:
        frame = tk.Frame(self.root, padx=28, pady=24)
        frame.pack(fill="both", expand=True)

        tk.Label(
            frame,
            text="Welcome to Ubuntu Python Desk",
            font=("TkDefaultFont", 16, "bold"),
        ).pack(anchor="w", pady=(0, 8))

        tk.Label(
            frame,
            text="Enter your name to try the application.",
        ).pack(anchor="w", pady=(0, 16))

        tk.Label(frame, text="Your name").pack(anchor="w")

        self.name_entry = tk.Entry(
            frame,
            textvariable=self.name_var,
        )
        self.name_entry.pack(fill="x", pady=(5, 14))
        self.name_entry.focus_set()
        self.name_entry.bind("<Return>", self.greet)

        tk.Button(
            frame,
            text="Say hello",
            command=self.greet,
        ).pack(anchor="w")

        tk.Label(
            self.root,
            textvariable=self.status_var,
            anchor="w",
            relief="sunken",
            padx=8,
            pady=5,
        ).pack(fill="x", side="bottom")

    def greet(self, event=None) -> None:
        name = self.name_var.get().strip()

        if not name:
            messagebox.showwarning(
                APP_NAME,
                "Please enter your name first.",
            )
            self.name_entry.focus_set()
            return

        messagebox.showinfo(
            APP_NAME,
            f"Hello, {name}! Your Python GUI is working.",
        )
        self.status_var.set(f"Last greeting: {name}")

    def clear_input(self) -> None:
        self.name_var.set("")
        self.status_var.set("Input cleared.")
        self.name_entry.focus_set()

    def show_about(self) -> None:
        messagebox.showinfo(
            f"About {APP_NAME}",
            f"{APP_NAME}\nA Python desktop application for Ubuntu.",
        )


def main() -> None:
    root = tk.Tk()
    DesktopApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
