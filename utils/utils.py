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

    return (max_value,min_value, avg_value, median_value)

def count_jaccard_similarity(ner1, ner2):

    set1 = set(ner1)
    set2 = set(ner2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 0
    return (intersection / union)
