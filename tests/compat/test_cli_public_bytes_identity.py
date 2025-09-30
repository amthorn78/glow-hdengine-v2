import json, subprocess, sys

def test_cli_public_bytes_two_run():
    cmd = [sys.executable, "scripts/hdctl.py", "showcompat",
           "--birthdate","2000-01-01","--birthtime","12:00","--place","Tallinn, EE","--tz","Europe/Tallinn",
           "--birthdate2","2001-02-03","--birthtime2","13:30","--place2","Paris, FR","--tz2","Europe/Paris"]
    out1 = subprocess.check_output(cmd)
    out2 = subprocess.check_output(cmd)
    assert out1 == out2 and out1.endswith(b"\n") and not out1.endswith(b"\n\n")
    j = json.loads(out1.decode("utf-8"))
    assert "band" in j and "categories" in j
