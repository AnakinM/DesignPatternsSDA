from typing import Dict


class Customer:
    def get_first_name(self) -> str:
        pass

    def get_last_name(self) -> str:
        pass

    def get_email(self) -> str:
        pass

    def get_phone_number(self) -> str:
        pass

    def get_transaction_count(self) -> int:
        pass


class Client:
    def __init__(
        self,
        full_name: str,
        contact_details: Dict[str, str],
        number_of_transactions: int,
    ):
        self._full_name = full_name
        self._contact_details = contact_details
        self._number_of_transactions = number_of_transactions

    def get_full_name(self) -> str:
        return self._full_name

    def get_contact_details(self) -> Dict[str, str]:
        return self._contact_details

    def get_number_of_transactions(self) -> int:
        return self._number_of_transactions


class ClientAdapter(Customer):
    def __init__(self, client: Client):
        self._client = client

    def get_first_name(self) -> str:
        return self._client.get_full_name().split(" ")[0]

    def get_last_name(self) -> str:
        return self._client.get_full_name().split(" ")[1]

    def get_email(self) -> str:
        return self._client.get_contact_details().get("email")

    def get_phone_number(self) -> str:
        return self._client.get_contact_details().get("phone")

    def get_transaction_count(self) -> int:
        return self._client.get_number_of_transactions()


if __name__ == "__main__":
    customers = [
        ClientAdapter(
            Client(
                "John Kowalsky",
                {"email": "johnkowalsky@example.com", "phone": "523456789"},
                10,
            )
        ),
        ClientAdapter(
            Client("Joe Doe", {"email": "jo@example.com", "phone": "516457785"}, 12)
        ),
        ClientAdapter(
            Client(
                "Eve Smith", {"email": "evesmi@example.com", "phone": "521251389"}, 1000
            )
        ),
    ]

    for c in customers:
        print(
            f"{c.get_first_name()} {c.get_last_name()} has email: {c.get_email()} and phone number: "
            f"{c.get_phone_number()} and did {c.get_transaction_count()} transactions."
        )
