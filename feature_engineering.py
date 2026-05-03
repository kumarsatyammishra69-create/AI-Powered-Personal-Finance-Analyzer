def add_features(df):
    if 'date' in df.columns:
        df['month']       = df['date'].dt.month
        df['day_of_week'] = df['date'].dt.dayofweek
        df['is_weekend']  = df['day_of_week'].isin([5, 6]).astype(int)
        df['year']        = df['date'].dt.year
    print("✅ Features added!")
    return df