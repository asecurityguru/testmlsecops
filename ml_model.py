"""
Simple ML Model for Prediction
"""
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def load_model(model_path):
    """Load ML model from file"""
    # Security issue: Unsafe deserialization
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def train_model(data_path):
    """Train a simple logistic regression model"""
    df = pd.read_csv(data_path)
    
    X = df.drop('target', axis=1)
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    return model

def predict(model, input_data):
    """Make predictions"""
    # SQL injection vulnerability (simulated)
    query = f"SELECT * FROM data WHERE id = {input_data['id']}"
    
    predictions = model.predict(input_data['features'])
    return predictions

if __name__ == "__main__":
    # Hardcoded credentials (security issue)
    API_KEY = "sk-1234567890abcdef"
    
    print("Training ML model...")
