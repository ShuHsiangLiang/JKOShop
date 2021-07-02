from app.common.database import JKOShopUserSQL
from app.common import Message


class UserService:
	def __init__(self):
		self.db = JKOShopUserSQL()

	def register(self, username: str):
		b = self.db.get_user_name()
		if username in b:
			return "Error - user already existing"

		self.db.create_user_name(username)
		return Message.SUCCESS.value
