def subs(elements):
    newlist = []
    for item in elements:
        if type(item) is int:
            newlist.append(item > 42)
        if type(item) is str:
            newlist.append("a" in item)
        if type(item) is float:
            newlist.append(item > 3.14)
        if type(item) is list:
            newlist.append(len(item) != 2)

    return newlist


lista = [1, 43, "alow", "low", 3.11, 4.1, [1, 2], [1]]
print(subs(lista))

# def subs(elements):
#     newlist = []
#     for item in elements:
#         if type(item) is int:
#             if item > 42:
#                 newlist.append(True)
#             else:
#                 newlist.append(False)
#         if type(item) is str:
#             if item.__contains__("a"):
#                 newlist.append(True)
#             else:
#                 newlist.append(False)
#         if type(item) is float:
#             if item > 3.14:
#                 newlist.append(True)
#             else:
#                 newlist.append(False)

#         if type(item) is list:
#             if len(item) != 2:
#                 newlist.append(True)
#             else:
#                 newlist.append(False)
#     return newlist
