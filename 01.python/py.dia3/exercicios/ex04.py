from ex03 import email_check


def list_email_check(lista: list):
    valid_emails = []
    for email in lista:
        try:
            email_check(email)
        except ValueError as err:
            print(err)
        else:
            valid_emails.append(email)
    return valid_emails


if __name__ == "__main__":
    email_list = [
        "gabriel_@hot.com",
        "1abriel_@hot.com",
        "ga#riel_@hot.com",
        "gabriel_@h$t.com",
        "gabriel_@hot.coom",
        "dulce@gmail.coom",
    ]
    print(list_email_check(email_list))
