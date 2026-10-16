import configparser
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

config = configparser.ConfigParser()
config.read("config/app.conf")


def student_text():
    name = os.getenv("STUDENT_NAME", config["student"]["name"])
    surname = os.getenv("STUDENT_SURNAME", config["student"]["surname"])
    group = os.getenv("STUDENT_GROUP", config["student"]["group"])
    student_id = os.getenv("STUDENT_ID", config["student"]["student_id"])

    return (
        f"Name: {name}\n"
        f"Surname: {surname}\n"
        f"Group: {group}\n"
        f"Student ID: {student_id}\n"
        f"Course: {config['student']['course']}\n"
    )


class StudentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        content = student_text().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    port = config.getint("app", "port")
    server = HTTPServer(("0.0.0.0", port), StudentHandler)
    print(f"Application started on port {port}", flush=True)
    server.serve_forever()