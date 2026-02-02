import pandas as pd
import numpy as np

# Settings
n_rows = 5000
gateways = ['HDFC', 'ICICI', 'Razorpay']
card_networks = ['Visa', 'Mastercard', 'Amex']

# Generate random base data
data = {
    'transaction_id': range(1000, 1000 + n_rows),
    'gateway': np.random.choice(gateways, n_rows),
    'card_network': np.random.choice(card_networks, n_rows),
}

df = pd.DataFrame(data)

# The "Pattern" Logic for your interview
def determine_success(row):
    # HDFC is great for Visa (90% success)
    if row['gateway'] == 'HDFC' and row['card_network'] == 'Visa':
        return 1 if np.random.random() < 0.90 else 0
    # ICICI is great for Mastercard (85% success)
    elif row['gateway'] == 'ICICI' and row['card_network'] == 'Mastercard':
        return 1 if np.random.random() < 0.85 else 0
    # Everything else is average (50% success)
    else:
        return 1 if np.random.random() < 0.50 else 0

df['is_success'] = df.apply(determine_success, axis=1)

# Save to CSV
df.to_csv('transactions.csv', index=False)
print("Success! 'transactions.csv' created with 5,000 rows.")