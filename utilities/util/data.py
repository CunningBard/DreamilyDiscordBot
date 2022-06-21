import time

import orjson

"""
{
    "people":
        10000000: {
            "id": 10000000,
            "last_use": 10523007,
            "command_use_times":  1,
            "num_stories": 2
            "stories":
                {
                    1: "asdasdasdasdasd asdasdasdadasdasdasdasdasdasdasd",
                    2: " asdasdasdasdasdasd"
                }
        }
}
"""


class Person:
    def __init__(self, discord_id: str, last_use: int = 0, command_use_times: int = 1, num_stories: int = 0,
                 stories=None):
        if stories is None:
            stories = {}

        discord_id = str(discord_id)

        self.dis_id = discord_id
        self.last_use = last_use
        self.command_use_times = command_use_times
        self.num_stories = num_stories
        self.stories = stories

    def as_dict(self) -> dict:
        return {
            "id": self.dis_id, "last_use": self.last_use, "command_use_times": self.command_use_times,
            "num_stories": self.num_stories, "stories": self.stories
        }


class Database:
    def __init__(self, file_path: str):
        self.data = {}
        self.file_path = file_path

    def import_content(self):
        self.data.clear()
        with open(self.file_path, "r") as f:
            content = f.read()
        data = orjson.loads(content)
        for id_ in list(data["people"]):
            person = data["people"][id_]
            self.data[id_] = Person(person["id"], person["last_use"], person["command_use_times"],
                                    person["num_stories"], person["stories"])

    def new_user(self, user_id: int):
        user_id = str(user_id)
        self.data[user_id] = Person(user_id, int(time.time()))
        self.export_content()

    def export_content(self):
        data = {"people": {}}
        for person in self.data.values():
            data["people"][person.dis_id] = person.as_dict()

        with open(self.file_path, "w") as f:
            f.write(orjson.dumps(data).decode())

    def reload(self):
        self.export_content()
        self.import_content()

    def has(self, auth_id):
        return True if str(auth_id) in self.data else False

    def get(self, auth_id) -> Person:
        self.reload()
        return self.data[str(auth_id)]


if __name__ == '__main__':
    db = Database("../../dynamic_files/data.json")
    db.new_user(1)
