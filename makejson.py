import json
import csv
import sys
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Syntax: %s <input_file> <output_file> \"<delim>\"" % sys.argv[0])
        sys.exit()
    input_csv = sys.argv[1]
    output_json = sys.argv[2]
    if len(sys.argv) == 4: delim = sys.argv[3]
    else: delim = ','
    if delim != ',' and delim != '|':
        print("Invalid delimiter, must be comma or pipe")
        sys.exit()

    json_data = list()

    with open(input_csv) as csvf:
        csv_reader = csv.DictReader(csvf, delimiter=delim, quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in csv_reader: json_data.append(row)
    
    with open(output_json, 'w') as jsonf:
        for item in json_data:
            trim_item = dict()
            for key in item:
                value = item[key]
                if key[0] == ' ': key = key[1:]
                if key[-1] == ' ': key = key[:-1]
                trim_item[key] = value
            jsonf.write(json.dumps(trim_item))
            jsonf.write('\n')

