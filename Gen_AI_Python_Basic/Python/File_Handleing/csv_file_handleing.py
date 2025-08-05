import csv  # Import CSV module for reading CSV files

with open('model_logs.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row

    # Create a dictionary where the key is the date (row[0]) and the value is the token count (row[3])
    token_data = {row[0]: int(row[3]) for row in reader}

    # Find the date with the highest number of tokens generated
    peak_day = max(token_data, key=token_data.get)

    # Print the date with the peak usage and the corresponding token count
    print(f'Peak Model Usage: {peak_day}, Tokens Generated: {token_data[peak_day]}')
