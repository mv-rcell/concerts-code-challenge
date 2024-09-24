class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    def band(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bands WHERE id = ?", (self.band_id,))
        band = cursor.fetchone()
        conn.close()
        return Band(*band)

    def venue(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM venues WHERE id = ?", (self.venue_id,))
        venue = cursor.fetchone()
        conn.close()
        return Venue(*venue)

    def hometown_show(self):
        band = self.band()
        venue = self.venue()
        return band.hometown == venue.city

    def introduction(self):
        band = self.band()
        venue = self.venue()
        return f"Hello {venue.city}!!!!! We are {band.name} and we're from {band.hometown}"
	