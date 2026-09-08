from backend.database.connection import get_connection


def check_data():
    connection = get_connection()
    cursor = connection.cursor()

    print("\nLife Areas:")

    cursor.execute(
        """
        SELECT id, name, description
        FROM life_areas
        """
    )

    for row in cursor.fetchall():
        print(row)

    print("\nConsciousness Levels:")

    cursor.execute(
        """
        SELECT id, name, score
        FROM consciousness_levels
        ORDER BY score
        """
    )

    for row in cursor.fetchall():
        print(row)

    connection.close()


if __name__ == "__main__":
    check_data()