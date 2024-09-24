class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    def concerts(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM concerts WHERE venue_id = ?", (self.id,))
        concerts = cursor.fetchall()
        conn.close()
        return concerts

    def bands(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT b.* FROM bands b
            JOIN concerts c ON b.id = c.band_id
            WHERE c.venue_id = ?
        ''', (self.id,))
        bands = cursor.fetchall()
        conn.close()
        return bands

    def concert_on(self, date):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM concerts WHERE venue_id = ? AND date = ?", (self.id, date))
        concert = cursor.fetchone()
        conn.close()
        return concert

    def most_frequent_band(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT b.*, COUNT(c.id) as performance_count FROM bands b
            JOIN concerts c ON b.id = c.band_id
            WHERE c.venue_id = ?
            GROUP BY b.id
            ORDER BY performance_count DESC
            LIMIT 1
        ''', (self.id,))
        most_frequent_band = cursor.fetchone()
        conn.close()
        return Band(*most_frequent_band)