from operator import ge
from sql_queries import select_song_by_session_item, select_song_user_session, select_user_by_song
from etl import get_session

def query_one(session):
    
    try:
        rows = session.execute(select_song_by_session_item, (338, 4))
        for row in rows:
            print(row.artist, '\n', row.song_title, '\n', row.song_length)
            print('\n')
            print('\n')
    except Exception as e:
        print(e)

def query_two(session):
    
    try:
        rows = session.execute(select_song_user_session, (10, 182))
        for row in rows:
            print(row.artist, row.song_title, row.first_name, row.last_name)
    except Exception as e:
        print(e)

def query_three(session):
    
    try:   
        rows = session.execute(select_user_by_song, ('All Hands Against His Own'))
        for row in rows:
            print(row.first_name, row.last_name)
    except Exception as e:
        print(e)

def main():
    
    session, cluster = get_session()
    
    print('Question 1', '\n', '\n')
    query_one(session)
    print('\n')

    print('Question 2', '\n', '\n')
    query_two(session)
    print('\n')

    print('Question 3', '\n', '\n')
    query_three(session)

if __name__ == "__main__":
    main()
