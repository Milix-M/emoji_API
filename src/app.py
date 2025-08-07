import falcon
from wsgiref.simple_server import make_server
from .dto.emoji_parameter import EmojiParamDTO

api = falcon.App()
api.add_route("/emoji", EmojiParamDTO())


if __name__ == "__main__":
    with make_server("", 8000, api) as httpd:
        print("Serving on port 8000...")

        # Serve until process is killed
        httpd.serve_forever()
