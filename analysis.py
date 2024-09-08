import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Correct file path
file_path = r"C:\Users\91904\Downloads\financial-analysis-portfolio\Nifty 50 Futures Historical Data.csv"
data = pd.read_csv(file_path)

# Continue with the rest of your script...


# Display the first few rows of the dataset
print(data.head())

# Data Preprocessing
# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Remove rows where 'Date' could not be converted
data = data.dropna(subset=['Date'])

# Set 'Date' as the index
data.set_index('Date', inplace=True)

# Convert 'Change %' to numeric (remove '%' sign and convert to float)
data['Change %'] = data['Change %'].str.rstrip('%').astype('float') / 100.0

# Convert 'Volume' to numeric (remove 'M' and convert to float)
data['Vol.'] = data['Vol.'].str.replace('M', '').astype('float') * 1e6

# Display basic statistics
print(data.describe())

# Plot Price Trend
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Price'], label='Price', color='blue')
plt.title('Nifty 50 Futures Price Trend')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r'C:\Users\91904\Downloads\financial-analysis-portfolio\price_trend.png')
plt.show()

# Plot Volume Trend
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Vol.'], label='Volume', color='orange')
plt.title('Nifty 50 Futures Volume Trend')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r'C:\Users\91904\Downloads\financial-analysis-portfolio\volume_trend.png')
plt.show()

# Plot Change % Distribution
plt.figure(figsize=(12, 6))
sns.histplot(data['Change %'], bins=30, kde=True, color='green')
plt.title('Distribution of Daily Change %')
plt.xlabel('Change %')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.savefig(r'C:\Users\91904\Downloads\financial-analysis-portfolio\change_distribution.png')
plt.show()
