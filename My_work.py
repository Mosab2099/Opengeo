import urllib.request, urllib.parse, urllib.error
import requests as req
import http
import sqlite3
import json as js
import time
import ssl
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect("myopengeo.sqlite")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS 'Locations' (
          address TEXT UNIQUE,
          geo_data TEXT
          )"""
)
i = 0
with open("where.data") as f:
    for line in f:
        if i > 100:
            break
        loc = line.strip()
        encoded_loc = urllib.parse.quote(loc)
        c.execute("SELECT geo_data FROM Locations WHERE address = ?", (loc,))
        try:
            data = c.fetchone()[0]
            continue
        except:
            pass
        re = (
            urllib.request.urlopen(
                f"https://py4e-data.dr-chuck.net/opengeo?q={encoded_loc}", context=ctx
            )
            .read()
            .decode()
        )
        json = js.loads(re)
        print(json)
        c.execute(
            """INSERT INTO Locations (address,geo_data) VALUES (?,?)""",
            (loc, re),
        )
        print(loc,re)
        i = i + 1        # if i % 10 == 0 :
        #    time.sleep(5)
conn.commit()
conn.close()
