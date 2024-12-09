import pandas as pd

def load_and_process_data(file_path):
    """Load biodiversity data from a CSV file and preprocess it."""
    # Load data
    data = pd.read_csv(file_path)
    
    # Ensure data types are correct
    data['year'] = pd.to_numeric(data['year'], errors='coerce')
    data['population_count'] = pd.to_numeric(data['population_count'], errors='coerce')
    
    # Drop rows with missing values
    data = data.dropna()
    
    return data
