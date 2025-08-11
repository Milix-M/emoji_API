import falcon
from wsgiref.simple_server import make_server
from .dto.emoji_parameter import EmojiParamDTO
from .dto.font_resorce import EmojiResource

api = falcon.App(cors_enable=True)
api.add_route("/emoji", EmojiParamDTO())
api.add_route("/fonts", EmojiResource())


if __name__ == "__main__":
    with make_server("", 8000, api) as httpd:
        print("Serving on port 8000...")

        # Serve until process is killed
        httpd.serve_forever()
