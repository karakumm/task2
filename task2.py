"""
This module helps to navigate inside json file.
"""


import json
# import pprint


def read_file(path: str):
    '''
    This function reads json file.
    '''
    json_file = open(path, encoding="utf-8")
    return json.load(json_file)


def navigate(data: str):
    '''
    This function navigates in json file via command line.
    '''
    if isinstance(data, list):
        print("♥ ♥ ♥ ♥ ♥")
        print(f"Enter the value from indexes in range 0 to {len(data) - 1}")
        # print("♥ ♥ ♥ ♥ ♥")

        while True:
            print("♥ ♥ ♥ ♥ ♥")
            print(f"Available indexes {[ind for ind in range(len(data) - 1)]}")
            print("♥ ♥ ♥ ♥ ♥")

            user_key = input("Make your choice: ")

            if user_key in [str(ind) for ind in range(len(data) - 1)]:
                return navigate(data[int(user_key)])
            else:
                continue

        return navigate(data[int(user_key)])

    if isinstance(data, dict):
        keys_base = list(data.keys())
        print("♥ ♥ ♥ ♥ ♥")
        print("Enter the value from keys:")

        while True:
            print("♥ ♥ ♥ ♥ ♥")
            for key in keys_base:
                print(f"- {key}")
            print("♥ ♥ ♥ ♥ ♥")

            user_key = input("Make your choice: ")

            if user_key in keys_base:
                return navigate(data[user_key])
            else:
                continue

    return data


if __name__ == "__main__":
    json_data = read_file("example_2.json")
    print(navigate(json_data))
    # print()
    print("♥ ♥ ♥ ♥ ♥")
    print('Thanks for using this program :)')
    print("♥ ♥ ♥ ♥ ♥")

