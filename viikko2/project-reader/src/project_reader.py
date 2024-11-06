from urllib import request

from toml import loads

from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)
        parsed_toml = loads(content)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            "Test name",
            "Test description",
            list(parsed_toml["tool"]["poetry"]["dependencies"].keys()),
            list(parsed_toml["tool"]["poetry"]["group"]["dev"]["dependencies"].keys()),
            parsed_toml["tool"]["poetry"]["license"],
            list(parsed_toml["tool"]["poetry"]["authors"]), 
        )
