import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
matches = pd.read_csv('match_info_data.csv')
deliveries = pd.read_csv('match_data.csv')

sns.set_style("darkgrid")

# Chart 1 — Most Winning Teams
team_wins = matches['winner'].value_counts().head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=team_wins.values, y=team_wins.index, palette='flare')
plt.title('Top 10 Most Winning IPL Teams', fontsize=16, fontweight='bold')
plt.xlabel('Total Wins')
plt.ylabel('Team')
plt.tight_layout()
plt.savefig('team_wins.png', dpi=150)
plt.show()

# Chart 2 — Top 10 Run Scorers
top_batsmen = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=top_batsmen.values, y=top_batsmen.index, palette='rocket')
plt.title('Top 10 IPL Run Scorers of All Time', fontsize=16, fontweight='bold')
plt.xlabel('Total Runs')
plt.ylabel('Batsman')
plt.tight_layout()
plt.savefig('top_batsmen.png', dpi=150)
plt.show()

# Chart 3 — Toss Decision
toss = matches['toss_decision'].value_counts()
plt.figure(figsize=(7,7))
plt.pie(toss.values, labels=toss.index, autopct='%1.1f%%',
        colors=['#ff6b6b','#4ecdc4'], startangle=90,
        textprops={'fontsize':14})
plt.title('Toss Decision — Field vs Bat', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('toss_decision.png', dpi=150)
plt.show()

# Chart 4 — Matches Per Season
season_matches = matches['season'].value_counts().sort_index()
plt.figure(figsize=(12,6))
sns.lineplot(x=season_matches.index, y=season_matches.values,
             marker='o', color='#f7b731', linewidth=2.5, markersize=8)
plt.title('Number of IPL Matches Per Season', fontsize=16, fontweight='bold')
plt.xlabel('Season')
plt.ylabel('Total Matches')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('matches_per_season.png', dpi=150)
plt.show()

print("All 5 charts saved successfully!")