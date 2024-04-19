"""
This data will need to be translated into a new collection.

that makes more sense for Python to do its comparisons.
"""

from constants import PLAYERS
from constants import TEAMS
import copy


player_data = copy.deepcopy(PLAYERS)  # dirty data
team_data = copy.deepcopy(TEAMS)  # dirty data

clean_players = []  # cleaned data <---


def clean_player_data():
    """
    Classify Experience True or False.

    Remove the word 'and' from height.

    Set each key pair.

    """
    for player in player_data:
        if player['experience'] == 'YES':
            player['experience'] = True
        elif player['experience'] == 'NO':
            player['experience'] = False

        player['height'] = player['height'].split(' ')[0]

        player['guardians'] = player['guardians'].split(' and ')

        clean_player = {
            'name': player['name'],
            'guardians': player['guardians'],
            'experience': player['experience'],
            'height': int(player['height'])

            }

        clean_players.append(clean_player)

all_roster_details = []


def experience_sorter(player_data):
    """Sort cleaned player data into equal parts.

    Sort experienced players vs non-experienced players into equal parts

    """
    experienced_players = []
    non_experienced_players = []

    for player in player_data:
        if player['experience'] is True:
            experienced_players.append(player)
        else:
            non_experienced_players.append(player)

    players_per_team = int(len(player) / len(team_data))
    exp_players_per_team = int(len(experienced_players) / len(team_data))
    non_exp_players_per_team = int(len(non_experienced_players) / len(team_data))

    for team in team_data:

        roster_list = []

        # now lets add the players
        for player in range(0, exp_players_per_team):
            roster_list.append(experienced_players.pop(0))
        for player in range(0, non_exp_players_per_team):
            roster_list.append(non_experienced_players.pop(0))

        # create the team details
        team_details = {
            'team_name': team,
            'roster_list': roster_list,
            'roster_total': len(roster_list)

        }

        all_roster_details.append(team_details)


def start():
    """used to run the program.

    it will allow the user to pull team data.

    while viewing team info, using our clean data.

    """
    while True:
        try:
            start = input("\nWould you like to view team roster details? (y/n)  ")

            # handle if input is not y or n
            if start.lower() != 'y' and start.lower() != 'n':
                raise Exception('\nPlease select y or n only.')

            # print list of team, ask user to select
            if start.lower() == 'y':
                print("\n\nHere is a list of our teams:")
                for index, team in enumerate(all_roster_details):
                    print(f"{index+1}. {team['team_name']}")
                selected_team = input('\nPlease select a team number:  ')

                # check the input is a number.
                if selected_team.isdigit() is False:
                    raise Exception('\nThis is not an integer. Please try again.')

                # check the input is within the range.
                if 1 > int(selected_team) or int(selected_team) > len(team_data):
                    raise Exception('\nPlease select a number corresponding to a team on this list.\n')

                # print content for selected team
                for index, team in enumerate(all_roster_details):

                    # create/print team details
                    if int(selected_team) == (index+1):

                        player_names = []
                        for player in team['roster_list']:
                            player_names.append(player['name'])
                        player_names = ', '.join(player_names)

                        print(f"""
    ___________________

    Team Name: {team['team_name'].upper()}

    Roster Total: {team['roster_total']}

    Players: {player_names}
                               """)

                        # ask if user wants more details
                        show_more = input(f"\nWould you like to see more roster information for {team['team_name']}? (y/n)  ")

                        # handle if input is not y or n
                        if show_more.lower() != 'y' and show_more.lower() != 'n':
                            raise Exception('\nPlease select (y/n)  \n')

                        # if not, quit.
                        elif show_more.lower() == "n":
                            print('_____________________\n')
                            break

                        # generate/print additional details
                        else:
                            experienced_players = []
                            non_exp_players = []
                            heights = []
                            guardians = []
                            for player in team['roster_list']:
                                if player['experience'] is True:
                                    experienced_players.append(player['name'])
                                else:
                                    non_exp_players.append(player['name'])
                                heights.append(player['height'])
                                for guardian in player['guardians']:
                                    guardians.append(guardian)
                            average_height = int(sum(heights) / len(heights))

                            print(f"""

        Experienced players: ({len(experienced_players)}) - {', '.join(experienced_players)}
        Non-experienced players: ({len(non_exp_players)}) - {', '.join(non_exp_players)}
        Average height: {average_height} inches.
        List of guardians: {', '.join(guardians)}
                                   """)

            else:
                print('\nProgram is being terminated, See you later.')
                break

        # handle non-valid input
        except ValueError:
            print('Nice try but thats not an integer. Please try again.')
        except Exception as error:
            print(error)



if __name__ == "__main__":
    clean_player_data()
    experience_sorter(clean_players)
    start()
