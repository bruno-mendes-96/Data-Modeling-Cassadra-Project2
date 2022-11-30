create_song_session_item = """
    CREATE TABLE IF NOT EXISTS song_by_session_item (
        artist TEXT,
        song_title TEXT,
        song_length DECIMAL,
        session_id INT,
        item_in_session INT,
        PRIMARY KEY (session_id, item_in_session)
    )
"""

create_song_user_session = """
    CREATE TABLE IF NOT EXISTS song_by_user_session (
        song_title TEXT,
        session_id INT,
        item_in_session INT,
        user_id INT,
        first_name TEXT,
        last_name TEXT,
        PRIMARY KEY((user_id, session_id), item_in_session)
    )
"""

create_user_by_song = """
    CREATE TABLE IF NOT EXISTS user_by_song (
        user_id INT,
        first_name TEXT,
        last_name TEXT,
        song_title TEXT,
        PRIMARY KEY (song_title, user_id)
    )
"""

insert_song_session_item = """
    INSERT INTO song_session_item (artist, song_title, song_length, session_id, item_in_session)
    VALUES (%s, %s, %s, %s, %s)
"""

insert_song_user_session = """
    INSERT INTO song_by_user_session (song_title, session_id, item_in_session, user_id, first_name, last_name)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

insert_user_by_song = """
    INSERT INTO user_by_song (user_id, first_name, last_name, song_title)
    VALUES (%s, %s, %s, %s)
"""

# session_id = 338, item_in_session = 4
select_song_by_session_item = """
    SELECT 
        artist, 
        song_title,
        song_length 
    FROM song_session 
    WHERE session_id = %s and item_in_session = %s
"""

# user_id = 10, session_id = 182
select_song_user_session = """
    SELECT 
        artist,
        song_title,
        firstName,
        lastName 
    FROM song_user_session 
    WHERE userId = %s AND sessionId = %s
"""

# song_title = 'All Hands Against His Own'
select_user_by_song = """
    SELECT 
        first_name,
        last_name
    FROM user_song
    WHERE song_title = %s
"""

drop_song_session_item = 'DROP TABLE IF EXISTS song_by_session_item'
drop_song_user_session = 'DROP TABLE IF EXISTS song_by_user_session'
drop_user_by_song = 'DROP TABLE IF EXISTS user_by_song'

create_table_queries = [create_song_session_item, create_song_user_session, create_user_by_song]
drop_table_queries = [drop_song_session_item, drop_user_by_song, drop_user_by_song]
