"""
{
    "people":
    [
        {
            "id": 10000000,
            "last_use": 10523007,
            "command_use_times":  1
        }
    ]
}
"""


class Person:
    def __init__(self, discord_id: int, last_generation: int, command_use_times: int):
        self.dis_id = discord_id
        self.last_gen = last_generation
        self.command_use_times = command_use_times


class Database:
    def __init__(self, file_path: str):
        self.data = []
        self.file_path = file_path

    def import_content(self, data: dict):
        for person in data["people"]:
            self.data.append(Person(person["id"], person["last_use"], person["command_use_times"]))
