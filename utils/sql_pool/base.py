from django.db.backends.mysql.base import (Database, 
    DatabaseWrapper as BaseDatabaseWrapper)
from django.conf import settings
    
# import MySQLdb as Database
import sqlalchemy.pool as pool
from sqlalchemy.pool import QueuePool

SQLALCHEMY_QUEUEPOOL = {
    'pool_size': 10,
    'max_overflow': 10,
    'timeout': 5,
    'recycle': 119,
}

Database = pool.manage(Database, poolclass=QueuePool, **SQLALCHEMY_QUEUEPOOL)


class DatabaseWrapper(BaseDatabaseWrapper):
    def get_new_connection(self, conn_params):
        # return a mysql connection
        databases = settings.DATABASES
        alias = None
        for _alias in databases:
            if databases[_alias]['NAME'] == conn_params['db']:
                alias = _alias
                break
        client_flag = conn_params['client_flag']

        conn_params = databases[alias]
        return Database.connect(
            host=conn_params['HOST'],
            port=conn_params['PORT'],
            user=conn_params['USER'],
            db=conn_params['NAME'],
            passwd=conn_params['PASSWORD'],
            use_unicode=True,
            charset='utf8',
            client_flag=client_flag,
            sql_mode='STRICT_TRANS_TABLES',
        )
