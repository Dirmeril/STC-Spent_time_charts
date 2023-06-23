import gui
import load_data
import pandas as pd
import datetime


if __name__ == '__main__':
    activity_summary = load_data.load()
    df_activity_summary = pd.DataFrame(activity_summary, dtype='timedelta64[s]')
    # df_activity_summary = df_activity_summary.applymap(lambda x: str(x).split()[-1]) # transform from deltatime to string
    app = gui.App()
    app.mainloop()
