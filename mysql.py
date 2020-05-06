import pymysql
import config

class mysql:
    connection = None
    cursor = None

    _config=config.config().mysql()
    
    def __init__(self):
        self.connection = pymysql.connect(self._config['host'], self._config['username'], self._config['password'], self._config['database'])
        self.cursor = self.connection.cursor()
    
    def __del__(self):
        return self.connection.close()

    def getmaxid(self,database):
        sql="SELECT MAX(id) AS max_id FROM '%s';"%(database)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        
        maxid=0
        for row in result:
            if row[0] is None:
                maxid=0
            else:
                maxid=int(row[0])+1
        return maxid

    def get(self,index,index2):
        return 0

def __init__():
    pass

if __name__=='__main__':
    pass