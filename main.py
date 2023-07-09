import gui
import load_data
import pandas as pd


if __name__ == '__main__':
    activity_summary = load_data.load()
    df_activity_summary = pd.DataFrame(activity_summary, dtype='timedelta64[s]')
    app = gui.App()
    app.mainloop()
