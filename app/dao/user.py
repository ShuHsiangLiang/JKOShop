from app.core.database import db
from app.models.user import User


class UserDAO:
    @staticmethod
    def create_user(form):
        with db.auto_commit():
            user = User.create(
                commit=False,
                username=getattr(form, 'username', None)
            ) 
            if (hasattr(form, 'username')):
                User.abort_repeat(identifier=form.username, msg='Error - user already existing')
                User.create(commit=False, user_id=user.id, type=ClientTypeEnum.USERNAME.value, verified=1,
                                identifier=form.username, password=form.password)