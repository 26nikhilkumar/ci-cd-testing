import psycopg2


def save_conflict_data(conflicts):
    """
    Saves conflict metrics to a PostgreSQL database.

    Args:
        conflicts (list of dict): Conflict data with file_name, developer_name, conflict_type, etc.
    """
    try:
        # Database connection
        conn = psycopg2.connect(
            dbname="conflicts_db", user="username", password="password", host="localhost"
        )
        cursor = conn.cursor()

        # Insert each conflict into the database
        for conflict in conflicts:
            cursor.execute(
                """
                INSERT INTO merge_conflicts (file_name, developer_name, conflict_type, resolution_time_seconds, conflict_date)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    conflict["file_name"],
                    conflict["developer_name"],
                    conflict["conflict_type"],
                    conflict["resolution_time_seconds"],
                    conflict["conflict_date"],
                ),
            )

        # Commit and close the connection
        conn.commit()
        conn.close()
        print("Data saved successfully.")

    except Exception as e:
        print(f"Error saving data: {e}")
