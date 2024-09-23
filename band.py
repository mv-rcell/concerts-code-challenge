from database import connect_db

class Band:
    def __init__(self,name,hometown):
        self.name = name
        self.hometown = hometown

    @classmethod
    def all_introductions(cls,conn):
        cursor = conn.cursor()
        cursor.execute('''
        SELECT v.city,b.name,b.hometown
        FROM   concerts c
        JOIN  bands b ON
        c.band_name = b.name
        JOIN  venues v ON
        c.venue_title = v.title
                ''')
        introductions = [
            f"Hello {row[0]}!!!!!
    We are {row[1]} and we're from {row[2]}"
        for row in cursor.fetchall() ]
        return introductions
    
    @classmethod
    def most_performances(cls,conn):
        cursor = conn.cursor()
        cursor.execute('''
        SELECT band_name),
    COUNT(*) as performance_count
        FROM concerts
        GROUP BY band_name
        ORDER BY
    performance_count DESC
        LIMIT 1
        ''')
        return cursor.fetchtone()[0]
