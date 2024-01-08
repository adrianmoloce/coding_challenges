import os

symbols = {
    "{": "}",
    "[": "]",
    "\"": "\""
}


class Lexer:
    def __init__(self):
        self.__stack = []

    def scan(self, data):
        if not data:
            return 1
        
        idx = 0
        while idx < len(data):
            item = data[idx]
            if item in ["{", "["]:
                self.__stack.append(item)
            elif item in ["}", "]", "\""]:
                opened = self.__stack.pop()
                if symbols[opened] != item:
                    return 1
            elif item.isalpha():
                word = ""
                while item.isalpha():
                    word += item
                    idx += 1
                    item = data[idx]
                if word not in ["true", "false", "null"]:
                    return 1
            elif item == "," and data[idx+1] == "}":
                return 1
            idx += 1
        if not self.__stack:
            return 0
        return 1


if __name__ == "__main__":
    lex = Lexer()

    base = os.path.join(os.getcwd(), "tests")
    f = open(f"{base}/step1/valid.json", "r")
    data = f.read().strip()
    f.close()
    
    print(lex.scan(data))
    
    f = open(f"{base}/step1/invalid.json", "r")
    data = f.read().strip()
    f.close()

    print(lex.scan(data))
