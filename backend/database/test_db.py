from backend.database.connection import get_connection


def test_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        ORDER BY name
        """
    )

    tables = cursor.fetchall()

    print("Database tables:")

    for table in tables:
        print(f"- {table[0]}")

    connection.close()


if __name__ == "__main__":
    test_database()