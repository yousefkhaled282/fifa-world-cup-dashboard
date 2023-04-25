import os
import pandas as pd

SRC_FOLDER = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
DATA_FOLDER = os.path.join(os.path.dirname(
    os.path.abspath(SRC_FOLDER)), "data/")
ASSETS_FOLDER = os.path.join(os.path.dirname(
    os.path.abspath(SRC_FOLDER)), "src/assets/")

teams = pd.read_csv(os.path.join(DATA_FOLDER, "processed/teams.csv"))
bookings = pd.read_csv(os.path.join(DATA_FOLDER, "processed/bookings.csv"))
award_winners = pd.read_csv(os.path.join(
    DATA_FOLDER, "processed/award_winners.csv"))
data = pd.read_csv(os.path.join(DATA_FOLDER, "processed/qualified_teams.csv"))
goals = pd.read_csv(os.path.join(DATA_FOLDER, "processed/goals.csv"))
tours = pd.read_csv(os.path.join(DATA_FOLDER, "processed/tournaments.csv"))
matches = pd.read_csv(os.path.join(DATA_FOLDER, "processed/matches.csv"))
team_stats = pd.read_csv(os.path.join(
    DATA_FOLDER, "processed/teams_overall_stats.csv"))

Maps = pd.read_csv(os.path.join(
    DATA_FOLDER, "processed/Map.csv"))

Country_data = pd.read_csv(os.path.join(
    DATA_FOLDER, "processed/country_data.csv"))

Goals = pd.read_csv(os.path.join(
    DATA_FOLDER, "processed/goals_Y.csv"))

Award = pd.read_csv(os.path.join(
    DATA_FOLDER, "processed/award_winners_Y.csv"))

Rank = pd.read_csv(os.path.join(
    DATA_FOLDER, "processed/fifa_ranking.csv"))