import pandas as pd
import os
import glob
from sql_queries import *
from cassandra.cluster import Cluster
import csv

def get_filepath_list():
    """
    This function get all filenames of the files inside event_data folder - The filepaths are returned.

    OUTPUT
        * file_path_list - List that contained all filepaths of event_data folder.
    """
        
    # Get your current folder and subfolder event data
    filepath = os.getcwd() + '/event_data'

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):

    # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root,'*'))
    return file_path_list

def write_event_datafile(file_path_list, output_filename):
    """
    This function read all event files and concat all lines into one unique csv.

    INPUT
        * file_path_list - List that contained all filepaths of event_data folder.
        * output_filename - Name of the output csv
    """

    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = [] 
        
    # for every filepath in the file path list 
    for f in file_path_list:

    # reading csv file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)
            
    # extracting each data row one by one and append it        
            for line in csvreader:
                full_data_rows_list.append(line) 

    # creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the \
    # Apache Cassandra tables
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open(output_filename, 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','first_name','gender','item_in_session','last_name','length',\
                    'level','location','session_id','song','user_id'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))

def get_session():
    """
    This function instantiates the cluster and creates a session.

    OUTPUT
        * session - Connection in cluster.
        * cluster - Cluster.
    """

    cluster = Cluster(['127.0.0.1'])

    session = cluster.connect()
    session.set_keyspace('sparkify')

    return session, cluster

def etl(output_filename):
    """
    This function reads the csv and iterates over the rows.
    Function get_session are executed and the session are used to execute insert queries.
    The respective columns are selected and inserted into cassandra tables.

    INPUT
        * output_filename - CSV with all event_data concatenated.

    RETURNS nothing.
    """

    df = pd.read_csv(output_filename)
    session, cluster = get_session()

    for i, line in df.iterrows():
        session.execute(insert_song_session_item, (line.artist, line.song, line.length, line.session_id, line.item_in_session))
        session.execute(insert_song_user_session, (line.song, line.session_id, line.item_in_session, line.user_id, line.first_name, line.last_name))
        session.execute(insert_user_by_song, (line.user_id, line.first_name, line.last_name, line.song))

def main():
    """
    This function extract, transform and load all data.

    First, all CSVs are concatenated ans saved into one archive with "output_filename" name.

    The function "etl" are executed and cassandra tables are populated with event_data.
    """

    filepath_list = get_filepath_list()
    output_filename = 'event_datafile_new.csv'
    write_event_datafile(filepath_list, output_filename)
    etl(output_filename)

if __name__ == "__main__":
    main()
