# import json
# import falcon
# from models.account import AccountModel, AccountSchema
#
#
# class Item:
#
#     def on_get(self, req, resp, account_id):
#         query = req.context['session'].query(AccountModel)
#         query = query.filter(AccountModel.id == account_id)
#         account = query.one_or_none()
#         if not account:
#             raise falcon.HTTPNotFound()
#         resp.body = json.dumps(AccountSchema().dump(account).data)
#
#     def on_post(self, req, resp):
#         schema = AccountSchema()
#         data = schema.load(json.loads(req.stream.read())).data
#         req.context['session'].add(data)
#         req.context['session'].commit()
#
#
# class Collection:
#     pass
