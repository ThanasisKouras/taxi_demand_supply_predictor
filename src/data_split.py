from datetime import datetime, timezone
from typing import Tuple

import pandas as pd

def train_test_split(
    df: pd.DataFrame,
    cutoff_date: datetime,
    target_column_name: str,
) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    """
    """
    # Ensure cutoff_date is timezone-aware (UTC)
    cutoff_date = cutoff_date.replace(tzinfo=timezone.utc)


    # Convert pickup_hour to pandas datetime with timezone--------
    df['pickup_hour'] = pd.to_datetime(df['pickup_hour'], utc=True)

    ## Convert pickup_hour to pandas datetime with timezone##
    df['pickup_hour'] = pd.to_datetime(df['pickup_hour'], utc=True)

    # Assuming the pickup_hour column is already timezone-aware
    train_data = df[df.pickup_hour < cutoff_date].reset_index(drop=True)
    test_data = df[df.pickup_hour >= cutoff_date].reset_index(drop=True)

    # Print the number of samples before and after the cutoff date
    print(f'Number of samples before cutoff date: {len(train_data)}')
    print(f'Number of samples after cutoff date: {len(test_data)}')

    X_train = train_data.drop(columns=[target_column_name])
    y_train = train_data[target_column_name]
    X_test = test_data.drop(columns=[target_column_name])
    y_test = test_data[target_column_name]

    return X_train, y_train, X_test, y_test
