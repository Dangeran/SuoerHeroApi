import requests

heroes = ["Hulk", "Captain America", "Thanos"]
superhero_host = "https://akabab.github.io/superhero-api/api/"


def get_heroes():
    return requests.get(superhero_host + 'all.json')


def get_heroes_intelligence(heroes_list):
    heroes_intelligence = {}
    for hero in get_heroes().json():
        if hero['name'] in heroes_list:
            heroes_intelligence[hero['name']] = hero['powerstats']['intelligence']
    return heroes_intelligence


if __name__ == '__main__':
    best_hero_name = ''
    best_hero_intelligence = 0
    heroes_intelligences = get_heroes_intelligence(heroes)
    print('Список героев и их интеллект:')
    for hero_name, hero_intelligence in heroes_intelligences.items():
        print(f"{hero_name}: {hero_intelligence}")
        if hero_intelligence > best_hero_intelligence:
            best_hero_name, best_hero_intelligence = hero_name, hero_intelligence
    if best_hero_name:
        print(f"Самый умный герой - {best_hero_name} с интеллектом {best_hero_intelligence}")
