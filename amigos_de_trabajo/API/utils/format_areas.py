import os

areas = []
with open("E:\\PYTHON\\amigos_de_trabajo\\amigos_de_trabajo\\API\\areas.txt", 'r', encoding='utf-8') as source:
    for line in source:
        areas.append(line)

new_areas = []
for area in areas:
    area = area.replace("\n", "")
    old_area = area[:]
    area = area.replace("WI", "Wisconsin")
    area = area.replace("WY", "Wyoming")
    area = area.replace("WV", "West Virginia")
    area = area.replace("WA", "Washington")
    area = area.replace("VA", "Virginia")
    area = area.replace("VT", "Vermont")
    area = area.replace("UT", "Utah")
    area = area.replace("TX", "Texas")
    area = area.replace("TN", "Tennessee")
    area = area.replace("SD", "South Dakota")
    area = area.replace("SC", "South Carolina")
    area = area.replace("RI", "Rhode Island")
    area = area.replace("PR", "Puerto Rico")
    area = area.replace("PA", "Pennsylvania")
    area = area.replace("OR", "Oregon")
    area = area.replace("OK", "Oklahoma")
    area = area.replace("OH", "Ohio")
    area = area.replace("ND", "North Dakota")
    area = area.replace("NC", "North Carolina")
    area = area.replace("NY", "New York")
    area = area.replace("NM", "New Mexico")
    area = area.replace("NJ", "New Jersey")
    area = area.replace("NH", "New Hampshire")
    area = area.replace("NV", "Nevada")
    area = area.replace("NE", "Nebraska")
    area = area.replace("MT", "Montana")
    area = area.replace("MO", "Missouri")
    area = area.replace("MS", "Mississippi")
    area = area.replace("MN", "Minnesota")
    area = area.replace("MI", "Michigan")
    area = area.replace("MA", "Massachusetts")
    area = area.replace("MD", "Maryland")
    area = area.replace("ME", "Maine")
    area = area.replace("LA", "Louisiana")
    area = area.replace("KY", "Kentucky")
    area = area.replace("KS", "Kansas")
    area = area.replace("IA", "Iowa")
    area = area.replace("IN", "Indiana")
    area = area.replace("IL", "Illinois")
    area = area.replace("ID", "Idaho")
    area = area.replace("HI", "Hawaii")
    area = area.replace("GA", "Georgia")
    area = area.replace("FL", "Florida")
    area = area.replace("DL", "Delaware")
    area = area.replace("CT", "Connecticut")
    area = area.replace("CO", "Colorado")
    area = area.replace("CA", "California")
    area = area.replace("AR", "Arkansas")
    area = area.replace("AZ", "Arizona")
    area = area.replace("AK", "Alaska")
    area = area.replace("AL", "Alabama")
    area = area.split("–")[0]
    old_area = old_area.split("–")[0]
    string_area = f'("{old_area}","{area}")'
    print(string_area)
    new_areas.append(string_area)

with open("E:\\PYTHON\\amigos_de_trabajo\\amigos_de_trabajo\\API\\locals.py", 'w', encoding='utf-8') as target:
    for area in new_areas:
        target.write(f'{area},\n')