import os, sqlite3, pandas as pd

os.makedirs("data", exist_ok=True)
db_path = r"data\gpu_value.db"

conn = sqlite3.connect(db_path)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS gpus (
        model TEXT PRIMARY KEY,
        vram_gb REAL,
        bus_width_bits INTEGER,
        tdp_w REAL,
        release_year INTEGER
    )
""")

cur.execute("INSERT OR REPLACE INTO gpus (model, vram_gb, bus_width_bits, tdp_w, release_year) VALUES (?, ?, ?, ?, ?)", 
    ("Geforce RTX 4070",12.0, 192, 200.0, 2023)
)

conn.commit()

for row in cur.execute("""
    SELECT * 
    FROM gpus
"""):
    print(row)
    
df = pd.read_sql_query("SELECT * FROM gpus", conn)

conn.close()

print(df)

