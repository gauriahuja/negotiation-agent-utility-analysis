import pandas as pd

# Load CSV, skip rows if needed
df = pd.read_csv("Individual utility.csv", skiprows=2)

# Print actual column names to verify
print("📌 Columns:", df.columns)

# Rename if needed based on actual headers
df = df[['Row Labels', 'Average of Utility 1']].dropna()
df.columns = ['Agent', 'Average Utility']

# Sort agents by utility
df_sorted = df.sort_values(by='Average Utility', ascending=False)

# Script the output
summary_lines = []
summary_lines.append("🔍 Agent Performance Summary\n")

top_agent = df_sorted.iloc[0]
worst_agent = df_sorted.iloc[-1]

summary_lines.append(f"🏆 Top Agent: {top_agent['Agent']} with average utility {top_agent['Average Utility']:.4f}")
summary_lines.append(f"🔻 Lowest Agent: {worst_agent['Agent']} with average utility {worst_agent['Average Utility']:.4f}")
summary_lines.append("\n📊 Full Rankings:\n")

for _, row in df_sorted.iterrows():
    summary_lines.append(f" - {row['Agent']}: {row['Average Utility']:.4f}")

# Save to text file
with open("individual_utility_script.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(summary_lines))

print("✅ Saved to 'individual_utility_script.txt'")

