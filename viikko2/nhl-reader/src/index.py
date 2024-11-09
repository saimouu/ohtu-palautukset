from rich.console import Console
from rich.table import Table

from playerReader import PlayerReader
from playerStats import PlayerStats


def create_table(title):
    table = Table(title=title)
    table.add_column("name", justify="left", style="cyan")
    table.add_column("team", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    return table


def add_players_to_table(table: Table, players):
    for player in players:
        table.add_row(
            str(player.name),
            str(player.team),
            str(player.goals),
            str(player.assists),
            str(player.points),
        )
    return table


def main():
    console = Console()

    console.print("NHL statistics by nationality\n")
    season = console.input(
        "Select season\n[bold cyan][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25][/bold cyan]: "
    )

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationalities = "/".join(reader.get_nationalities())
    while True:
        nationality = console.input(
            f"Select nationality\n[bold cyan][{nationalities}][/bold cyan]: "
        )
        players = stats.top_scorers_by_nationality(nationality)
        table = create_table(f"Top scorers of {nationality} season {season}")
        console.print(add_players_to_table(table, players))


if __name__ == "__main__":
    main()
