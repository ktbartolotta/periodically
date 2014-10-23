#!/usr/bin/env python

import pprint


def _periodic_table():

    return [['1', '1.0079', 'Hydrogen', 'H'], 
            ['2', '4.0026', 'Helium', 'He'], 
            ['3', '6.941', 'Lithium', 'Li'], 
            ['4', '9.0122', 'Beryllium', 'Be'], 
            ['5', '10.811', 'Boron', 'B'], 
            ['6', '12.0107', 'Carbon', 'C'], 
            ['7', '14.0067', 'Nitrogen', 'N'], 
            ['8', '15.9994', 'Oxygen', 'O'], 
            ['9', '18.9984', 'Fluorine', 'F'], 
            ['10', '20.1797', 'Neon', 'Ne'], 
            ['11', '22.9897', 'Sodium', 'Na'], 
            ['12', '24.305', 'Magnesium', 'Mg'], 
            ['13', '26.9815', 'Aluminum', 'Al'], 
            ['14', '28.0855', 'Silicon', 'Si'], 
            ['15', '30.9738', 'Phosphorus', 'P'], 
            ['16', '32.065', 'Sulfur', 'S'], 
            ['17', '35.453', 'Chlorine', 'Cl'], 
            ['18', '39.948', 'Argon', 'Ar'], 
            ['19', '39.0983', 'Potassium', 'K'], 
            ['20', '40.078', 'Calcium', 'Ca'], 
            ['21', '44.9559', 'Scandium', 'Sc'], 
            ['22', '47.867', 'Titanium', 'Ti'], 
            ['23', '50.9415', 'Vanadium', 'V'], 
            ['24', '51.9961', 'Chromium', 'Cr'], 
            ['25', '54.938', 'Manganese', 'Mn'], 
            ['26', '55.845', 'Iron', 'Fe'], 
            ['27', '58.9332', 'Cobalt', 'Co'], 
            ['28', '58.6934', 'Nickel', 'Ni'], 
            ['29', '63.546', 'Copper', 'Cu'], 
            ['30', '65.39', 'Zinc', 'Zn'], 
            ['31', '69.723', 'Gallium', 'Ga'], 
            ['32', '72.64', 'Germanium', 'Ge'], 
            ['33', '74.9216', 'Arsenic', 'As'], 
            ['34', '78.96', 'Selenium', 'Se'], 
            ['35', '79.904', 'Bromine', 'Br'], 
            ['36', '83.8', 'Krypton', 'Kr'], 
            ['37', '85.4678', 'Rubidium', 'Rb'], 
            ['38', '87.62', 'Strontium', 'Sr'], 
            ['39', '88.9059', 'Yttrium', 'Y'], 
            ['40', '91.224', 'Zirconium', 'Zr'], 
            ['41', '92.9064', 'Niobium', 'Nb'], 
            ['42', '95.94', 'Molybdenum', 'Mo'], 
            ['43', '98', 'Technetium', 'Tc'], 
            ['44', '101.07', 'Ruthenium', 'Ru'], 
            ['45', '102.9055', 'Rhodium', 'Rh'], 
            ['46', '106.42', 'Palladium', 'Pd'], 
            ['47', '107.8682', 'Silver', 'Ag'], 
            ['48', '112.411', 'Cadmium', 'Cd'], 
            ['49', '114.818', 'Indium', 'In'], 
            ['50', '118.71', 'Tin', 'Sn'], 
            ['51', '121.76', 'Antimony', 'Sb'], 
            ['52', '127.6', 'Tellurium', 'Te'], 
            ['53', '126.9045', 'Iodine', 'I'], 
            ['54', '131.293', 'Xenon', 'Xe'], 
            ['55', '132.9055', 'Cesium', 'Cs'], 
            ['56', '137.327', 'Barium', 'Ba'], 
            ['57', '138.9055', 'Lanthanum', 'La'], 
            ['58', '140.116', 'Cerium', 'Ce'], 
            ['59', '140.9077', 'Praseodymium', 'Pr'], 
            ['60', '144.24', 'Neodymium', 'Nd'], 
            ['61', '145', 'Promethium', 'Pm'], 
            ['62', '150.36', 'Samarium', 'Sm'], 
            ['63', '151.964', 'Europium', 'Eu'], 
            ['64', '157.25', 'Gadolinium', 'Gd'], 
            ['65', '158.9253', 'Terbium', 'Tb'], 
            ['66', '162.5', 'Dysprosium', 'Dy'], 
            ['67', '164.9303', 'Holmium', 'Ho'], 
            ['68', '167.259', 'Erbium', 'Er'], 
            ['69', '168.9342', 'Thulium', 'Tm'], 
            ['70', '173.04', 'Ytterbium', 'Yb'], 
            ['71', '174.967', 'Lutetium', 'Lu'], 
            ['72', '178.49', 'Hafnium', 'Hf'], 
            ['73', '180.9479', 'Tantalum', 'Ta'], 
            ['74', '183.84', 'Tungsten', 'W'], 
            ['75', '186.207', 'Rhenium', 'Re'], 
            ['76', '190.23', 'Osmium', 'Os'], 
            ['77', '192.217', 'Iridium', 'Ir'], 
            ['78', '195.078', 'Platinum', 'Pt'], 
            ['79', '196.9665', 'Gold', 'Au'], 
            ['80', '200.59', 'Mercury', 'Hg'], 
            ['81', '204.3833', 'Thallium', 'Tl'], 
            ['82', '207.2', 'Lead', 'Pb'], 
            ['83', '208.9804', 'Bismuth', 'Bi'], 
            ['84', '209', 'Polonium', 'Po'], 
            ['85', '210', 'Astatine', 'At'], 
            ['86', '222', 'Radon', 'Rn'], 
            ['87', '223', 'Francium', 'Fr'], 
            ['88', '226', 'Radium', 'Ra'], 
            ['89', '227', 'Actinium', 'Ac'], 
            ['90', '232.0381', 'Thorium', 'Th'], 
            ['91', '231.0359', 'Protactinium', 'Pa'], 
            ['92', '238.0289', 'Uranium', 'U'], 
            ['93', '237', 'Neptunium', 'Np'], 
            ['94', '244', 'Plutonium', 'Pu'], 
            ['95', '243', 'Americium', 'Am'], 
            ['96', '247', 'Curium', 'Cm'], 
            ['97', '247', 'Berkelium', 'Bk'], 
            ['98', '251', 'Californium', 'Cf'], 
            ['99', '252', 'Einsteinium', 'Es'], 
            ['100', '257', 'Fermium', 'Fm'], 
            ['101', '258', 'Mendelevium', 'Md'], 
            ['102', '259', 'Nobelium', 'No'], 
            ['103', '262', 'Lawrencium', 'Lr'], 
            ['104', '261', 'Rutherfordium', 'Rf'], 
            ['105', '262', 'Dubnium', 'Db'], 
            ['106', '266', 'Seaborgium', 'Sg'], 
            ['107', '264', 'Bohrium', 'Bh'], 
            ['108', '277', 'Hassium', 'Hs'], 
            ['109', '268', 'Meitnerium', 'Mt']]


def _get_periodic_table():

    table = []
    table_list = _periodic_table()
    for row in table_list:
        table.append(
            {
                "atomic_no": row[0],
                "atomic_wt": row[1],
                "name": row[2],
                "symbol": row[3]
            }
        )

    return table


def build_string(word):

    matches = []
    table = _get_periodic_table()

    def build(word_, match):
        for length in xrange(2, 0, -1):
            if len(word_) >= length:
                el = [r["symbol"] for r in table
                      if r["symbol"].upper() == word_[:length].upper()]
                if len(el) > 0:
                    matched = list(match + el)
                    if "".join(matched).upper() == word.upper():
                        matches.append(matched)
                        return
                    else:
                        build(word_[length:], matched)

        return
    build(word, [])
    return matches


def get_periodics(word):

    table = _get_periodic_table()
    matches = build_string(word)
    periodics = []
    if len(matches) > 0:
        for match in matches:
            m = []
            for el in match:
                m += [r for r in table if r["symbol"] == el]
            periodics.append(m)

    return periodics


def main(word):

    print build_string(word)


if __name__ == "__main__":
    pprint.pprint(get_periodics("bacon"))
