import pandas as pd

# Load and print structure to debug
df = pd.read_csv("Product utility.csv", skiprows=2)

# Auto-select the first two columns with actual data
first_two = df.columns[:2].tolist()
print("✅ Using columns:", first_two)

# Extract and clean
df_clean = df[first_two].dropna()
df_clean.columns = ['Agent', 'Avg_Product_Utility']
df_clean['Agent'] = df_clean['Agent'].str.strip()
df_clean = df_clean.drop_duplicates(subset='Agent')
df_sorted = df_clean.sort_values(by='Avg_Product_Utility', ascending=False)

# Build summary
summary = []
summary.append("🔍 Product Utility Summary\n")
summary.append(f"Total agents evaluated: {len(df_sorted)}\n")

top = df_sorted.iloc[0]
bottom = df_sorted.iloc[-1]

summary.append(f"🏆 Top Agent: {top['Agent']} with product utility {top['Avg_Product_Utility']:.4f}")
summary.append(f"🔻 Lowest Agent: {bottom['Agent']} with product utility {bottom['Avg_Product_Utility']:.4f}")
summary.append("\n📊 Full Rankings:\n")
for _, row in df_sorted.iterrows():
    summary.append(f" - {row['Agent']}: {row['Avg_Product_Utility']:.4f}")

# Save
with open("product_utility_summary.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(summary))

print("✅ Summary saved to 'product_utility_summary.txt'")

