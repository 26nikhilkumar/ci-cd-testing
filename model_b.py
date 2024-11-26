import re
import matplotlib.pyplot as plt
from collections import Counter

def conflict_frequency(logs):
    pattern = r"^.*\s+<<<<<<<\s+HEAD\s+.*\s+======="
    conflicts = Counter(re.findall(pattern, logs, re.MULTILINE))
    return conflicts

def visualize_conflicts(conflicts):
    plt.bar(conflicts.keys(), conflicts.values())
    plt.xlabel('File Name')
    plt.ylabel('Number of Conflicts')
    plt.title('Merge Conflict Frequencies')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    try:
        with open('git_logs.txt', 'r') as file:
            logs = file.read()
        conflicts = conflict_frequency(logs)
        visualize_conflicts(conflicts)
    except FileNotFoundError:
        print("Error: Git logs file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()