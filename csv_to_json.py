import json
import sys

def csv_to_json(filepath):
    with open(filepath, encoding='utf-8', mode="r") as f:
        lines = f.readlines()
    header = lines[0].replace('\n','').split('\t')[1:]
    entries = {}
    for line in lines[1:]:
        cells = line.replace('\n','').split('\t')
        segment = cells[0]
        features = {}
        values = cells[1:]
        for i in range(len(header)):
            features[header[i]] = values[i]
        entries[segment] = features
    return json.dumps(entries)

if __name__ == "__main__":
    input_file = sys.argv[0]
    outfile = sys.argv[1]

    with open(outfile, "w", encoding='utf-8') as f:
        f.write(csv_to_json(input_file))


