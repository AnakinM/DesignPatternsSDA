"""Strategy pattern example"""
import random
from abc import ABC, abstractmethod
from typing import Optional


class MatureLanguageFilterStrategy(ABC): # pylint: disable=too-few-public-methods
    """MatureLanguageFilterStrategy class"""
    @abstractmethod
    def modify(self, text: str, word: str) -> str:
        """ Modify method that applies modification to a given
        test.

        :param text:
        :param word:
        :return:
        """


class RemoveWordStrategy(MatureLanguageFilterStrategy): # pylint: disable=too-few-public-methods
    """RemoveWordStrategy class"""
    def modify(self, text: str, word: str) -> str:
        """ Modify method that applies modification to a given
        test.

        :param text:
        :param word:
        :return:
        """
        return text.replace(word, "")


class StarWordStrategy(MatureLanguageFilterStrategy): # pylint: disable=too-few-public-methods
    """RemoveWordStrategy class"""
    def modify(self, text: str, word: str) -> str:
        """ Modify method that applies modification to a given
        test.

        :param text:
        :param word:
        :return:
        """
        return text.replace(word, "*" * len(word))


class MessWordStrategy(MatureLanguageFilterStrategy): # pylint: disable=too-few-public-methods
    """RemoveWordStrategy class"""
    def modify(self, text: str, word: str) -> str:
        """ Modify method that applies modification to a given
        test.

        :param text:
        :param word:
        :return:
        """
        letters = list(word)
        random.shuffle(letters)
        return text.replace(word, "".join(letters))


class BackwardStrategy(MatureLanguageFilterStrategy): # pylint: disable=too-few-public-methods
    """RemoveWordStrategy class"""
    def modify(self, text: str, word: str) -> str:
        """ Modify method that applies modification to a given
        test.

        :param text:
        :param word:
        :return:
        """
        return text.replace(word, word[::-1])


class CensoreMiddleWordStrategy(MatureLanguageFilterStrategy): # pylint: disable=too-few-public-methods
    """RemoveWordStrategy class"""
    def modify(self, text: str, word: str) -> str:
        """ Modify method that applies modification to a given
        test.

        :param text:
        :param word:
        :return:
        """
        censored_word = word[0] + "*" * (len(word) - 2) + word[-1]
        return text.replace(word, censored_word)


class MatureLanguageFilterStrategyProvider: # pylint: disable=too-few-public-methods
    """RemoveWordStrategy class"""
    @staticmethod
    def get_strategy(
            strategy_type: str
    ) -> Optional[MatureLanguageFilterStrategy]:
        """ Method that provides requested strategy.

        :param strategy_type:
        :return:
        """
        if strategy_type.lower() == "remove":
            return RemoveWordStrategy()
        if strategy_type.lower() == "star":
            return StarWordStrategy()
        if strategy_type.lower() == "mess":
            return MessWordStrategy()
        if strategy_type.lower() == "backward":
            return BackwardStrategy()
        if strategy_type.lower() == "partcensore":
            return CensoreMiddleWordStrategy()
        return None


if __name__ == "__main__":
    choice = input("Choose strategy [remove|star|mess|backward|partcensore]: ")
    TEXT_TO_FILTER = "Holy coaww now I have to coaww go there myself!"

    strategy = MatureLanguageFilterStrategyProvider().get_strategy(choice)
    output = strategy.modify(TEXT_TO_FILTER, "coaww")
    print(output)

# Zadanie 1
# MessWordStrategy()
# cow -> owc lub woc lub cwo

# Zadanie 2
# Zaimplementować dowolną własną strategię (np. zamiana słowa na inne)
