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

        resp.body = UserSchema(only=('username', 'is_active')).dumps(user)

    def on_post(self, req, resp):
        data = req.stream.read()
        data = json.loads(data)
        data = UserSchema().load(data).data
        req.context['session'].add(data)
        req.context['session'].commit()

    def on_put(self, req, resp, user_id):
        data = UserSchema().load(json.loads(req.stream.read())).data
        req.context['session'].add(data)
        req.context['session'].commit()


class Collection:
    pass
