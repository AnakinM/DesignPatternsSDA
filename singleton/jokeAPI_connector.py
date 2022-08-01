import json
from typing import Dict, Union

import requests

from singleton_metaclass import SingletonMeta


class JokeAPIConnector(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._base_url: str = "https://v2.jokeapi.dev"
        self._headers: Dict[str, str] = {"Accept": "application/json"}
        self._response: Union[requests.Request, None] = None

    def _build_path(self, *args: str) -> str:
        return f"{self._base_url}/{'/'.join(args)}?type=single"

    @staticmethod
    def _build_error_message(status_code: int, message: str) -> Dict[str, str]:
        return {"Error": f"{status_code}: {message}"}

    def get_joke(self, category: str = "Any") -> Union[Dict, None, str]:
        self._response = requests.request("GET",
                                          self._build_path("joke", category),
                                          headers=self._headers)
        if self._response.ok:
            return json.loads(self._response.text).get("joke")
        error = json.loads(self._response.text)
        return self._build_error_message(self._response.status_code,
                                         error.get("message"))


if __name__ == '__main__':
    joke = JokeAPIConnector()
    print(joke.get_joke(category="Spooky"), end="\n\n")
    joke_2 = JokeAPIConnector()
    print(joke_2.get_joke())
