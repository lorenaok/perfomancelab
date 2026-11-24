import sys
import json


def load_values(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {item["id"]: item["value"] for item in data["values"]}


def fill(node, values_map):
    if isinstance(node, dict):
        if "id" in node and "value" in node:
            node["value"] = values_map.get(node["id"], node.get("value", ""))
        for key in ("values", "tests"):
            if key in node and isinstance(node[key], list):
                for child in node[key]:
                    fill(child, values_map)
    elif isinstance(node, list):
        for item in node:
            fill(item, values_map)


def main():
    values_path, tests_path, report_path = sys.argv[1:4]

    values_map = load_values(values_path)

    with open(tests_path, "r", encoding="utf-8") as f:
        tests = json.load(f)

    fill(tests, values_map)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(tests, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()