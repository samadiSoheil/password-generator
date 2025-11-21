import random
import string
from abc import ABC, abstractmethod
from word import words


class PasswordType(ABC):

    @abstractmethod
    def generate(self, length: int) -> str:
        pass


class PasswordGenerator:
    
    def generate_password(
        self, type, length, word_list=words, digits=False, letters=True, specific_chars=False
    ):
        return FactoryPasswordType(length).type_of_pass(
            type, digits, letters, specific_chars, word_list
        )


class FactoryPasswordType:

    def __init__(self, length):
        self.pass_length = length

    def type_of_pass(self, type, digits, letters, specific_chars, word_list):

        if type == "pin":
            return Pin_pass().generate(self.pass_length)

        elif type == "memorable":
            return Memorable_pass(word_list=word_list).generate(length=self.pass_length)

        elif type == "random":
            random_pass_obj = Random_pass()
            random_pass_obj.config(digits, letters, specific_chars)
            return random_pass_obj.generate(self.pass_length)

        else:
            raise ValueError("please enter valid data, pin, memorable, random.")


class Random_pass(PasswordType):

    def __init__(self):
        self.characters = ""

    def config(self, digits, letters, specific_chars):
        if digits:
            self.characters += string.digits

        if letters:
            self.characters += string.ascii_letters

        if specific_chars:
            self.characters += string.punctuation

    def generate(self, length):
        password = "".join(random.choices(self.characters, k=length))

        return password


class Pin_pass(PasswordType):
    def generate(self, length: int) -> str:

        first_digit = random.choice("123456789")

        numbers = "".join(random.choices("0123456789", k=length-1))
        password = first_digit + numbers

        return password


class Memorable_pass(PasswordType):

    def __init__(self, word_list: list[str]):
        self.words = word_list
        self.words_separator = '-'

    def generate(self, length: int) -> str:

        password_words: list =  random.choices(self.words, k=length)
        generated_pass: list = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
        password = self.words_separator.join(generated_pass)

        return password


def main():
    generated_obj = PasswordGenerator()
    pin = generated_obj.generate_password(type='pin', length=4)
    random_pass = generated_obj.generate_password(type="random", length=4)
    memorable = generated_obj.generate_password(type="memorable", length=4)

    print('pin password= ', pin)
    print('random password= ', random_pass)
    print('memorable password= ', memorable)


if __name__ == "__main__":
    main()
