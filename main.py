 def insert_sample_data():
conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()

    
    cursor.execute("INSERT INTO bands (name, hometown) VALUES (?, ?)", ("The Rockers", "Los Angeles"))
    cursor.execute("INSERT INTO bands (name, hometown) VALUES (?, ?)", ("Jazz Band", "New York"))

    
    cursor.execute("INSERT INTO venues (title, city) VALUES (?, ?)", ("Stadium", "Los Angeles"))
    cursor.execute("INSERT INTO venues (title, city) VALUES (?, ?)", ("The Jazz Club", "New York"))

    
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", (1, 1, "2024-09-01"))
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", (2, 2, "2024-09-02"))

    conn.commit()
    conn.close()

insert_sample_data()
