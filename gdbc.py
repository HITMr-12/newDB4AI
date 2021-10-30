import pyodbc


class GDBC(object):
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.ans = None
    """
        与数据库的连接，返回ok或任何其它信息。
    """

    def connect(self):
        # 建立连接
        self.conn = pyodbc.connect('DRIVER={GaussMPP};SERVER=127.0.0.1;DATABASE=omm;UID=omm;PWD=Gauss@123')
        self.cursor = self.conn.cursor()

    """
        关闭与数据库的连接。
    """

    def close(self):
        #  关闭连接
        self.cursor.commit()
        self.cursor.close()
        self.conn.close()
        print("Successfully closed!")
        return True

    """
        执行sql。
    """

    def execute(self, sql: str):
        #  执行sql
        self.cursor.execute(sql)
        self.conn.commit()
    """
        取数据，返回。
    """

    def fetch(self):
        try:
            self.ans = self.cursor.fetchall()
        except:
            pass
        return self.ans


if __name__ == '__main__':
    gdbc = GDBC()
    gdbc.connect()
    gdbc.execute(f"select db4ai_sub('a', 'b','_14');")
    print(gdbc.fetch())
    print(gdbc.fetch())
    gdbc.close()
