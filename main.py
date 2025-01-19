import re

def find_lines_in_text_file(file_path, pattern):
    # Compile the regular expression pattern
    regex = re.compile(pattern)
    
    # Dictionary to store the total amounts for each store
    store_totals = {}
    
    # Open the text file and read lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Search for the pattern in each line
        for line_num, line in enumerate(lines, start=1):
            matches = regex.findall(line)
            for match in matches:
                date1, date2, store, price = match
                price = float(price.replace(' CR', '').replace(',', ''))
                
                if store not in store_totals:
                    store_totals[store] = 0.0
                store_totals[store] += price

    # Print the total amounts for each store
    for store, total in store_totals.items():
        print(f"Total for {store}: {total:.2f}")
    # Print the total amount for all stores
    print(f"Total for all stores: {sum(store_totals.values()):.2f}")

# Example usage
file_path = 'files/transactions.txt'
pattern = r'(\w{3}\. \d{1,2}) (\w{3}\. \d{1,2}) ([A-Z0-9 \*\-#\@]+) (\d+\.\d{2}(?: CR)?)'
find_lines_in_text_file(file_path, pattern)