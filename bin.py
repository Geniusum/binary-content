class BinaryContent():
    def __init__(self) -> None:
        self.content = []

    def __parse_bin(self, bin: any) -> any:
        if isinstance(bin, str):
            return max(0, min(int(bin, 16), 255))
        return max(0, min(int(bin), 255))

    def __lshift__(self, bin: any):
        self.content.append(self.__parse_bin(bin))
        
        return self

    def __str__(self) -> str:
        s = ""
        for binchr in self.content:
            s += chr(binchr)
        return s

    def __iter__(self) -> iter:
        return iter(self.content)

    def __len__(self) -> int:
        return len(self.content)

    def __repr__(self) -> str:
        return self.__str__()

bin = BinaryContent()
bin << 212 << 4
print(bin)