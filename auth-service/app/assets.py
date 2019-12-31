from flask_assets import Bundle, Environment


def register_assets(app):
    css = Bundle(
        "css/style.css",
        filters="cssmin",
        output="public/css/common.css"
    )

    js = Bundle(
        "js/plugins.js",
        filters="jsmin",
        output="public/js/common.js"
    )

    assets = Environment(app)

    assets.register("js_all", js)
    assets.register("css_all", css)
