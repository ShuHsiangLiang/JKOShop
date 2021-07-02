from app.configurations import JKOShopConfig

from .database import Database

class JKOShopUserSQL(Database):

    def __init__(self):
        super().__init__(JKOShopConfig.Database)
    
    def create_user_name(self, name: str):
        args = {
            'name': name
        }
        sql = "INSERT INTO user_tab (name) VALUES (%(name)s);"
        self._connection.execute_modify_sql(sql, args)

    def get_user_name(self):
        sql = "SELECT name FROM user_tab;"
        res = self._connection.execute_select_sql(sql)
        return res
    
