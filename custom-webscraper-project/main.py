from selenium import webdriver
from selenium.webdriver.common.by import By
import time

urls = ["https://www.nba.com/stats",
        "https://www.audible.com/search?keywords=book&node=18573211011",        #URLs can change overtime 
        "https://steamdb.info/"]

website = int(input("What data would you like to scrape:\n"
                    "1)NBA player stats\n"
                    "2)Audible books and ratings\n"
                    "3)Steam Games Data\n"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

if website == 1:
    driver.get(url=urls[0])
    time.sleep(0.5)
    try:
        driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button').click()                 
    finally:                                                                                                      #XPaths and class names are subject to changes overtime
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[2]/'
                                      'button[2]').click()
    time.sleep(0.5)
    stats = driver.find_elements(By.CLASS_NAME, 'LeaderBoardWithButtons_lbwbCardWrapper__re1TJ')
    data = [stat.text.split('\n') for stat in stats]
    chunked_list_players = [data[0][i:i + 6] for i in range(0, 54, 6)]
    chunked_list_teams = [data[1][i:i + 3] for i in range(0, 27, 3)]
    with open('NBA_stats.csv', 'w') as file:
        file.write(f"Player\n")
        for stats in chunked_list_players:
            file.write(f"{stats}\n")
        file.write(f"Teams\n")
        for stats in chunked_list_teams:
            file.write(f"{stats}\n")
elif website == 2:
    driver.get(url=urls[1])
    time.sleep(2)
    books = []
    for i in range(1, 20):
        books.append(driver.find_element(By.XPATH, f'//*[@id="center-3"]/div/div/div/span[2]/ul/li[{i}]').text
                     .split("\n"))
    for book in books:
        del book[0]
    with open("books.csv", 'w') as file:
        file.write("Name             " "Description\n")
        for book in books:
            file.write(f"{book}\n")
elif website == 3:
    driver.get(url=urls[2])
    time.sleep(2)
    data = driver.find_elements(By.CLASS_NAME, 'app')
    most_played = []
    trending_games = []
    popular_releases = []
    hot_releases = []
    for i in range(59):
        if i <= 14:
            most_played.append(data[i].text)
        elif i <= 29:
            trending_games.append(data[i].text)
        elif i <= 44:
            popular_releases.append(data[i].text)
        else:
            hot_releases.append(data[i].text)
    most_played_games = []
    most_played_current_players = []
    most_played_peak_players = []
    trending_game = []
    trending_games_players_now = []
    popular_releases_games = []
    popular_releases_24h_peak = []
    popular_releases_price = []
    hot_releases_games = []
    hot_releases_rating = []
    hot_releases_price = []
    for item in most_played:
        parts = item.rsplit(' ', 2)
        most_played_games.append(parts[0])
        most_played_current_players.append(parts[1])
        most_played_peak_players.append(parts[2])
    for item in trending_games:
        parts = item.rsplit(' ', 1)
        trending_game.append(parts[0])
        trending_games_players_now.append(parts[1])
    for item in popular_releases:
        parts = item.rsplit(' ', 2)
        popular_releases_games.append(parts[0])
        popular_releases_24h_peak.append(parts[1])
        popular_releases_price.append(parts[2])
    for item in hot_releases:
        parts = item.rsplit(' ', 2)
        hot_releases_games.append(parts[0])
        hot_releases_rating.append(parts[1])
        hot_releases_price.append(parts[2])
    with open("steam_games_data.csv", "w") as file:
        file.write("Most played games\nGame                   Players now                24hr peak\n")
        for i in range(len(most_played_games)-1):
            file.write(f"{most_played_games[i]}     {most_played_current_players[i]}   {most_played_peak_players[i]}\n")
        file.write("\nTrending games\n Game                   Players now\n")
        for i in range(len(trending_game)-1):
            file.write(f"{trending_game[i]}            {trending_games_players_now[i]}\n")
        file.write("\nPopular releases\n Game                24hr peak                 Price\n")
        for i in range(len(popular_releases_games)-1):
            file.write(f"{popular_releases_games[i]}     {popular_releases_24h_peak[i]}  {popular_releases_price[i]}\n")
        file.write("\nHot releases\n Game              Rating                    Price\n")
        for i in range(len(hot_releases_games)-1):
            file.write(f"{hot_releases_games[i]}      {hot_releases_rating[i]}       {hot_releases_price[i]}\n")
