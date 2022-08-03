import json
from typing import Dict, Union

import requests


class JokeAPIConnector:
    def __init__(self) -> None:
        self._base_url: str = "https://v2.jokeapi.dev"
        self._headers: Dict[str, str] = {"Accept": "application/json"}
        self._response: Union[requests.Request, None] = None

    def _build_path(self, *args: str) -> str:
        return f"{self._base_url}/{'/'.join(args)}?type=single"

    @staticmethod
    def _build_error_message(status_code: int, message: str) -> Dict[str, str]:
        return {"Error": f"{status_code}: {message}"}

    def get_response(self, category: str = "Any") -> Union[Dict, None, str]:
        self._response = requests.request("GET",
                                          self._build_path("joke", category),
                                          headers=self._headers)
        if self._response.ok:
            return json.loads(self._response.text)
        return json.loads(self._response.text)


class JokesAdapter:
    def __init__(self, response: Dict):
        self._response = response

    def is_error(self) -> bool:
        return self._response.get("error")

    def get_category(self) -> str:
        return self._response.get("category")

    def get_joke(self) -> str:
        return self._response.get("joke")


if __name__ == '__main__':
    joke_response = JokeAPIConnector().get_response()
    print(joke_response)
    joke = JokesAdapter(joke_response)

    print(joke.is_error())
    print(joke.get_category())
    print(joke.get_joke())
