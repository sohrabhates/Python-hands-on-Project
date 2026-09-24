import tkinter as tk
from tkinter import messagebox
import password_manager
import secrets
import string


# =========================================================
# WINDOW
# =========================================================

root = tk.Tk()

root.title("Password Manager")
root.geometry("1000x650")
root.minsize(850, 550)

root.configure(bg="#111827")


# =========================================================
# COLORS
# =========================================================

BG = "#111827"
SIDEBAR = "#1f2937"
CARD = "#1f2937"

TEXT = "#ffffff"
SECONDARY = "#9ca3af"

BUTTON = "#374151"
BUTTON_HOVER = "#4b5563"

ACCENT = "#6366f1"
ACCENT_HOVER = "#4f46e5"

DANGER = "#ef4444"


# =========================================================
# SIDEBAR
# =========================================================

sidebar = tk.Frame(
    root,
    bg=SIDEBAR,
    width=240
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


# =========================================================
# LOGO
# =========================================================

title = tk.Label(
    sidebar,
    text="🔐 Password\nManager",
    bg=SIDEBAR,
    fg=TEXT,
    font=("Segoe UI", 21, "bold"),
    justify="left"
)

title.pack(
    padx=25,
    pady=(35, 50),
    anchor="w"
)


# =========================================================
# CONTENT
# =========================================================

content = tk.Frame(
    root,
    bg=BG
)

content.pack(
    side="right",
    fill="both",
    expand=True
)


# =========================================================
# CLEAR CONTENT
# =========================================================

def clear_content():

    for widget in content.winfo_children():
        widget.destroy()


# =========================================================
# SIDEBAR BUTTON
# =========================================================

def sidebar_button(text, command):

    button = tk.Button(
        sidebar,
        text=text,
        command=command,
        bg=SIDEBAR,
        fg="#d1d5db",
        activebackground=BUTTON,
        activeforeground=TEXT,
        bd=0,
        relief="flat",
        font=("Segoe UI", 12),
        anchor="w",
        padx=25,
        pady=14,
        cursor="hand2"
    )

    button.pack(
        fill="x",
        padx=10
    )

    return button


# =========================================================
# DASHBOARD
# =========================================================

def dashboard():

    clear_content()

    passwords = password_manager.view()

    # Heading

    heading = tk.Label(
        content,
        text="Dashboard",
        bg=BG,
        fg=TEXT,
        font=("Segoe UI", 28, "bold")
    )

    heading.pack(
        anchor="nw",
        padx=50,
        pady=(45, 5)
    )

    # Subtitle

    subtitle = tk.Label(
        content,
        text="Manage your passwords securely.",
        bg=BG,
        fg=SECONDARY,
        font=("Segoe UI", 12)
    )

    subtitle.pack(
        anchor="nw",
        padx=50
    )

    # Password count card

    card = tk.Frame(
        content,
        bg=CARD,
        width=300,
        height=160
    )

    card.pack(
        anchor="nw",
        padx=50,
        pady=40
    )

    card.pack_propagate(False)

    label = tk.Label(
        card,
        text="Saved Passwords",
        bg=CARD,
        fg=SECONDARY,
        font=("Segoe UI", 11)
    )

    label.pack(
        anchor="nw",
        padx=25,
        pady=(25, 5)
    )

    count = tk.Label(
        card,
        text=str(len(passwords)),
        bg=CARD,
        fg=TEXT,
        font=("Segoe UI", 32, "bold")
    )

    count.pack(
        anchor="nw",
        padx=25
    )


# =========================================================
# ADD PASSWORD
# =========================================================

def add_password():

    clear_content()

    # Heading

    heading = tk.Label(
        content,
        text="Add Password",
        bg=BG,
        fg=TEXT,
        font=("Segoe UI", 28, "bold")
    )

    heading.pack(
        anchor="nw",
        padx=50,
        pady=(45, 5)
    )

    subtitle = tk.Label(
        content,
        text="Save a new password securely.",
        bg=BG,
        fg=SECONDARY,
        font=("Segoe UI", 12)
    )

    subtitle.pack(
        anchor="nw",
        padx=50,
        pady=(0, 30)
    )

    # Form card

    card = tk.Frame(
        content,
        bg=CARD,
        padx=35,
        pady=35
    )

    card.pack(
        anchor="nw",
        padx=50
    )

    # =====================================================
    # ACCOUNT NAME
    # =====================================================

    account_label = tk.Label(
        card,
        text="Account Name",
        bg=CARD,
        fg=TEXT,
        font=("Segoe UI", 11)
    )

    account_label.grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="w",
        pady=(0, 8)
    )

    account_entry = tk.Entry(
        card,
        width=45,
        bg="#374151",
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        font=("Segoe UI", 12)
    )

    account_entry.grid(
        row=1,
        column=0,
        columnspan=2,
        sticky="ew",
        ipady=9,
        pady=(0, 25)
    )

    # =====================================================
    # PASSWORD
    # =====================================================

    password_label = tk.Label(
        card,
        text="Password",
        bg=CARD,
        fg=TEXT,
        font=("Segoe UI", 11)
    )

    password_label.grid(
        row=2,
        column=0,
        columnspan=2,
        sticky="w",
        pady=(0, 8)
    )

    password_entry = tk.Entry(
        card,
        width=32,
        show="•",
        bg="#374151",
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        font=("Segoe UI", 12)
    )

    password_entry.grid(
        row=3,
        column=0,
        sticky="ew",
        ipady=9
    )

    # =====================================================
    # SHOW / HIDE
    # =====================================================

    def toggle_password():

        if password_entry.cget("show") == "":

            password_entry.config(
                show="•"
            )

            show_button.config(
                text="Show"
            )

        else:

            password_entry.config(
                show=""
            )

            show_button.config(
                text="Hide"
            )

    show_button = tk.Button(
        card,
        text="Show",
        command=toggle_password,
        bg=BUTTON,
        fg=TEXT,
        activebackground=BUTTON_HOVER,
        activeforeground=TEXT,
        bd=0,
        relief="flat",
        font=("Segoe UI", 10),
        cursor="hand2"
    )

    show_button.grid(
        row=3,
        column=1,
        padx=(10, 0)
    )

    # =====================================================
    # SAVE PASSWORD
    # =====================================================

    def save_password():

        account = account_entry.get().strip()
        password = password_entry.get()

        if not account:

            messagebox.showwarning(
                "Missing Account",
                "Please enter an account name."
            )

            account_entry.focus()

            return

        if not password:

            messagebox.showwarning(
                "Missing Password",
                "Please enter a password."
            )

            password_entry.focus()

            return

        try:

            password_manager.add(
                account,
                password
            )

            messagebox.showinfo(
                "Success",
                "Password saved successfully!"
            )

            account_entry.delete(
                0,
                tk.END
            )

            password_entry.delete(
                0,
                tk.END
            )

            account_entry.focus()

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not save password.\n\n{e}"
            )

    save_button = tk.Button(
        card,
        text="🔒  Save Password",
        command=save_password,
        bg=ACCENT,
        fg=TEXT,
        activebackground=ACCENT_HOVER,
        activeforeground=TEXT,
        bd=0,
        relief="flat",
        font=("Segoe UI", 11, "bold"),
        cursor="hand2",
        padx=20,
        pady=11
    )

    save_button.grid(
        row=4,
        column=0,
        columnspan=2,
        sticky="ew",
        pady=(28, 0)
    )


