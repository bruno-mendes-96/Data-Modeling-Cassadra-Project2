from cassandra.cluster import Cluster
from cql_queries import create_table_queries, drop_table_queries

def create_cluster():
    """
    Creates and connects to the sparkify.
    Returns the cluster and session.
    """

    cluster = Cluster(['127.0.0.1'])

    session = cluster.connect()

    session.execute("DROP KEYSPACE IF EXISTS sparkify")
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS sparkify 
        WITH REPLICATION = 
        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
    """
    ) 

    session.set_keyspace('sparkify')

    return cluster, session

def drop_tables(session):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """

    for query in drop_table_queries:
        session.execute(query)

def create_tables(session):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """

    for query in create_table_queries:
        session.execute(query)

def main():
    """
    Create cluster and session.

    Drops (if exists) and Creates the sparkify database. 
    
    Drops all the tables.  
    
    Creates all tables needed.
    
    Finally, shutdown session and cluster
    """

    cluster, session = create_cluster()

    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()
