
import sqlite3

class Band:
    def __init__(self, id, name, hometown):
        self.id = 
        self.name = name
        self.hometown = hometown

    def concerts(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM concerts WHERE band_id = ?", (self.id,))
        concerts = cursor.fetchall()
        conn.close()
        return concerts

    def venues(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT v.* FROM venues v
            JOIN concerts c ON v.id = c.venue_id
            WHERE c.band_id = ?
        ''', (self.id,))
        venues = cursor.fetchall()
        conn.close()
        return venues

    def play_in_venue(self, venue_title, date):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM venues WHERE title = ?", (venue_title,))
        venue_id = cursor.fetchone()
        if venue_id:
            cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", 
                           (self.id, venue_id[0], date))
            conn.commit()
        conn.close()

    def all_introductions(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT v.city FROM venues v
            JOIN concerts c ON v.id = c.venue_id
            WHERE c.band_id = ?
        ''', (self.id,))
        cities = cursor.fetchall()
        introductions = [
            f"Hello {city[0]}!!!!! We are {self.name} and we're from {self.hometown}"
            for city in cities
        ]
        conn.close()
        return introductions

    @staticmethod
    def most_performances():
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT b.*, COUNT(c.id) as performance_count FROM bands b
            JOIN concerts c ON b.id = c.band_id
            GROUP BY b.id
            ORDER BY performance_count DESC
            LIMIT 1
        ''')
        most_performed_band = cursor.fetchone()
        conn.close()
        return Band(*most_performed_band)