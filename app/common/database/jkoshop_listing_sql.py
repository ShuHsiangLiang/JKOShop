from app.configurations import JKOShopConfig

from .database import Database


class JKOShopListingSQL(Database):

    def __init__(self):
        super().__init__(JKOShopConfig.Database)

    def create_listing(
            self, user_name: str, title: str, description: str, price: int, category: str):
        args = {
            'user_name': user_name,
            'title': title,
            'description': description,
            'price': price,
            'category': category 
        }
        sql = "INSERT INTO listing_tab (username, title, description, price, category) \
               VALUES (%(user_name)s, %(title)s, %(description)s, %(price)s, %(category)s)"    
        self._connection.execute_modify_sql(sql, args)

        # 增加類別總數
        sql = "UPDATE category_tab SET count = count + 1"
        self._connection.execute_modify_sql(sql, args)


    def delete_listing(self, user_name: str, listing_id: int):
        args = {
            'user_name': user_name,
            'listing_id': listing_id
        }
        sql = "DELETE FROM listing_tab WHERE username = %(user_name)s AND id = %(listing_id)s;"
        self._connection.execute_modify_sql(sql, args)

        # 減少類別總數
        sql = "UPDATE category_tab SET count = count - 1"
        self._connection.execute_modify_sql(sql, args)


    def get_listing(self, user_name: str, listing_id: int):
        args = {
            'user_name': user_name,
            'listing_id': listing_id
        }
        sql = "SELECT * FROM listing_tab WHERE username = %(user_name)s AND id = %(listing_id)s;"
        res = self._connection.execute_select_sql(sql, args)
        return res

    def get_category(self, user_name: str, category: str):
        args = {
            'user_name': user_name,
            'category': category
        }
        sql = "SELECT * FROM listing_tab WHERE username = %(user_name)s AND category = %(category)s;"
        res = self._connection.execute_select_sql(sql, args)
        return res
