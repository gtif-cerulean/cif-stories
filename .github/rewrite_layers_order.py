import json
import re
import sys


LAYERS_ATTR_REGEX = re.compile(r"""layers\s*=\s*'(?P<json>\[.*?\])'""", re.DOTALL)


def reverse_group_layers(layers):
    """
    Reverse this layers list and reverse nested Group.layers only.
    """
    reversed_layers = list(reversed(layers))

    for layer in reversed_layers:
        if (
            isinstance(layer, dict)
            and layer.get("type") == "Group"
            and isinstance(layer.get("layers"), list)
        ):
            layer["layers"] = reverse_group_layers(layer["layers"])

    return reversed_layers


def process_markdown(content: str) -> str:
    def replacer(match: re.Match) -> str:
        json_text = match.group("json")

        try:
            layers = json.loads(json_text)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Invalid layers JSON: {e}")

        if not isinstance(layers, list):
            return match.group(0)

        layers = reverse_group_layers(layers)

        new_json = json.dumps(layers, separators=(",", ":"))
        return f"layers='{new_json}'"

    return LAYERS_ATTR_REGEX.sub(replacer, content)


def main(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = process_markdown(content)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python reverse_layers.py <markdown-file>")
        sys.exit(1)

    main(sys.argv[1])
