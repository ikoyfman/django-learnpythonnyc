import csv
from pathlib import Path
from vdata.models import Genre, Publisher, Platform, Videogame
from decimal import Decimal

#%%

vfiledata = Path('./vdata/Video_Games_Sales_as_at_22_Dec_2016.csv') 
with open(vfiledata) as vdata: 
    csv_read = csv.reader(vdata)
    count = 0
    for row in csv_read:
        if count == 0:
            count += 1
            continue

        # Insert into sql
        vplatform = Platform.objects.get_or_create(name=row[1])
        vgenre = Genre.objects.get_or_create(name=row[3])
        vpublisher = Publisher.objects.get_or_create(name=row[4])
        print(row)
        Videogame.objects.get_or_create(
            name= row[0],
            platform = Platform.objects.get(name=row[1]),
            released = int(row[2]),
            genre = Genre.objects.get(name=row[3]),
            publisher = Publisher.objects.get(name=row[4]),
            na_sales = Decimal(row[5])
        )

    
