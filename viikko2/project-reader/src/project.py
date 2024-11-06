class Project:
    def __init__(
        self, name, description, dependencies, dev_dependencies, license, authors
    ):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def _list_items(self, items):
        return "\n- " + "\n- ".join(items) if items else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.license or '-'}\n"
            f"\nAuthors: {self._list_items(self.authors)}\n"
            f"\nDependencies: {self._list_items(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self._list_items(self.dev_dependencies)}"
        )
