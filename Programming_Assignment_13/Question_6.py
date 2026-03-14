class Password_Checker:
    def __init__(self, password: str) -> None:
        self.password: str = password

    def has_alpha_lower(self) -> bool:
        return any(c.islower() for c in self.password)

    def has_alpha_upper(self) -> bool:
        return any(c.isupper() for c in self.password)

    def has_digit(self) -> bool:
        return any(c.isdigit() for c in self.password)

    def has_special_char(self) -> bool:
        return any(c in "$#@" for c in self.password)

    def is_valid_length(self) -> bool:
        length = len(self.password)
        return 6 <= length <= 12

    def check_valid(self) -> bool:
        return (
            self.has_alpha_lower()
            and self.has_alpha_upper()
            and self.has_digit()
            and self.has_special_char()
            and self.is_valid_length()
        )

if __name__ == "__main__":
    raw = input("Enter the passwords to check (comma separated):\n")
    values = [v.strip() for v in raw.split(",") if v.strip()]
    valid = []
    for value in values:
        checker = Password_Checker(value)
        if checker.check_valid():
            valid.append(value)
    print(",".join(valid))
