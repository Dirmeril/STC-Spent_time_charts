import datetime
import __main__
import pandas as pd


def sum_time():
    # Create matrix
    activity_summary = __main__.activity_summary
    df_activity_summary = pd.DataFrame(activity_summary)
    print(df_activity_summary)


