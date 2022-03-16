import sys
import requests


def grouped_teams():
    api_url = "https://www.balldontlie.io/api/v1/teams"
    teams = requests.get(api_url)
    region = {}
    for team in teams.json()["data"]:
        if team["division"] not in region:
            region[team["division"]] = list()
        region[team["division"]].append(team["full_name"] + " (" + team["abbreviation"] + ")")
    for key, value in region.items():
        print(key)
        for i in range(len(value)):
            print(" " + value[i])


def player_stats(name):
    api_url = f"https://www.balldontlie.io/api/v1/players/?search={name}"
    players = requests.get(api_url, params={"per_page": "100"})
    answer = {
        "tallest": [0, " "],
        "heaviest": [0, " "]
    }
    for player in players.json()["data"]:
        if None in (player["height_feet"], player["height_inches"], player["weight_pounds"]):
            continue
        if answer["tallest"][0] < player["height_feet"] * 0.3048 + 0.0254 * player["height_inches"]:
            answer["tallest"] = [round(player["height_feet"] * 0.3048 + 0.0254 * player["height_inches"], 2),
                                 player["first_name"] + " " + player["last_name"]]
        if answer["heaviest"][0] < player["weight_pounds"] * 0.045359237:
            answer["heaviest"] = [round(player["weight_pounds"] * 0.45359237),
                                  player["first_name"] + " " + player["last_name"]]
    if answer["tallest"][0] != 0:
        print(f'The tallest player: {answer["tallest"][1]} {answer["tallest"][0]} meters')
        print(f'The heaviest player: {answer["heaviest"][1]} {answer["heaviest"][0]} kilograms')
    else:
        print(f'The tallest player: Not found')
        print(f'The heaviest player: Not found')


def teams_stats(season):
    games_list = list()
    api_url = f"https://www.balldontlie.io/api/v1/games/?seasons[]={season}"
    games = requests.get(api_url, params={"per_page": "100"})
    for a in range(games.json()["meta"]["total_pages"]):
        games_list.extend(requests.get(api_url, params={"per_page": "100", 'page': f"{a}"}).json()["data"])
    results = {}  # "team_name" : ["won_home_team","won_visitor_team","lost_home_team","lost_visitor_team"
    for match in games_list:
        visitors_team_name = match["visitor_team"]["full_name"] + "(" + match["visitor_team"]["abbreviation"] + ")"
        home_team_name = match["home_team"]["full_name"] + "(" + match["home_team"]["abbreviation"] + ")"

        if home_team_name not in results:
            results[home_team_name] = [0, 0, 0, 0]

        if visitors_team_name not in results:
            results[visitors_team_name] = [0, 0, 0, 0]

        if match['home_team_score'] > match['visitor_team_score']:
            results[home_team_name][0] += 1
            results[visitors_team_name][3] += 1
        else:
            results[home_team_name][2] += 1
            results[visitors_team_name][1] += 1
    for key, value in results.items():
        print(key)
        print("  won games as home team:" + str(value[0]))
        print("  won games as visitor team:" + str(value[1]))
        print("  lost games as home team:" + str(value[2]))
        print("  lost games as visitor team:" + str(value[3]))


if __name__ == '__main__':
    print(sys.argv[1:])
    while True:
        try:
            if len(sys.argv) == 2 and sys.argv[1].lower() == "grouped-teams":
                grouped_teams()
                break
            elif sys.argv[1].lower() == "players-stats":
                if sys.argv[2].lower() == "--name":
                    name = sys.argv[3]
                    player_stats(name)
                else:
                    print("Please enter a valid command e.g.(player-stats --name Jordan)")
            elif sys.argv[1].lower() == "team-stats":
                if sys.argv[2].lower() == "--season":
                    season = sys.argv[3]
                    teams_stats(season)
                else:
                    print("Please enter a valid command e.g.(player-stats --name Jordan)")
                pass
        except:
            IndexError
        finally:
            break

