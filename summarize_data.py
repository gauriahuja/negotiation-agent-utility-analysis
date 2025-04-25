import pandas as pd

# Load the CSV
df = pd.read_csv("data.csv")

# Clean any whitespace from column names
df.columns = df.columns.str.strip()

# 1. Basic stats
total_sessions = len(df)
agreements = df[df["Agreement"] == "Yes"]
failed = df[df["Agreement"] != "Yes"]

# 2. Top agents by average utility
agents = pd.concat([df[["Agent 1", "Utility 1"]].rename(columns={"Agent 1": "Agent", "Utility 1": "Utility"}),
                    df[["Agent 2", "Utility 2"]].rename(columns={"Agent 2": "Agent", "Utility 2": "Utility"})])

agent_stats = agents.groupby("Agent").agg(
    Sessions=("Utility", "count"),
    Avg_Utility=("Utility", "mean")
).sort_values(by="Avg_Utility", ascending=False)

# 3. Agreement rate per agent
agent_agreements = pd.concat([
    agreements["Agent 1"],
    agreements["Agent 2"]
]).value_counts()

agent_stats["Agreements"] = agent_stats.index.map(agent_agreements).fillna(0).astype(int)
agent_stats["Agreement Rate"] = agent_stats["Agreements"] / agent_stats["Sessions"]

# 4. Most frequent matchups
matchups = df.groupby(["Agent 1", "Agent 2"]).size().reset_index(name="Session Count")
matchups = matchups.sort_values(by="Session Count", ascending=False)

# 5. Top agent summary
top_agent = agent_stats.iloc[0]
top_agent_summary = (
    f"🏆 Top Agent: {top_agent.name}\n"
    f"   - Sessions: {top_agent['Sessions']}\n"
    f"   - Avg Utility: {top_agent['Avg_Utility']:.4f}\n"
    f"   - Agreement Rate: {top_agent['Agreement Rate']:.2%}\n"
)

# 6. Write results
summary = [
    f"📊 Total negotiation sessions: {total_sessions}",
    f"✅ Agreements reached: {len(agreements)} ({len(agreements)/total_sessions:.2%})",
    f"❌ Failed negotiations: {len(failed)} ({len(failed)/total_sessions:.2%})\n",
    top_agent_summary,
    "📈 Top 5 Agents by Average Utility:\n" + agent_stats.head().to_string(),
    "\n🔁 Most Frequent Agent Pairs:\n" + matchups.head().to_string(index=False)
]

# Save as text file
with open("negotiation_summary.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(summary))

print("✅ Summary saved to 'negotiation_summary.txt'")
