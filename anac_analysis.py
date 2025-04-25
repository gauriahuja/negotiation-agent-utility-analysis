import pandas as pd #loads the pandas library which is like excel in python.

# Step 1: Load All Sheets 
excel_path = "ANAC_results.xlsx"
all_sheets = pd.read_excel(excel_path, sheet_name=None) # loads all the sheets into the directory called all_sheets, sheet_name=None tells pandas that give me every sheet inside this excel file.

print("Sheets found in the file:") #loops through each sheet's name and prints it (like a preview of sheet names inside Excel)
for name in all_sheets:
    print(f" - {name}")

# Step 2: Loop through each sheet and process if valid 
for sheet_name, df in all_sheets.items(): #this loops through each sheet one by one, sheet_name is the sheet's name and df is the actual data inside that sheet.
    print(f"\nProcessing sheet: {sheet_name}")

    # Save raw sheet as CSV
    csv_name = f"{sheet_name}.csv" # saves each excel file as it's own csv, index=false means "don't include row numbers in the file"
    df.to_csv(csv_name, index=False)
    print(f"Saved full sheet to: {csv_name}")    

    # Try to summarize if it's an agent utility sheet
    if 'Row Labels' in df.columns and 'Average of Utility 1' in df.columns: # we are basically asking that does this sheet have both row labels and average of utility 1 columns?if both are found we continue otherwise we skip it.
        try: #let me try to process this sheet now and if anything goes wrong dont crash just tell me the error.
            # Optional: skip rows if the first few are not data
            df_clean = df[['Row Labels', 'Average of Utility 1']].dropna()
            df_clean.columns = ['Agent', 'Avg_Utility']
            df_sorted = df_clean.sort_values(by='Avg_Utility', ascending=False)

            # Save summary CSV
            summary_csv = f"{sheet_name}_agent_utility_summary.csv"
            df_sorted.to_csv(summary_csv, index=False)
            print(f"Agent utility summary saved to: {summary_csv}")

            # Print top 5
            print("Top 5 Agents:")
            print(df_sorted.head())

        except Exception as e:
            print(f"Could not summarize {sheet_name} due to error: {e}")
    else:
        print(f"ℹSheet '{sheet_name}' skipped for summary (no matching columns)")

