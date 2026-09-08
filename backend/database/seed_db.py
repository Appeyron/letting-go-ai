from backend.database.connection import get_connection


def seed_database():
    connection = get_connection()
    cursor = connection.cursor()

    life_areas = [
        (
            "Work",
            "Career and professional life"
        )
    ]

    cursor.executemany(
        """
        INSERT INTO life_areas (name, description)
        VALUES (?, ?)
        """,
        life_areas
    )

    connection.commit()
    connection.close()

    print("Database seeded successfully.")


if __name__ == "__main__":
    seed_database()