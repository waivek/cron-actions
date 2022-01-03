def sqlite3_test():
    import sqlite3

    pysqlite_version = sqlite3.version
    sqlite_version = sqlite3.sqlite_version
    print(f"PYSQLITE: {pysqlite_version}")
    print(f"SQLITE  : {sqlite_version}")

    db_path = "sqlite_test.db"
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS nba_players;")
    cursor.execute("CREATE TABLE nba_players (name TEXT PRIMARY KEY, team TEXT);")
    cursor.execute("INSERT INTO nba_players (name, team) VALUES (?, ?);", ("LeBron James", "Cleaveland Cavaliers"))
    row = cursor.execute("SELECT * FROM nba_players LIMIT 1;").fetchone()
    print(row["name"], row["team"])
    cursor.execute("INSERT INTO nba_players (name, team) VALUES (?, ?) ON CONFLICT DO UPDATE SET (team)=(excluded.team);", ("LeBron James", "Los Angeles Lakers"))
    row = cursor.execute("SELECT * FROM nba_players LIMIT 1;").fetchone()
    print(row["name"], row["team"])

sqlite3_test()
