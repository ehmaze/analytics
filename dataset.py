import pandas as pd
import numpy as np
import csv
import sys


def load(filename, final_week):
    """Load data from csv."""

    team_dict = {}
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for i, team in enumerate(reader):

            # first row just metadata, so ignore
            if i == 0:
                continue
            
            # first entry is team name
            cur = team[0]
            team_dict[cur] = []

            # loop thru team data
            for j, entry in enumerate(team[1:]):

                # if week doesnt exist
                if j % 16 >= final_week:
                    continue
                
                # first 16 are str
                if j < 16:
                    team_dict[cur].append(entry)
                
                # otherwise float
                else:
                    team_dict[cur].append(float(entry))
            
    return team_dict

# normalize all stats [-1, 1]
def normalize(filename, final_week):
    """Normalize loaded data."""

    # Normalization factors, highest in each stat
    factors = []

    # load team dictionary
    team_dict = load(filename, final_week)
    for _, entries in team_dict.items():
        for i, val in entries[final_week:]:

            
