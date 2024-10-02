import pandas as pd
import numpy as np

# Create a synthetic dataset
num_samples = 1000
np.random.seed(42)  # For reproducibility

# Generate random features
feature_1 = np.random.rand(num_samples)
feature_2 = np.random.rand(num_samples)
feature_3 = np.random.rand(num_samples)

# Create labels based on some logic
# For example: label is 1 if feature_1 > 0.5 and feature_2 < 0.5
labels = np.where((feature_1 > 0.5) & (feature_2 < 0.5), 1, 0)

# Create a DataFrame
df = pd.DataFrame({
    'feature_1': feature_1,
    'feature_2': feature_2,
    'feature_3': feature_3,
    'label': labels
})

# Save to CSV
df.to_csv('threat_data.csv', index=False)
print("Synthetic dataset created and saved as 'threat_data.csv'")
