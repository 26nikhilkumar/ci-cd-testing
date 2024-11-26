import re
import matplotlib.pyplot as plt
from collections import Counter
import logging

# Configure logging
logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)


def parse_git_log(logs):
    """
    Parses Git logs to extract merge conflict information.

    Args:
        logs (list): List of Git log entries.

    Returns:
        dict: A dictionary with file names as keys and conflict counts as values.
    """
    conflict_pattern = re.compile(r"conflict in (.*)")
    result = Counter()

    for log in logs:
        try:
            match = conflict_pattern.search(log)
            if match:
                file_name = match.group(1)
                result[file_name] += 1
        except Exception as e:
            logging.error(f"Error parsing log: {e}")

    return dict(result)


def visualize_conflicts(conflict_counts):
    """
    Visualizes merge conflict frequencies using a bar chart.

    Args:
        conflict_counts (dict): A dictionary with file names and conflict counts.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(
        conflict_counts.keys(), conflict_counts.values(), color="skyblue"
    )  # Use a light color for better visibility
    plt.title("Merge Conflict Frequency")
    plt.xlabel("File Name")
    plt.ylabel("Number of Conflicts")
    plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for readability
    plt.tight_layout()
    plt.show()


def analyze_conflicts(logs):
    """
    Analyzes merge conflict frequencies from Git logs.

    Args:
        logs (list): List of Git log entries.

    Returns:
        dict: A dictionary with file names and conflict counts.
    """
    try:
        conflict_counts = parse_git_log(logs)
        visualize_conflicts(conflict_counts)
        return conflict_counts
    except Exception as e:
        logging.error(f"Error analyzing conflicts: {e}")
        return {}


# Example usage
if __name__ == "__main__":
    # Sample Git log entries
    logs = [
        "Merge branch 'feature' into develop",
        "Auto-merging src/file1.py",
        "CONFLICT (content): Merge conflict in src/file1.py",
        "Auto-merging src/file2.py",
        "CONFLICT (content): Merge conflict in src/file2.py",
        "Automatic merge failed; fix conflicts and then commit the result.",
    ]

    conflict_counts = analyze_conflicts(logs)
    print(conflict_counts)