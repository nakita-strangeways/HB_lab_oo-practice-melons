############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller


        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.add_pairing = self.pairings.extend(pairing) #add pairing(as a list since extend is a list) to add pairing list

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.update_code = new_code

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairing(['mint'])
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    cas.add_pairing(['strawberries', 'mint'])
    all_melon_types.append(cas)

    cren = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    cren.add_pairing(['proscuitto'])
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', False, True)
    yw.add_pairing(['ice cream'])
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print('{} pairs with'.format(melon.name))

        for pair in melon.pairings:
            print('- {}'.format(pair))



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_dict = {}

    for melon in melon_types:
        if melon.code in melon_type_dict:
            melon_type_dict[melon.code] += melon        #everything in melon

        else:
            melon_type_dict[melon.code] = melon


    print(melon_type_dict)

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest


all_melon_types_list = make_melon_types()
print_pairing_info(all_melon_types_list)
make_melon_type_lookup(all_melon_types_list)

