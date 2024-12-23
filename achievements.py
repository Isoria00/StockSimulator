import json


def load_achievements():
    with open('achievements.json', 'r') as file:
        return json.load(file)


def save_achievements(achievements_data):
    with open('achievements.json', 'w') as file:
        json.dump(achievements_data, file, indent=4)


def check_achievements(player_data, achievements_data):
    for achievement in achievements_data['achievements']:
        if not achievement['earned']:
            if 'difficulty' in achievement['criteria'] and achievement['criteria']['difficulty'] == player_data['difficulty'] and achievement['criteria']['win'] == player_data['win']:
                achievement['earned'] = True
            elif 'win_game' in achievement['criteria'] and player_data['win_game']:
                achievement['earned'] = True
            elif 'investment_total' in achievement['criteria'] and player_data['investment_total'] >= achievement['criteria']['investment_total']:
                achievement['earned'] = True
            elif 'high_risk_investment' in achievement['criteria'] and player_data['high_risk_investment']:
                achievement['earned'] = True


def update_player_progress(player_data):
    
    if player_data['difficulty'] == 150:
        player_data['difficulty'] = 'easy'
    elif player_data['difficulty'] == 300:
        player_data['difficulty'] = 'medium'
    elif player_data['difficulty'] == 500:
        player_data['difficulty'] = 'hard'

    
    achievements_data = load_achievements()
    
    
    check_achievements(player_data, achievements_data)
    
    
    save_achievements(achievements_data)

