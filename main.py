from src.data_preprocessing import load_and_clean
from src.feature_engineering import add_features
from src.model_training import train_model

# Change this to your actual CSV file name
df = load_and_clean("data/raw/Personal_Finance_Dataset.csv")
df = add_features(df)
train_model(df)

print("Full pipeline complete!")