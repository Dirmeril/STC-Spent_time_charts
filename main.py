import gui
import load_data


if __name__ == '__main__':
    activity_summary = load_data.load()
    app = gui.App()
    app.mainloop()