def email_check(email: str):
    user = email.split("@")[0]
    website, extension = email.split("@")[1].split(".")
    if not user[0].isalpha():
        raise ValueError("Must start with character!")
    for char in user:
        if not char.isalpha() and not char.isdigit() and char not in "-_":
            raise ValueError("Invalid character!")
    for char in website:
        if not char.isalpha() and not char.isdigit():
            raise ValueError("Invalid website!")
    if len(extension) > 3:
        raise ValueError("Invalid extension!")
    return True


if __name__ == "__main__":
    email_check("gabriel_@hot.com")
