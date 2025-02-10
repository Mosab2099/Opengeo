import sqlite3 as sq
import json as js 
import codecs

conn = sq.connect('myopengeo.sqlite')
c = conn.cursor()

c.execute('SELECT * FROM Locations')
count = -1
with open('mywhere.js','w',encoding="utf-8") as f:
    f.write("myData = [\n")
    for row in c :
        data = row[1]
        json = js.loads(data)
        try:
            lat= json['features'][0]['geometry']['coordinates'][1]
            lng = json['features'][0]['geometry']['coordinates'][0]
            place = json['features'][0]['properties']['display_name']
        except:continue
        count = count + 1
        if count > 0 : f.write(",\n")

        output = "[" + str(lat) + "," + str(lng) + "," + '"' + place + '"' + "]" + "\n"
        f.write(output)
    f.write("];")   
        
              



