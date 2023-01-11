from typing import TextIO

class ParseError(Exception):
    __module__ = Exception.__module__ # set exception as builtin to hide __name__
    def __init__(self, message):
        self.message = message
    
    def __str__(self) -> str:
        return str(self.message)

class Parser:
    class subclass:
        pass

    def __init__(self):
        self.digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    
    def __str__(self) -> str:
        # try:
        #     return open(self.file).read()
        # except:
        #     return self.__repr__()
        return self.__repr__()

    def __repr__(self):
        return f"<Parser object at {hex(id(self))}>"

    def load(self, fp : TextIO):
        self.loads(fp.read())

    # load from string
    def loads(self, data):
        l = []
        for i, c in enumerate(data): # find closing brackets
            match c:
                case "[":
                    l.append(i)
                case "]":
                    if len(l) == 0:
                        raise ParseError("Syntax error")
                    l.pop()
        if len(l) > 0:
            raise ParseError("Syntax error")

        lines = [i for i in data.splitlines() if i != ""] # remove empty lines to avoid IndexError
        for i in range(len(lines)):
            if lines[i].startswith("["):
                section = lines[i].strip().replace("[", "").replace("]", "")

                if section[0] in self.digits: # section name starts with a number
                    raise ParseError(f"Invalid data at line {i + 1}")

                setattr(self, section, self.subclass())
                at = getattr(self, section) # get subclass object since we cant do something like locals()[f"self.{section}"]
                i += 1
                try:
                    while not lines[i].strip().startswith("["):
                        s = lines[i].strip().split("=", 2) # split by "=" 2 times
                        if s[0][0] in self.digits: # first char in name
                            raise ParseError(f"Invalid data at line {i + 1}")
                        
                        try:
                            setattr(at, s[0].strip(), int(s[1].strip()))
                        except ValueError:
                            setattr(at, s[0].strip(), s[1].strip())
                        
                        i += 1
                except IndexError:
                    pass
                
            else:
                j = lines[i].strip().split("=", 2)
                if len(j) == 0 or j[0].strip()[0] in self.digits:
                    raise ParseError(f"Invalid data at line {i + 1}")
                
                try:
                    setattr(self, j[0].strip(), int(j[1].strip()))
                except ValueError:
                    setattr(self, j[0].strip(), j[1].strip())