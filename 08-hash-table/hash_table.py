class HashTable:
    def __init__(self) -> None:
        self.collection: dict[int, dict] = {}

    def hash(self, key: str) -> int:
        return sum(ord(char) for char in key)

    def add(self, key: str, value) -> None:
        hashed = self.hash(key)
        # each hash owns a bucket, so keys that collide sit side by side
        if hashed not in self.collection:
            self.collection[hashed] = {}
        self.collection[hashed][key] = value

    def remove(self, key: str) -> None:
        hashed = self.hash(key)
        if hashed not in self.collection or key not in self.collection[hashed]:
            return
        del self.collection[hashed][key]
        if not self.collection[hashed]:
            del self.collection[hashed]

    def lookup(self, key: str):
        hashed = self.hash(key)
        if hashed not in self.collection:
            return None
        return self.collection[hashed].get(key)


if __name__ == "__main__":
    table = HashTable()
    table.add("fcc", "freeCodeCamp")
    table.add("cfc", "same hash, different key")

    print(table.hash("fcc"))
    print(table.lookup("fcc"))
    print(table.collection)

    table.remove("fcc")
    print(table.lookup("fcc"))
    print(table.lookup("cfc"))
