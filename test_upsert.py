
def sqlite3_test():
    from db import db_init, sqlite3
    pysqlite_version = sqlite3.version
    sqlite_version = sqlite3.sqlite_version
    print(f"PYSQLITE: {pysqlite_version}")
    print(f"SQLITE  : {sqlite_version}")

    cursor, connection = db_init("sqlite_test.db")
    cursor.execute("DROP TABLE IF EXISTS nba_players;")
    cursor.execute("CREATE TABLE nba_players (name TEXT PRIMARY KEY, team TEXT);")
    cursor.execute("INSERT INTO nba_players (name, team) VALUES (?, ?);", ("LeBron James", "Cleaveland Cavaliers"))
    row = cursor.execute("SELECT * FROM nba_players LIMIT 1;").fetchone()
    print(row["name"], row["team"])
    cursor.execute("INSERT INTO nba_players (name, team) VALUES (?, ?) ON CONFLICT DO UPDATE SET (team)=(excluded.team);", ("LeBron James", "Los Angeles Lakers"))
    row = cursor.execute("SELECT * FROM nba_players LIMIT 1;").fetchone()
    print(row["name"], row["team"])

sqlite3_test()
