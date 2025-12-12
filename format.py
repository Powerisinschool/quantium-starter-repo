import pandas as pd

data = pd.concat([pd.read_csv('data/daily_sales_data_0.csv'), pd.read_csv('data/daily_sales_data_1.csv'), pd.read_csv('data/daily_sales_data_2.csv')])

# Applying the filters here:
filtered = data.loc[data['product'] == 'pink morsel'].reset_index(drop=True)
filtered['price_numeric'] = filtered['price'].str.replace('$', '').astype(float)
filtered['sales'] = filtered['price_numeric'] * filtered['quantity']
filtered.drop(['product', 'price', 'quantity', 'price_numeric'], axis=1, inplace=True)
filtered.to_csv('data/pink_morsels_filtered.csv', index=False)
