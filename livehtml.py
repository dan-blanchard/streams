#!/usr/bin/env python

#
# simple static Flask fileserving app
#
from __future__ import print_function

from flask import Flask

app = Flask(__name__,
            static_folder="_build/slides",
            static_url_path="")

@app.route("/")
def root():
    return app.send_static_file("index.html")

#
# livereload server
#
from livereload import Server

def make_livereload_server(wsgi_app):
    server = Server(wsgi_app)

    watch_patterns = (
        "index.rst",
        "/_static/*"
    )

    build_cmd = "make slides"

    print("Files being monitored:")

    for pattern in watch_patterns:
        print("Pattern: ", pattern)
        server.watch(pattern, build_cmd)
        print()

    return server

def main():
    # wire livereload to Flask via wsgi
    flask_wsgi_app = app.wsgi_app
    server = make_livereload_server(flask_wsgi_app)
    # serve application
    server.serve(host='0.0.0.0')

if __name__ == "__main__":
    main()
