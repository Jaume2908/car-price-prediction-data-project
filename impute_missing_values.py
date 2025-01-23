import pandas as pd
from sklearn.impute import SimpleImputer

# Example DataFrame
data = {
    'make': ['Toyota', 'Honda', 'Ford', None, 'BMW'],
    'location': ['NY', 'CA', 'TX', 'FL', None],
    'model': ['Corolla', 'Civic', 'Focus', 'Fiesta', '3 Series'],
    'version': [None, 'EX', 'SE', 'Titanium', None],
    'power': [130, None, 160, 120, 250],
    'dealer_name': ['Dealer1', None, 'Dealer3', 'Dealer4', 'Dealer5'],
    'fuel': ['Petrol', 'Diesel', None, 'Petrol', 'Diesel'],
    'kms': [50000, 30000, None, 40000, 20000],
    'shift': ['Manual', None, 'Automatic', 'Manual', 'Automatic']
}

df = pd.DataFrame(data)

# Imputing missing values
imputer = SimpleImputer(strategy='most_frequent')

df[['version', 'power', 'dealer_name', 'fuel', 'kms', 'shift']] = imputer.fit_transform(df[['version', 'power', 'dealer_name', 'fuel', 'kms', 'shift']])

print(df)