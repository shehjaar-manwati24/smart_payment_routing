import pandas as pd

# 1. Load the data
df = pd.read_csv('transactions.csv')

# 2. Calculate Success Rates
# Group by card_network and gateway to find the average of 'is_success'
analysis = df.groupby(['card_network', 'gateway'])['is_success'].mean().reset_index()

# Convert decimal (0.9) to percentage (90.0%)
analysis['success_rate_pct'] = (analysis['is_success'] * 100).round(2)

# 3. Find the Best Gateway per Card Network
# Sort by card network and highest success rate
recommendations = analysis.sort_values(['card_network', 'success_rate_pct'], ascending=[True, False])
recommendations = recommendations.drop_duplicates('card_network')

print("--- SMART PAYMENT ROUTING REPORT ---")
print("\nFull Analysis Table:")
print(analysis[['card_network', 'gateway', 'success_rate_pct']])

print("\n--- FINAL RECOMMENDATIONS ---")
for index, row in recommendations.iterrows():
    print(f"For {row['card_network']} cards: Use {row['gateway']} ({row['success_rate_pct']}% Success)")