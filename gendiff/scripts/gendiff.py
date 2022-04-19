import argparse
import json
from ntpath import join

def generate_diff(first_file, second_file):
    first_json = json.load(open(first_file))
    second_json = json.load(open(second_file))
    all_keys = set(filter(None, first_json)) | set(filter(None, second_json))
    all_keys = sorted(all_keys)
    result = []
    result.append("{")
    for key in all_keys:
        if first_json.get(key) is not None and second_json.get(key) is not None:
            if first_json.get(key) == second_json.get(key):
                result.append(f"    {key}: {first_json[key]}")
            else:
                result.append(f"  - {key}: {first_json[key]}")
                result.append(f"  + {key}: {second_json[key]}")
        else:
            if first_json.get(key) is not None:
                result.append(f"  - {key}: {first_json[key]}")
            else:
                result.append(f"  + {key}: {second_json[key]}")
    result.append("}")
    return "\n".join(result)




def main():
    pharser = argparse.ArgumentParser(description="Generate diff")
    pharser.add_argument("first_file", type=str, help="")
    pharser.add_argument("second_file", type=str, help="")
    pharser.add_argument("-f", "--format")
    args = pharser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)



if __name__ == "__main__":
    main()
