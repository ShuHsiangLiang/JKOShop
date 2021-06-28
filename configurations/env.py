from . import default


class EnvironmentConfig(default.EnvironmentConfig):
    ENV = "SIT"


class JKOShopConfig(default.JKOShopConfig):

    class Database:
        driver = "mysql"
        host = "127.0.0.1"
        port = "3306"
        user = "root"
        password = "diligent.30616"
        database = "JKOShop"
