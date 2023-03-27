import requests
from bs4 import BeautifulSoup
import csv

with open("playoffs_data.csv", "w") as new_file:
    csv_writer = csv.writer(new_file, delimiter=",")
    headers = ["year", "team", "is_playoffs_team"]
    csv_writer.writerow(headers)

    start_year = 2000
    end_year = 2022

    for curr_year in range(start_year, end_year+1):
        page = requests.get("https://www.basketball-reference.com/leagues/NBA_" + str(curr_year) + ".html")
        soup = BeautifulSoup(page.text, 'html.parser')
        results = soup.find('table', {'id':'per_game-team'}).find('tbody').findAll('tr')
        print(curr_year)

        for team in results:
            team_name = team.find('td',{'data-stat': 'team'}).text.strip()
            if "*" in team_name:
                is_playoff_team = 1
                team_name = team_name.strip("*")
            else:
                is_playoff_team = 0
            new_row = [curr_year, team_name, is_playoff_team]
            csv_writer.writerow(new_row)