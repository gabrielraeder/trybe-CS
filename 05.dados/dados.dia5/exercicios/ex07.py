from stack import Stack
from queue import Queue


class RevertString:
    def __init__(self, string):
        self.queue = Queue()
        self.add_to_stack(string)

    def add_to_stack(self, string):
        for letter in string:
            self.queue.enqueue(letter)

    def __str__(self):
        return self.queue.__str__()

    def revert(self):
        correct = []
        to_revert = []
        letter = self.queue.dequeue()

        while letter != "(":
            correct.append(letter)
            letter = self.queue.dequeue()

        letter = self.queue.dequeue()
        while letter != ")":
            to_revert.append(letter)
            letter = self.queue.dequeue()

        correct = "".join(correct)
        to_revert = "".join(to_revert[::-1])
        return f"{correct}{to_revert}"


def reverse_word(stack):
    char = ")"
    reversed_word = []
    while char != "(":
        char = stack.pop()
        if char != "(":
            reversed_word.append(char)

    for letter in reversed_word:
        stack.push(letter)


def reverse_letters(phrase):
    stack = Stack()
    for char in phrase:
        if char != ")":
            stack.push(char)
        else:
            reverse_word(stack)

    reversed_phrase = []
    while not stack.is_empty():
        reversed_phrase.append(stack.pop())

    return "".join(reversed(reversed_phrase))


if __name__ == "__main__":
    string = "teste(lagel)"
    revert = RevertString(string)

    print(revert.revert())

    print(reverse_letters("teste(lagel)"))
    print(reverse_letters("(abcd)"))
    print(reverse_letters("(u(love)i)"))
    print(reverse_letters("(ed(et(oc))el)"))
    print(reverse_letters("a(bcdefghijkl(mno)p)q"))
