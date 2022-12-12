<h1> Project: Data Modeling with Cassandra </h1>

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

This is a data engineering project, whose purpose is to create an Apache Cassandra database that queries can be runned on song play data to answer business questions. An ETL pipeline was developed to extract, transform and load the CSVs into the NoSQL database.


<h1> Files description </h1>

The <code>images</code> folder is used for the purpose of storing the images. It has an unique file that brings the head of CSVs.

The file <code>cql_queries.py</code> contains the cql queries that are executed during pipeline execution. In summary, there are DROP, CREATE, SELECT and INSERT statements.

The <code>create_tables.py</code> file contains functions that instanciate the cluster, create the session and execute the DDLs statements.

<code>etl_template.ipynb</code> is a jupyter notebook that allows the idealization and partial construction of the pipeline with easy debug.

The <code>etl.py</code> file contains functions that extract, transform and load the CSV files into the NoSQL database.

<code>test.py</code> is a file that gives answers business questions.

<h1> Data description </h1>

Event_data brings information regarding the execution of songs by users in the application:

![Alt text](images/image_event_datafile_new.jpg "CSVs")

The instances of these two objects were extract, transform and load into the NoSQL database.

<h1> Data Model </h1>

Three tables were created based on the queries that will be executed on the NoSQL database:

song_by_session_item - Give the artist, song title and other song information listened in the music app history 
during a session based on session_id and item_in_session;

song_by_user_session - Give the name of artist, song (sorted by itemInSession) and user (first and last name)
based on user_id and session_id;

user_by_song - Give user information that listened a specific song.

<h1> Running the Pipeline </h1>

1 - Install dependencies;

2 - Run <code>create_tables.py</code> to create the environment and the tables;

3 - Run <code>etl.py</code> to extract and transform the CSVs files and load into NoSQL database;

4 - Use <code>etl_template.ipynb</code> to debug and correct functions of <code>etl.py</code> if necessary.

5 - Run <code>test.py</code> to get the response to the following business questions:

    - Give me the artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4.

    - Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182.

    - Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'.
