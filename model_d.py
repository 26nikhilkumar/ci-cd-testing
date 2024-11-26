from collections import defaultdict
import matplotlib.pyplot as plt
import sqlite3

# Function to calculate conflict frequencies
def conflict_frequency(logs):
    result = defaultdict(int)
    try:
        for log in logs:
            if "conflict" in log:
                parts = log.split()
                file_name = parts[-1]
                result[file_name] += 1
    except Exception as e:
        print(f"Error: {e}")
        return {}
    return result

# Function to visualize conflict frequencies
def visualize_conflict_frequencies(result):
    file_names = list(result.keys())
    conflict_counts = list(result.values())

    plt.bar(file_names, conflict_counts, color="skyblue")
    plt.xlabel("File Name")
    plt.ylabel("Conflict Count")
    plt.title("Merge Conflict Frequencies")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to store conflict frequencies in SQLite
def store_conflict_frequencies(result):
    conn = sqlite3.connect("conflict_frequencies.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS conflicts (file_name TEXT, conflict_count INTEGER)")
    for file_name, conflict_count in result.items():
        c.execute("INSERT INTO conflicts (file_name, conflict_count) VALUES (?, ?)", (file_name, conflict_count))
    conn.commit()
    conn.close()

# Main function for testing
if __name__ == "__main__":
    # Simulated Git logs
    logs = [
        "Auto-merging src/file1.py",
        "CONFLICT (content): Merge conflict in src/file1.py",
        "Auto-merging src/file2.py",
        "CONFLICT (content): Merge conflict in src/file2.py",
        "CONFLICT (content): Merge conflict in src/file3.py",
        "Automatic merge failed; fix conflicts and then commit the result.",
    ]

    # Analyze conflict frequencies
    conflict_counts = conflict_frequency(logs)

    # Visualize conflicts
    if conflict_counts:
        visualize_conflict_frequencies(conflict_counts)

    # Store conflicts in the database
    store_conflict_frequencies(conflict_counts)
    print("Conflict frequencies stored in the database.")
