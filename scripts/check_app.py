import runpy
import sys
import time
from unittest.mock import patch
from urllib.error import URLError
from urllib.request import urlopen

app = runpy.run_path("app/main.py")
expected = (
    "Name: Elmira\n"
    "Surname: Kamilzhanova\n"
    "Group: IT2-2304\n"
    "Student ID: 37713\n"
    "Course: DevOps\n"
)

assert app["student_text"]() == expected, "Personal information check failed"
with patch.dict("os.environ", {"STUDENT_NAME": "OverrideCheck"}):
    assert "Name: OverrideCheck\n" in app["student_text"](), "Environment check failed"

if len(sys.argv) > 1:
    for attempt in range(10):
        try:
            with urlopen(sys.argv[1], timeout=2) as response:
                actual = response.read().decode("utf-8")
            break
        except URLError:
            if attempt == 9:
                raise
            time.sleep(1)
    assert actual == expected, "HTTP response check failed"
    print("HTTP check passed")

print(expected, end="")
print("Application checks passed")