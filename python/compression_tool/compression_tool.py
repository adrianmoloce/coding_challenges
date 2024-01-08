import sys
from collections import Counter


def get_freq(file_name):
    try:
        file = open(file_name, "r")
        data = file.read()
        return Counter(data)
    except FileError as ex:
        raise FileError
    finally:
        file.close()


if __name__ == "__main__":
    freqs = get_freq(sys.argv[1])
    print(freqs)
    print(freqs['X'])
    print(freqs['t'])
