# Negotiation Agent Utility Analysis and Feedback Preparation
This project analyzes the performance of automated negotiation agents using real-world competition data from the [Automated Negotiating Agents Competition (ANAC) 2019](https://data.4tu.nl/articles/dataset/Results_from_the_Automated_Negotiating_Agents_Competition_ANAC_2019_/19161851). 

Using Python and data processing techniques, this project generates structured summaries of agent performance metrics — including utility rankings, agreement rates, and negotiation outcomes — for use in downstream agentic AI feedback systems.

## Objective

To extract, summarize, and prepare negotiation performance data that can serve as training material for feedback-driven AI agents, aiding future work in negotiation coaching and autonomous decision-making support systems.

##  Technologies Used

- **Python 3.9+**
- **pandas** (for data handling and aggregation)
- **openpyxl** (for Excel reading)
- **NLP concepts** (summarization and prompt formatting)


## Dataset Source

- **Competition:** Automated Negotiating Agents Competition (ANAC) 2019
- **Link:** [4TU.ResearchData Repository](https://data.4tu.nl/articles/dataset/Results_from_the_Automated_Negotiating_Agents_Competition_ANAC_2019_/19161851)


## Project Structure

```bash
negotiation-agent-utility-analysis/
├── data/
│   ├── ANAC_results.xlsx                # Raw competition results
│   ├── Individual utility.csv            # Agent average utility scores
│   ├── Product utility.csv               # Alternative utility evaluation
│   └── data.csv                          # Negotiation session records
│
├── scripts/
│   ├── anac_analysis.py                  # Extract and clean sheets
│   ├── summarize_individual_utility.py   # Summarize individual utilities
│   ├── summarize_product_utility.py      # Summarize product-based utilities
│   └── summarize_data.py                  # Analyze full negotiation sessions
│
├── outputs/
│   ├── individual_utility_script.txt     # Ranked agent utilities
│   ├── product_utility_summary.txt       # Product utility summaries
│   └── negotiation_summary.txt           # Overall negotiation outcomes
│
├── README.md
```

---

## Installation
 **Install dependencies:**
   ```bash
   pip install pandas openpyxl
   ```

---

## How It Works

- **Step 1:** Load negotiation and agent utility data from multiple sources (Excel and CSVs).
- **Step 2:** Process agent performance metrics (average utility, agreement rate).
- **Step 3:** Rank agents and identify top performers and lowest performers.
- **Step 4:** Analyze total negotiation sessions, success vs. failure outcomes.
- **Step 5:** Format outputs as structured feedback prompts ready for future agentic AI integration.

---

## Example Output

Total negotiation sessions: 10500

Agreements reached: 7362 (70.11%)

Failed negotiations: 3138 (29.89%)

Top Agent: AgentGG
    - Sessions: 1000
    - Avg Utility: 0.7574
    - Agreement Rate: 81.00%

Top 5 Agents by Average Utility:
Agent     Sessions  Avg_Utility  Agreements  Agreement Rate
AgentGG        1000     0.757399         810           0.810
KakeSoba       1000     0.743267         796           0.796
...
```

---

## Research Relevance

This project enables downstream use in:
- Agentic AI feedback coaching
- Negotiation strategy recommendation systems
- Ethical decision-making simulations
- Healthcare AI negotiation modeling (e.g., patient-provider agreement systems)

---

## License
This project is intended for academic and research purposes under the University of Florida AI Systems Research Initiative.

---

## Author
**Gauri Ahuja**  
M.S. in Computer Science, University of Florida  
[LinkedIn](https://linkedin.com/in/gauri777) | [Email](mailto:ahujagauri@ufl.edu)
