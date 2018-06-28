from wsgiref.simple_server import make_server
from app import App


def error_handler(ex, req, resp, params):
    raise ex


if __name__ == '__main__':

    application = App()
    application.add_error_handler(Exception, error_handler)

    # TODO, If I use something like watchdog to reload on changes I loose my session?
    httpd = make_server('localhost', 8181, application)

    # httpd.handle_request()
    httpd.serve_forever(poll_interval=0.5)
