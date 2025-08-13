class ConstantMeta(type):
    """Metaclass to prevent reassignment of constants."""
    def __setattr__(cls, key, value):
        """Prevents reassignment of attributes once set."""
        if key in cls.__dict__:
            raise AttributeError("Cannot reassign constant")
        super().__setattr__(key, value)


class Fonts(metaclass=ConstantMeta):
    """Defines constants related to fonts."""

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
