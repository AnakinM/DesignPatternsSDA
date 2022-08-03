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


class MatureLanguageFilterStrategyProvider:

    @staticmethod
    def get_strategy(strategy_type: str) -> MatureLanguageFilterStrategy:
        if strategy_type.lower() == "remove":
            return RemoveWordStrategy()
        elif strategy_type.lower() == "star":
            return StarWordStrategy()


if __name__ == "__main__":
    choice = input("Choose strategy [remove|star]: ")
    text_to_filter = "Holy cow now I have to cow go there myself!"

    strategy = MatureLanguageFilterStrategyProvider().get_strategy(choice)
    output = strategy.modify(text_to_filter, "cow")
    print(output)
