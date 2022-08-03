import random
from abc import ABC, abstractmethod


class MatureLanguageFilterStrategy(ABC):

    @abstractmethod
    def modify(self, text: str, word: str) -> str:
        pass


class RemoveWordStrategy(MatureLanguageFilterStrategy):

    def modify(self, text: str, word: str) -> str:
        return text.replace(word, "")


class StarWordStrategy(MatureLanguageFilterStrategy):

    def modify(self, text: str, word: str) -> str:
        return text.replace(word, '*' * len(word))


class MessWordStrategy(MatureLanguageFilterStrategy):

    def modify(self, text: str, word: str) -> str:
        letters = list(word)
        random.shuffle(letters)
        return text.replace(word, ''.join(letters))


class BackwardStrategy(MatureLanguageFilterStrategy):

    def modify(self, text: str, word: str) -> str:
        return text.replace(word, word[::-1])


class CensoreMiddleWordStrategy(MatureLanguageFilterStrategy):

    def modify(self, text: str, word: str) -> str:
        censored_word = word[0] + "*" * (len(word) - 2) + word[-1]
        return text.replace(word, censored_word)


class MatureLanguageFilterStrategyProvider:

    @staticmethod
    def get_strategy(strategy_type: str) -> MatureLanguageFilterStrategy:
        if strategy_type.lower() == "remove":
            return RemoveWordStrategy()
        elif strategy_type.lower() == "star":
            return StarWordStrategy()
        elif strategy_type.lower() == "mess":
            return MessWordStrategy()
        elif strategy_type.lower() == "backward":
            return BackwardStrategy()
        elif strategy_type.lower() == "partcensore":
            return CensoreMiddleWordStrategy()


if __name__ == "__main__":
    choice = input("Choose strategy [remove|star|mess|backward|partcensore]: ")
    text_to_filter = "Holy coaww now I have to coaww go there myself!"

    strategy = MatureLanguageFilterStrategyProvider().get_strategy(choice)
    output = strategy.modify(text_to_filter, "coaww")
    print(output)

# Zadanie 1
# MessWordStrategy()
# cow -> owc lub woc lub cwo

# Zadanie 2
# Zaimplementować dowolną własną strategię (np. zamiana słowa na inne)