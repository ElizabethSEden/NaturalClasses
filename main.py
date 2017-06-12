import json
from mapping import Map
from NaturalClasses import NaturalClasses
from csv_to_json import csv_to_json
from settings import FILEPATH

with open(filepath, encoding='utf-8', mode="r") as f:
    try:
        data = json.loads(f.read())
    except:
        data = json.loads(csv_to_json(filepath))
        with open(filepath.replace('.csv','.txt'), "w", encoding='utf-8') as f:
            f.write(csv_to_json(filepath))

map = Map(data)

nc = NaturalClasses(map, 3)

with open("Natural classes.txt", "w", encoding='utf-8') as f:
    nc.output(f)

with open("Feature combinations with no segments.txt", "w", encoding='utf-8') as f:
    f.write('\n'.join([r for r in nc.featureCombo_to_segments if not nc.featureCombo_to_segments[r]]))

with open("Redundant natural classes.txt", "w", encoding="utf-8") as f:
    nc.output_redundant(f)

with open("Redundant natural classes sans subsets.txt", "w", encoding="utf-8") as f:
    nc.output_redundant_sans_subsets(f)

with open("Natural classes with non-subset redundancies.txt", "w", encoding="utf-8") as f:
    nc.output_redundant_if_nonsubsets(f)

with open("Contrasts between segments.txt", "w", encoding="utf-8") as f:
    nc.output_segment_contrasts(f)