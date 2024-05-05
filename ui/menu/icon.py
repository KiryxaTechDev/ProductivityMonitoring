from utils.data_utils import *

images = read_json('data\\settings.json')['left_menu_icons']

MENU = load_img(images['menu'])
HOME = load_img(images['home'])
GOALS_AND_OBJECTIVES = load_img(images['goals_and_objectives'])
STATISTICS = load_img(images['statistics'])
SETTINGS = load_img(images['settings'])