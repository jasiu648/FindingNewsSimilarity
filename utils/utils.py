import statistics

def calculate_stats(float_list):
    if not float_list:
        print("List is empty.")
        return

    # Maximum
    max_value = max(float_list)

    # Minimum
    min_value = min(float_list)

    # Average
    avg_value = sum(float_list) / len(float_list)

    # Median
    median_value = statistics.median(float_list)

    # Print the results
    print(f"Maximum: {max_value}")
    print(f"Minimum: {min_value}")
    print(f"Average: {avg_value:.2f}")
    print(f"Median: {median_value:.2f}")