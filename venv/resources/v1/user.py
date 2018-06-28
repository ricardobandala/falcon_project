import json
import falcon
from models.user import UserModel, UserSchema


class Item:

    def on_get(self, req, resp, user_id):
        query = req.context['session'].query(UserModel)
        query = query.filter(UserModel.id == user_id)
        user = query.one_or_none()
        if not user:
            raise falcon.HTTPNotFound()
        resp.body = json.dumps(UserSchema().dump(user).data)

    def on_post(self, req, resp, user_id):
        query = req.context['session'].query(UserModel)
        query = query.filter(UserModel.id == user_id)
        user = query.one_or_none()
        if not user:
            raise falcon.HTTPNotFound()
        resp.body = json.dumps(UserSchema().dump(user).data)


class Collection:
    pass
