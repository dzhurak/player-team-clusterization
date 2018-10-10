from os import listdir
from random import randrange, sample
from itertools import combinations
from pathlib import Path
from shutil import copyfile


groups_to_clusterize = [
    "blue_light_black",
    "green_black",
    "purple_black",
    "red_black_white",
    "white_green",
    "yellow_blue"
]
file_path = "../team_color_dataset_splitted/train/"
dest_path = "groups_to_cluster"
players_in_team = 10
random_choice = True


def generate_file_indices():
    if random_choice:
        referee_index = randrange(len(files[referee_folder]))
        team_indices = sample(
            range(min(len(files[team1_folder]), len(files[team2_folder]))), players_in_team)
    else:
        referee_index = 0
        team_indices = range(j, j + players_in_team)
    return referee_index, team_indices


def create_images():
    referee_ix, team_ixs = generate_file_indices()
    copyfile(files[referee_folder][referee_ix], Path(
        dest_path, group_number_str + "_referee.jpg"))
    for i in team_ixs:
        copyfile(files[team1_folder][i], Path(
            dest_path, group_number_str + "_team1_" + str(i % players_in_team) + ".jpg"))
        copyfile(files[team2_folder][i], Path(
            dest_path, group_number_str + "_team2_" + str(i % players_in_team) + ".jpg"))


files = {}
for folder in groups_to_clusterize:
    files[folder] = sorted([Path(file_path, folder, f)
                            for f in listdir(Path(file_path, folder))])
group_number = 1
for referee_folder in groups_to_clusterize:
    for team1_folder, team2_folder in combinations(set(groups_to_clusterize) - {referee_folder}, 2):
        number_of_groups = min(
            (len(files[team1_folder]) // 10, len(files[team2_folder]) // 10, 20))
        for j in range(0, players_in_team * number_of_groups, players_in_team):
            group_number_str = "%04d" % group_number
            create_images()
            group_number += 1
print("Number of generated groups:", group_number)
