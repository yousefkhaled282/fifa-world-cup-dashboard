from src.utils.consts import Maps as map_df
import pandas as pd



"""World cup Map"""


tournament_names = ['1930 FIFA World Cup', '1934 FIFA World Cup', '1938 FIFA World Cup',
                    '1950 FIFA World Cup', '1954 FIFA World Cup', '1958 FIFA World Cup',
                    '1962 FIFA World Cup', '1966 FIFA World Cup', '1970 FIFA World Cup',
                    '1974 FIFA World Cup', '1978 FIFA World Cup', '1982 FIFA World Cup',
                    '1986 FIFA World Cup', '1990 FIFA World Cup', '1994 FIFA World Cup',
                    '1998 FIFA World Cup', '2002 FIFA World Cup', '2006 FIFA World Cup',
                    '2010 FIFA World Cup', '2014 FIFA World Cup', '2018 FIFA World Cup', '2022 FIFA World Cup']
country_data = map_df.groupby(['tournament_name', 'country_name', 'latitude', 'longitude', 'location'])[
    'score'].sum().reset_index()
country_data['goals_per_match'] = pd.Series([None] * len(country_data), dtype=float)
country_data['games_played'] = pd.Series([None] * len(country_data), dtype=float)
country_data['avg_player_age'] = pd.Series([None] * len(country_data), dtype=float)
country_data['num_players'] = pd.Series([None] * len(country_data), dtype=float)

for tournament in tournament_names:
    file_path = f"G:/ai & ML ITI 9 month/fifa-worldcup-dashboard-main/fifa-worldcup-dashboard-main/data/processed/Card/{tournament[:4]}_card.csv"
    df_card = pd.read_csv(file_path)
    mask = (country_data['tournament_name'] == tournament)
    row_location = country_data.loc[mask].index[0]
    country_data['goals_per_match'].iloc[row_location] = df_card['goals_per_match'].iloc[0]
    country_data['games_played'].iloc[row_location] = df_card['games_played'].iloc[0]
    country_data['avg_player_age'].iloc[row_location] = df_card['avg_player_age'].iloc[0]
    country_data['num_players'].iloc[row_location] = df_card['num_players'].iloc[0]

mask = (country_data['country_name'] == 'Japan')
row_location = country_data.loc[mask].index[0]
country_data['goals_per_match'].fillna(country_data['goals_per_match'].iloc[row_location],inplace =True)
country_data['games_played'].fillna(country_data['games_played'].iloc[row_location],inplace =True)
country_data['avg_player_age'].fillna(country_data['avg_player_age'].iloc[row_location],inplace =True)
country_data['num_players'].fillna(country_data['num_players'].iloc[row_location],inplace =True)
country_data['goals_per_match'].iloc[3] = country_data['goals_per_match'].iloc[3].replace('g','').strip()
country_data['num_players'] = country_data['num_players'].astype(int)
country_data['hover_text'] = country_data['country_name'] + '<br>' + country_data['tournament_name'] + '<br>'+'Goals Per Match'+': '+ country_data['goals_per_match'].astype(str)+'<br>'+'Average Player Age'+': '+country_data['avg_player_age'].astype(str)+'<br>'+'Numbers of Players'+': '+country_data['num_players'].astype(str)
country_data['score'] = country_data['score'].astype(int)




country_data.to_csv('G:/ai & ML ITI 9 month/fifa-worldcup-dashboard-main/fifa-worldcup-dashboard-main/data/processed/country_data.csv',index=False)

