import falcon


class Root:

    def on_get(self, req, resp):
        resp.body = '{"message": "Hola a los !"}'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        resp.body = '{"message": "Hola from post"}'
        resp.status = falcon.HTTP_200