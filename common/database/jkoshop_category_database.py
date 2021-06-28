from JKOShop.configurations import JKOShopConfig

from .database import Database


class JKOShopCategoryDatabase(Database):

    def __init__(self):
        super().__init__(JKOShopConfig.Database)

    def delete_platform_extra_jko_fee_rate(self, platform_id: int):
        args = {
            'platform_id': platform_id
        }
        sql = "DELETE FROM platform_extra_jko_fee_rate_tab WHERE platform_id = %(platform_id)s;"
        self._connection.execute_modify_sql(sql, args)

    def delete_api_key(self, platform_id: int):
        args = {
            'platform_id': platform_id
        }
        sql = "DELETE FROM api_key_tab WHERE platform_id = %(platform_id)s;"
        self._connection.execute_modify_sql(sql, args)

    def delete_platform(self, platform_id: int):
        args = {
            'platform_id': platform_id
        }
        sql = "DELETE FROM platform_tab WHERE id = %(platform_id)s;"
        self._connection.execute_modify_sql(sql, args)

    def get_platform(self, platform_id: int):
        args = {
            'platform_id': platform_id
        }
        sql = "SELECT * FROM platform_tab WHERE id = %(platform_id)s;"
        res = self._connection.execute_select_sql(sql, args)
        return res

    def get_platform_api_keys(self, platform_id: int, valid: int = None):
        args = {
            'platform_id': platform_id,
            'valid': valid
        }
        sql = "SELECT * FROM api_key_tab WHERE platform_id = %(platform_id)s"
        if valid in [0, 1]:
            sql += " AND valid = %(valid)s;"
        res = self._connection.execute_select_sql(sql, args, fetchall=True)
        return res
