import psycopg2
from psycopg2.extras import execute_values, RealDictCursor

import config
from src import sql


class Database:
    """Configurations"""
    def __init__(self):
        self.host = config.DATABASE_HOST
        self.username = config.DATABASE_USERNAME
        self.password = config.DATABASE_PASSWORD
        self.port = config.DATABASE_PORT
        self.dbname = config.DATABASE_NAME
        self.conn = None

    def connect(self):
        """Connect to postgres database"""
        if not self.conn:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    dbname=self.dbname
                )
            except psycopg2.DatabaseError as e:
                config.logging.debug(e)
                raise e
            finally:
                config.logging.info('Connection opened successfully')

    def check_exists(self, vars=None):
        """Run SQL query to select rows from table"""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(sql.query_exists, vars=vars)
            record = cur.fetchone()
            cur.close()
            return record

    def update(self, vars=None):
        """Run SQL query to update rows from table"""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(sql.query_update, vars=vars)
            self.conn.commit()
            cur.close()
            return f"{cur.rowcount} rows affected"

    def add(self, vars=None):
        """Run SQL query to add rows from table"""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(sql.query_add, vars=vars)
            self.conn.commit()
            cur.close()

    def first_add(self, vars=None):
        """Run SQL query to add rows from table"""
        self.connect()
        with self.conn.cursor() as cur:
            execute_values(cur, sql.query_add, vars)
            self.conn.commit()
            cur.close()

    def get_sheets(self, vars=None):
        """Run SQL query to add rows from table"""
        self.connect()
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql.query_get)
            record = cur.fetchall()
            cur.close()
            return record

    def close(self):
        self.conn.close()
