from cql_queries import select_song_by_session_item, select_song_user_session, select_user_by_song
from etl import get_session

def query_one(session):
    """
    Get reponse to the following question:

    * 1. Give me the artist, song title and song's length in the music app history that was heard during 
    sessionId = 338, and itemInSession  = 4
    """

    try:
        rows = session.execute(select_song_by_session_item, (338, 4))
        for row in rows:
            print(row.artist, '\n', row.song_title, '\n', row.song_length)
            print('\n')
            print('\n')
    except Exception as e:
        print(e)

def query_two(session):
    """
    Get reponse to the following question:

    * 2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and 
    last name) for userid = 10, sessionid = 182
    """
    
    try:
        rows = session.execute(select_song_user_session, (10, 182))
        for row in rows:
            print(row.artist, row.song_title, row.first_name, row.last_name)
    except Exception as e:
        print(e)

def query_three(session):
    """
    Get reponse to the following question:

    * 3. Give me every user name (first and last) in my music app history who listened to the song 'All 
    Hands Against His Own'
    """
    
    try:
        song_title = 'All Hands Against His Own'
        query = select_user_by_song % song_title
        rows = session.execute(query)
        for row in rows:
            print(row.first_name, row.last_name)
    except Exception as e:
        print(e)

def main():
    """
    Get all response to business questions

    * 1. Give me the artist, song title and song's length in the music app history that was heard during 
    sessionId = 338, and itemInSession  = 4

    * 2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and 
    last name) for userid = 10, sessionid = 182
        
    * 3. Give me every user name (first and last) in my music app history who listened to the song 'All 
    Hands Against His Own'
    """

    session, cluster = get_session()
    
    print('\n')
    print('Question 1', '\n', '\n')
    query_one(session)

    print('Question 2', '\n', '\n')
    query_two(session)

    print('Question 3', '\n', '\n')
    query_three(session)

if __name__ == "__main__":
    main()
