color_list = ['alizarin', 'amaranth', 'amber', 'amethyst', 'apricot', 'aqua',
              'aquamarine', 'asparagus', 'auburn', 'azure', 'beige', 'bistre', 'black',
              'blue', 'blue-green', 'blue-violet', 'bondi-blue', 'brass', 'bronze',
              'brown', 'buff', 'burgundy', 'camouflage-green', 'caput-mortuum',
              'cardinal', 'carmine', 'carrot-orange', 'celadon', 'cerise', 'cerulean',
              'champagne', 'charcoal', 'chartreuse', 'cherry-blossom-pink', 'chestnut',
              'chocolate', 'cinnabar', 'cinnamon', 'cobalt', 'copper', 'coral', 'corn',
              'cornflower', 'cream', 'crimson', 'cyan', 'dandelion', 'denim', 'ecru',
              'emerald', 'eggplant', 'falu-red', 'fern-green', 'firebrick', 'flax',
              'forest-green', 'french-rose', 'fuchsia', 'gamboge', 'gold', 'goldenrod',
              'green', 'grey', 'han-purple', 'harlequin', 'heliotrope',
              'hollywood-cerise', 'indigo', 'ivory', 'jade', 'kelly-green', 'khaki',
              'lavender', 'lawn-green', 'lemon', 'lemon-chiffon', 'lilac', 'lime',
              'lime-green', 'linen', 'magenta', 'magnolia', 'malachite', 'maroon',
              'mauve', 'midnight-blue', 'mint-green', 'misty-rose', 'moss-green',
              'mustard', 'myrtle', 'navajo-white', 'navy-blue', 'ochre', 'office-green',
              'olive', 'olivine', 'orange', 'orchid', 'papaya-whip', 'peach', 'pear',
              'periwinkle', 'persimmon', 'pine-green', 'pink', 'platinum', 'plum',
              'powder-blue', 'puce', 'prussian-blue', 'psychedelic-purple', 'pumpkin',
              'purple', 'quartz-grey', 'raw-umber', 'razzmatazz', 'red', 'robin-egg-blue',
              'rose', 'royal-blue', 'royal-purple', 'ruby', 'russet', 'rust',
              'safety-orange', 'saffron', 'salmon', 'sandy-brown', 'sangria', 'sapphire',
              'scarlet', 'school-bus-yellow', 'sea-green', 'seashell', 'sepia',
              'shamrock-green', 'shocking-pink', 'silver', 'sky-blue', 'slate-grey',
              'smalt', 'spring-bud', 'spring-green', 'steel-blue', 'tan', 'tangerine',
              'taupe', 'teal', 'tenné-(tawny)', 'terra-cotta', 'thistle',
              'titanium-white', 'tomato', 'turquoise', 'tyrian-purple', 'ultramarine',
              'van-dyke-brown', 'vermilion', 'violet', 'viridian', 'wheat', 'white',
              'wisteria', 'yellow', 'zucchini']


def validate_color_name(name: str):
    if name.lower() not in color_list:
        return False
    return True


def get_color_names_choice_tuple():
    tuple_of_tuples = tuple((color, color) for color in color_list)
    return tuple_of_tuples
