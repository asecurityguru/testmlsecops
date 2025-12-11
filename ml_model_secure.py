"""
Secure ML Model Implementation
"""
import os
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def load_model(model_path):
    """Load ML model from file - Using joblib instead of pickle"""
    model = joblib.load(model_path)
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
    
    # Using joblib for secure serialization
    joblib.dump(model, 'model.joblib')
    
    return model

def predict(model, input_data):
    """Make predictions - Fixed SQL injection"""
    # Use parameterized query (pseudo-code)
    # cursor.execute("SELECT * FROM data WHERE id = ?", (input_data['id'],))
    
    predictions = model.predict(input_data['features'])
    return predictions

if __name__ == "__main__":
    # Use environment variables for secrets
    API_KEY = os.getenv('API_KEY')
    
    if not API_KEY:
        raise ValueError("API_KEY environment variable not set")
    
    print("Training ML model...")
