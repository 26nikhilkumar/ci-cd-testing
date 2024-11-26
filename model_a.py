import re
import matplotlib.pyplot as plt

def parse_log(log):
    # Match lines starting with 'CONFLICT' and extract the file name
    match = re.search(r"^.*conflict.*: (.*)$", log)
    if match:
        return match.group(1)  # Extract the file name
    return None


def conflict_frequency(logs):
    result = {}
    for log in logs:
        file_name = parse_log(log)
        print(f"Parsed file: {file_name}")  # Add this line
        if file_name:
            result[file_name] = result.get(file_name, 0) + 1
    print(f"Conflict Frequency: {result}")  # Add this line
    return result


def visualize_conflicts(conflicts):
    plt.bar(conflicts.keys(), conflicts.values())
    plt.xlabel('File Name')
    plt.ylabel('Number of Conflicts')
    plt.title('Merge Conflict Frequencies')
    plt.show()

def main():
    try:
        with open('git_logs.txt', 'r') as file:
            logs = file.readlines()
        conflicts = conflict_frequency(logs)
        visualize_conflicts(conflicts)
    except FileNotFoundError:
        print("Error: Git logs file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()