# =========================================================
# VIEW PASSWORDS
# =========================================================

def view_passwords():

    clear_content()

    heading = tk.Label(
        content,
        text="My Passwords",
        bg=BG,
        fg=TEXT,
        font=("Segoe UI", 28, "bold")
    )

    heading.pack(
        anchor="nw",
        padx=50,
        pady=(45, 5)
    )

    subtitle = tk.Label(
        content,
        text="View your saved accounts.",
        bg=BG,
        fg=SECONDARY,
        font=("Segoe UI", 12)
    )

    subtitle.pack(
        anchor="nw",
        padx=50,
        pady=(0, 25)
    )

    passwords = password_manager.view()

    # No passwords

    if not passwords:

        empty_card = tk.Frame(
            content,
            bg=CARD,
            width=500,
            height=120
        )

        empty_card.pack(
            anchor="nw",
            padx=50,
            pady=10
        )

        empty_card.pack_propagate(False)

        empty = tk.Label(
            empty_card,
            text="No passwords saved yet.",
            bg=CARD,
            fg=SECONDARY,
            font=("Segoe UI", 13)
        )

        empty.pack(
            expand=True
        )

        return

    # =====================================================
    # PASSWORD CARDS
    # =====================================================

    for account, password in passwords:

        card = tk.Frame(
            content,
            bg=CARD
        )

        card.pack(
            fill="x",
            padx=50,
            pady=6
        )

        # Account

        account_label = tk.Label(
            card,
            text=account,
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 12, "bold"),
            width=20,
            anchor="w"
        )

        account_label.pack(
            side="left",
            padx=(20, 10),
            pady=15
        )

        # Password

        password_label = tk.Label(
            card,
            text="••••••••",
            bg=CARD,
            fg=SECONDARY,
            font=("Segoe UI", 11),
            width=18,
            anchor="w"
        )

        password_label.pack(
            side="left"
        )

        # Show / Hide

        def toggle(
            label=password_label,
            pwd=password
        ):

            if label.cget("text") == "••••••••":

                label.config(
                    text=pwd
                )

            else:

                label.config(
                    text="••••••••"
                )

        show_button = tk.Button(
            card,
            text="Show",
            command=toggle,
            bg=BUTTON,
            fg=TEXT,
            activebackground=BUTTON_HOVER,
            activeforeground=TEXT,
            bd=0,
            relief="flat",
            font=("Segoe UI", 10),
            cursor="hand2"
        )

        show_button.pack(
            side="right",
            padx=20,
            pady=10
        )


