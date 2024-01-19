import tkinter as tk
from UI.login_screen import LoginScreen
from UI.main_screen import MainScreen

def main():
    root = tk.Tk()

    def on_login_success(username):
        login_screen.root.destroy()  # Close the login window
        main_screen = MainScreen(username=username)

    login_screen = LoginScreen(root, on_login_success)

    root.mainloop()

    # main_screen = MainScreen()
    # main_screen.root.mainloop()

if __name__ == "__main__":
    main()
