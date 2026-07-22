# NYC 311 Service Requests Analysis
 
## How to Run
 
1. Make sure you have Python 3 installed.
2. Navigate to this folder in your terminal.
3. Run the script:
 
python3 analysis.py
 
Output will be saved to `output.txt`. The console will confirm when the file has been written.
 
## What This Script Does
 
This script reads the NYC 311 service request CSV file and counts requests by status, borough, and complaint type. It also finds the most common complaint, calculates closure rates by borough, and writes the final report to `output.txt`.
 
## Dependencies
 
This script uses only Python's built-in libraries: `csv`.
 
## Notes
 
The script uses dictionaries to count grouped values and uses `sorted()` to put the output in the required order. The closure rate is calculated from the number of closed requests divided by the total requests for each borough.
