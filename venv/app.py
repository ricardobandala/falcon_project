import falcon
from components import Database, Content
from resources import v1


class App(falcon.API):

    def __init__(self):

        self.database_component = Database()
        self.content_type_component = Content(content_type='application/json')

        super().__init__(middleware=[
            self.database_component,
            self.content_type_component
        ])

        self.add_route('/', v1.root.Root())

        user_item_resource = v1.user.Item()
        self.add_route('/v1/user', user_item_resource)
        self.add_route('/v1/user/{user_id:int}', user_item_resource)

        account_item_resource = v1.account.Item()
        self.add_route('/v1/account', account_item_resource)
        self.add_route('/v1/account/{account_id:int}', account_item_resource)

        # self.add_route('/v1/user', v1.user.Collection())
        # self.add_route('/v1/user', v1.user.Collection())
        # self.add_route('/v1/account', v1.account.Item())
        # self.add_route('/v1/account', v1.account.Collection())
