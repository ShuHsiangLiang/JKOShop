from app.configurations import JKOShopConfig

from .database import Database


class JKOShopCategorySQL(Database):

    def __init__(self):
        super().__init__(JKOShopConfig.Database)

    def get_categroy_name(self):
        sql = "SELECT name FROM category_tab"
        res = self._connection.execute_select_sql(sql)
        return res
    
    def create_category(self, name: str):
        args = {
            'name': name,
        }
        sql = "INSERT INTO category_tab (name) VALUES (%(name)s)"
        self._connection.execute_modify_sql(sql, args)

    def get_top_categroy(self):
        sql = "SELECT * FROM category_tab ORDER BY count DESC LIMIT 1"
        res = self._connection.execute_select_sql(sql)
        return res
