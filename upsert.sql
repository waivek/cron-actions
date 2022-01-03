SELECT sqlite_version();
DROP TABLE IF EXISTS nba_players;
CREATE TABLE nba_players (name TEXT PRIMARY KEY, team TEXT);
INSERT INTO nba_players (name, team) VALUES ("LeBron James", "Cleaveland Cavaliers");
SELECT * FROM nba_players LIMIT 1;
INSERT INTO nba_players (name, team) VALUES ("LeBron James", "Los Angeles Lakers") ON CONFLICT DO UPDATE SET (team)=(excluded.team);
SELECT * FROM nba_players LIMIT 1;

