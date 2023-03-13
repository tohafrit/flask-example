import os
from flask import Flask
from flask import request, make_response
import mysql.connector
import socket
from time import strftime
import logging


class DBManager:
    def __init__(self, database=os.environ.get("SQL_DATABASE"), 
                 host=os.environ.get("SQL_HOST"), 
                 user=os.environ.get("SQL_USER"), 
                 password_file=os.environ.get("SQL_PASSWORD_FILE")):
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user, 
            password=pf.read().strip(),
            host=host,
            database=database,
            auth_plugin='mysql_native_password'
        )
        pf.close()
        self.cursor = self.connection.cursor()
    
    def increase(self, counter, datetime, client_ip, internal_ip):
        query = '''INSERT INTO access_log (id, visit_count, record_datetime, client_ip, internal_ip) 
        VALUES (%s, %s, %s, %s, %s);
        '''
        self.cursor.execute(query, (None, counter, datetime, client_ip, internal_ip))
        self.connection.commit()
    
    def showcount(self):
        self.cursor.execute('SELECT MAX(visit_count) FROM access_log')
        maximum = ''
        for row in self.cursor.fetchall():
            maximum = str(row[0])
        return maximum


app = Flask(__name__)
app.debug = True

logging.basicConfig(filename='logs/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

conn = None
counter = 1

@app.route('/')
def main():
    app.logger.info('Main page')
    internal_ip = socket.gethostbyname(socket.gethostname())

    cookie_key = 'internal_ip'
    resp = make_response(internal_ip)
    if request.cookies.get(cookie_key) != internal_ip:
        resp.set_cookie(cookie_key, internal_ip, 1 * 60)

    global conn, counter
    if not conn:
        conn = DBManager()

    counter = counter + 1
    conn.increase(counter, strftime('%Y-%m-%d %H:%M:%S'), request.remote_addr, internal_ip)

    return resp

@app.route('/showcount')
def showcount():
    app.logger.info('Showcount page')
    global conn
    if not conn:
        conn = DBManager()

    return conn.showcount()