# =========================================================
# PASSWORD GENERATOR
# =========================================================

def generator():

    clear_content()

    heading = tk.Label(
        content,
        text="Password Generator",
        bg=BG,
        fg=TEXT,
        font=("Segoe UI", 28, "bold")
    )

    heading.pack(
        anchor="nw",
        padx=50,
        pady=(45, 5)
    )

    subtitle = tk.Label(
        content,
        text="Generate a strong random password.",
        bg=BG,
        fg=SECONDARY,
        font=("Segoe UI", 12)
    )

    subtitle.pack(
        anchor="nw",
        padx=50,
        pady=(0, 30)
    )

    card = tk.Frame(
        content,
        bg=CARD,
        padx=35,
        pady=35
    )

    card.pack(
        anchor="nw",
        padx=50
    )

    password_var = tk.StringVar()

    password_entry = tk.Entry(
        card,
        textvariable=password_var,
        width=50,
        bg="#374151",
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        font=("Consolas", 13)
    )

    password_entry.grid(
        row=0,
        column=0,
        columnspan=2,
        ipady=10,
        pady=(0, 20)
    )

    # =====================================================
    # GENERATE
    # =====================================================

    def generate():

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = "".join(
            secrets.choice(characters)
            for _ in range(16)
        )

        password_var.set(
            password
        )

    # =====================================================
    # COPY
    # =====================================================

    def copy_password():

        password = password_var.get()

        if not password:

            messagebox.showwarning(
                "Nothing to Copy",
                "Generate a password first."
            )

            return

        root.clipboard_clear()

        root.clipboard_append(
            password
        )

        root.update()

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard."
        )

    generate_button = tk.Button(
        card,
        text="⚡ Generate",
        command=generate,
        bg=ACCENT,
        fg=TEXT,
        activebackground=ACCENT_HOVER,
        activeforeground=TEXT,
        bd=0,
        relief="flat",
        font=("Segoe UI", 11, "bold"),
        cursor="hand2",
        padx=20,
        pady=9
    )

    generate_button.grid(
        row=1,
        column=0,
        padx=(0, 10)
    )

    copy_button = tk.Button(
        card,
        text="📋 Copy",
        command=copy_password,
        bg=BUTTON,
        fg=TEXT,
        activebackground=BUTTON_HOVER,
        activeforeground=TEXT,
        bd=0,
        relief="flat",
        font=("Segoe UI", 11),
        cursor="hand2",
        padx=20,
        pady=9
    )

    copy_button.grid(
        row=1,
        column=1
    )


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

sidebar_button(
    "🏠  Dashboard",
    dashboard
)

sidebar_button(
    "➕  Add Password",
    add_password
)

sidebar_button(
    "🔑  My Passwords",
    view_passwords
)

sidebar_button(
    "⚡  Generator",
    generator
)


# =========================================================
# START APPLICATION
# =========================================================

dashboard()

root.mainloop()
