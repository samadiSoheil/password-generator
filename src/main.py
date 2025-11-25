import random
import string
from abc import ABC, abstractmethod
from word import words


class Password(ABC):

    @abstractmethod
    def generate(self):
        pass


class PasswordFactory(ABC):

    @abstractmethod
    def create_pass(self):
        pass


# password classes
class PinPass(Password):

    def generate(self, **kwargs) -> str:

        length = kwargs.get('length', 8)

        first_digit = random.choice("123456789")
        numbers = "".join( random.choices("0123456789", k = length - 1 ))

        password = first_digit + numbers

        return password


class RandomPass(Password):

    def __init__(self):
        self.characters = ""

    def config(self, **kwargs):

        # reset characters  
        self.characters = ""

        digits = kwargs.get('digits', True)
        letters = kwargs.get('letters', True)
        specific_chars = kwargs.get('specific_chars', False)

        if digits:
            self.characters += string.digits

        if letters:
            self.characters += string.ascii_letters

        if specific_chars:
            self.characters += string.punctuation

    def generate(self, **kwargs):

        self.config(**kwargs)

        if not self.characters:
            raise ValueError("No character sets selected for password generation.")

        length = kwargs.setdefault('length', 8)

        password = "".join( random.choices( self.characters, k = length ))

        return password


class MemorablePass(Password):

    def generate(self, length: int = 8, separator: str = '-', words_list: list[str] = words) -> str:
        
        password_words: list =  random.choices( words_list, k = length )
        generated_pass: list = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
        password = separator.join(generated_pass)

        return password



# password factories
class PinPassFactory(PasswordFactory):

    def create_pass(self):
        return PinPass()


class RandomPassFactory(PasswordFactory):

    def create_pass(self):
        return RandomPass()


class MemorablePassFactory(PasswordFactory):

    def create_pass(self):
        return MemorablePass()


def password_selector(pass_type = 'pin', **kwargs):

    pass_type = pass_type.lower()

    factories = {
        'pin': PinPassFactory(),
        'random': RandomPassFactory(),
        'memorable': MemorablePassFactory(),
    }

    factory = factories.get(pass_type)

    if not factory :
        raise ValueError('plese enter valid type: PIN, RANDOM, MEMORABLE.')

    password = factory.create_pass().generate(**kwargs)

    return password


def main(pass_type, **kwargs):

   return password_selector(pass_type, **kwargs)


if __name__ == "__main__":

    pin = main('pin', length = 3)
    print(pin)

    random_pass = main('random', length = 9)
    print(random_pass)

    memorable_pass = main('memorable', length = 3)
    print(memorable_pass)
