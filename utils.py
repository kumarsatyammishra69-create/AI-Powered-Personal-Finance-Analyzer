def get_summary(df):
    summary = {
        "total_records"  : len(df),
        "total_spent"    : df['amount'].sum(),
        "avg_transaction": df['amount'].mean(),
        "top_category"   : df['category'].value_counts().idxmax()
    }
    return summary