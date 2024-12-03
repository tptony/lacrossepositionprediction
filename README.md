## Setup & Installation
1. Clone the repository
```
git clone ...
```

2. Setup your environment
This project uses a virtual environment to manage dependencies. To create a virtual environment and install all the depenencies, run the following bash script:
```
source setup.sh
```

This will also create a simple alias to run the command line tool.

3. Copy the environment file and fill in the necessary values
``` 
cp .env_sample .env
```
#### Data Access Statement
The dataset we used was compiled by Matt Hudson and is hosted on Amazon RDS in a relational dataset. The dataset is modeled as a star schema of information on NCAA Men’s Division 1, 2, and 3 lacrosse from 2015 through 2023. This includes data on the Programs (e.g. Schools), Seasons, Games, Box Scores (results of a game), and Play-by-Plays (events for each game).

There are roughly 3,000 games per season across all divisions. Each game has about 500 rows of play-by-play and box score data by player. This equates to nearly 12 million rows of data in total. The data was already pre-cleaned – but required modeling for the purposes described above.
All of this data was made accessible through any Postgres client, but our team primarily used a python class built on top of psycopg2 for easy reproducibility.

Please reach out if you have issues accessing the data. The `LaxDB` credentials (host, port, user, password, and name) can be obtained from Matt. 
