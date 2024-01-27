import statistics


def count_jaccard_similarity(ner1, ner2):

    set1 = set(ner1)
    set2 = set(ner2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 0
    return (intersection / union)

def count_words(text):
    """
    Count the number of words in a given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - int: Number of words in the text.
    """
    words = text.split()
    return len(words)

import matplotlib.pyplot as plt
import numpy as np

def create_histogram(data, threshold=700):
    """
    Create a histogram from a list of integers, ignoring values above a threshold.

    Parameters:
    - data (list of int): List of integers for the histogram.
    - threshold (int): Values above this threshold will be ignored in the histogram.

    Returns:
    - None
    """
    # Filter values below or equal to the threshold
    filtered_data = np.array(data)[np.array(data) <= threshold]
    
    plt.hist(filtered_data, bins=10, edgecolor='black')  # Adjust the number of bins as needed
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

import statistics
def calculate_stats(float_list):
    if not float_list:
        print("List is empty.")
        return

    # Count 
    count = len(float_list)

    # Maximum
    max_value = max(float_list)

    # Minimum
    min_value = min(float_list)

    # Average
    avg_value = sum(float_list) / len(float_list)

    # Median
    median_value = statistics.median(float_list)

    # Variance
    variance_value = statistics.variance(float_list)

    # Standard Deviation
    std_deviation_value = statistics.stdev(float_list)

    # Print the results
    print(f"Count: {count}")
    print(f"Maximum: {max_value}")
    print(f"Minimum: {min_value}")
    print(f"Average: {avg_value:.2f}")
    print(f"Median: {median_value:.2f}")
    print(f"Variance: {variance_value:.2f}")
    print(f"Standard Deviation: {std_deviation_value:.2f}")

    return (max_value, min_value, avg_value, median_value, variance_value, std_deviation_value)
