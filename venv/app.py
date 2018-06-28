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

        self.add_route('/v1/user', v1.user.Wala())
        self.add_route('/v1/user/{user_id}', v1.user.Wala())

        self.add_route('/v1/account', v1.account.AccountItem())
        self.add_route('/v1/account/{account_id}', v1.account.AccountItem())

        # self.add_route('/v1/user', v1.user.Collection())
        # self.add_route('/v1/user', v1.user.Collection())
        # self.add_route('/v1/account', v1.account.Item())
        # self.add_route('/v1/account', v1.account.Collection())
