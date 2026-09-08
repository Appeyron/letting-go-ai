from fastapi import APIRouter

from backend.database.connection import get_connection


router = APIRouter(
    prefix="/api/life-areas",
    tags=["Life Areas"]
)


@router.get("/")
async def get_life_areas():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, description
        FROM life_areas
        ORDER BY id
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "description": row[2]
        }
        for row in rows
    ]