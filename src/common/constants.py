class ConstantMeta(type):
    def __setattr__(cls, key, value):
        if key in cls.__dict__:
            raise AttributeError("Cannot reassign constant")
        super().__setattr__(key, value)


class Fonts(metaclass=ConstantMeta):
    """フォントに関する定数を定義するクラス"""

    FONT_NAME_PATH_MAPPING = {
        "M+ 1p black": {
            "path": "/fonts/MPLUS1p-Black.ttf",
            "typeface": "Gothic",
        },
        "Rounded M+ 1p black": {
            "path": "/fonts/rounded-mplus-1p-black.ttf",
            "typeface": "Rounded Gothic",
        },
        "Noto Sans JP": {
            "path": "/fonts/NotoSansJP-Black.ttf",
            "typeface": "Gothic",
        },
        "Sawarabi Mincho": {
            "path": "/fonts/SawarabiMincho-Regular.ttf",
            "typeface": "Mincho",
        },
        "YuseiMagic": {
            "path": "/fonts/YuseiMagic-Regular.ttf",
            "typeface": "Rounded Gothic",
        },
    }
