class StringHash:
    def __init__(self, the_string):
        self.the_string = the_string
        self.hashed_value = 0
        self.hash_the_string()

    def hash_the_string(self):
        current_value = 0
        for character in self.the_string:
            # Get the ASCII character of the current character and add it to the current value
            current_value = current_value + ord(character)
            # Multiply the current value by 17 and store it back into itself
            current_value = current_value * 17
            # Set the current value to its remainder after dividing by 256
            current_value = current_value % 256
        self.hashed_value = current_value

if __name__ == "__main__":
    a_hash = StringHash("HASH")
    print(a_hash.hashed_value)