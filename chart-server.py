# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import cx_Oracle
import pandas as pd
import pprint
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

#this is a function that is called within the index.html 


SQL_STATEMENT = "SELECT * FROM db.TABLE_1"#INSERT SQL STATEMENT HERE
USERNAME = 'admin' # insert username here
PASSWORD = 'pass' # insert pass here
IP_and_PORT = '127.0.0.1:1234' # insert IP address with port  here
SERVER_NAME = 'DB_SERVER_1' # insert server name here

@app.route('/chart_query')
def get_query():
    try:

        query = SQL_STATEMENT
        connection = cx_Oracle.connect(USERNAME'/'PASSWORD'@//'IP_and_PORT'/'SERVER_NAME)
        
        #for manually entered queries
        # query = request.args.get('query_input')
        df = pd.read_sql_query(query ,connection)
        df.rename(columns={'column_1': 'renamed_column_1'}, inplace=True)
        df = df.sort_values(by='column_2',ascending=False)
        df = df.head(10)
        json_object = df.to_json(orient='records')
        return json_object
    except Exception as e:
        return(str(e))



@app.route('/')
def index():
    return render_template('index.html')

    

if __name__ == '__main__':
    app.run()