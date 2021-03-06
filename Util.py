items = ['Apple','Bag','BlueBook','BlueCloth','BlueKey','BluePotion','Bottle','Bread','ChickenLeg','Coin','Compass','Cup','EvilBook','GoldCup','GreenBook','GreenKey','GreenPotion','Hammer','Helmet','InkandQuill','JewelKey','LitTorch','Lock','MagnifyingGlass','OpenScroll','PurpleBook','PurpleCloth','PurpleKey','PurplePotion','Rags','RedBook','RedCloth','RedKey','RedPotion','Scroll','Skull','SpellBook','Sword','Torch']
places = ['AlchemyShop','Blacksmith','Bridge','Camp','CastleBedroom','CastleCrossroads','City','Cottage','Courtyard','DiningRoom','Dungeon','Farm','ForestPath','GreatHall','Hallway','Library','Port','Ruins','SpookyPath','Storage','Tavern']

# create experience manager 'test_env.py'
def initialize():
    try:
        with open('test_env.py','w') as f:
            f.write('def action(command):\n\tprint(\'start \' + command)\n\twhile(True):\n\t\ti = input()\n\t\tif(i == \'succeeded \' + command):\n\t\t\treturn True\n\t\telif(i == \'failed \' + command):\n\t\t\treturn False\n\t\telif(i.startswith(\'error\')):\n\t\t\treturn False\n')

            # Create list of items and places
            f.write('\nitems = [\'Apple\',\'Bag\',\'BlueBook\',\'BlueCloth\',\'BlueKey\',\'BluePotion\',\'Bottle\',\'Bread\',\'ChickenLeg\',\'Coin\',\'Compass\',\'Cup\',\'EvilBook\',\'GoldCup\',\'GreenBook\',\'GreenKey\',\'GreenPotion\',\'Hammer\',\'Helmet\',\'InkandQuill\',\'JewelKey\',\'LitTorch\',\'Lock\',\'MagnifyingGlass\',\'OpenScroll\',\'PurpleBook\',\'PurpleCloth\',\'PurpleKey\',\'PurplePotion\',\'Rags\',\'RedBook\',\'RedCloth\',\'RedKey\',\'RedPotion\',\'Scroll\',\'Skull\',\'SpellBook\',\'Sword\',\'Torch\']')
            f.write('\nplaces = [\'AlchemyShop\',\'Blacksmith\',\'Bridge\',\'Camp\',\'CastleBedroom\',\'CastleCrossroads\',\'City\',\'Cottage\',\'Courtyard\',\'DiningRoom\',\'Dungeon\',\'Farm\',\'ForestPath\',\'GreatHall\',\'Hallway\',\'Library\',\'Port\',\'Ruins\',\'SpookyPath\',\'Storage\',\'Tavern\']\n')
            
            # create Bob
            f.write('\naction(\'CreateCharacter(Bob, D)\')')
            f.write('\naction(\'SetClothing(Bob, Peasant)\')')
            f.write('\naction(\'SetHairStyle(Bob, Spiky)\')\n')

            # create places
            f.write('\nfor p in places:\n\taction(f\'CreatePlace({p},{p})\')\n')

            # create items, add to inventory, and create icons for interaction
            f.write('\nfor i in items:\n\taction(f\'CreateItem({i},{i})\')\n\taction(f\'AddToList({i})\')\n\taction(f\'EnableIcon("un_pocket", draw, {i}, "Unpocket {i}")\')\n\taction(f\'EnableIcon("pocket", return, {i}, "Pocket {i}")\')\n\taction(f\'EnableIcon("pickup", hand, {i}, "Pickup {i}")\')\n\taction(f\'EnableIcon("putdown", cancel, {i},"Putdown {i}")\')\n')

            # create icons
            f.write('\naction(\'EnableIcon("Open_Door", exit, Port.BigShip, "Go to CastleCrossroads", true)\')')

            # start game
            f.write('\naction(\'SetPosition(Bob, Cottage.Door)\')')
            f.write('\naction(\'ShowMenu()\')\n')

            # input handler
            f.write('\nwhile(True):\n\ti = input()\n\tif(i == \'input Selected Start\' or i == \'input Selected Resume\'):\n\t\taction(\'SetCameraFocus(Bob)\')\n\t\taction(\'HideMenu()\')\n\t\taction(\'EnableInput()\')\n\telif(i == \'input Key Inventory\'):\n\t\taction(\'ShowList(Bob)\')\n\telif(i == \'input Close List\'):\n\t\taction(\'HideList()\')\n\telif(i == \'input Key Pause\'):\n\t\taction(\'ShowMenu()\')\n\telif(i == \'input Selected Quit\'):\n\t\taction(\'Quit()\')\n\telif(i == \'input Close Narration\'):\n\t\taction(\'HideNarration()\')')
            
            # connect places
            f.write(connect('Cottage','Door','City','GreenHouseDoor'))
            f.write(connect('City','BrownHouseDoor','Blacksmith','Door'))
            f.write(connect('City','RedHouseDoor','Tavern','Door'))
            f.write(connect('City','BlueHouseDoor','AlchemyShop','Door'))
            f.write(connect('City','EastEnd','Bridge','WestEnd'))
            f.write(connect('Bridge','SouthEnd','Camp','Exit'))
            f.write(connect('Bridge','NorthEnd','SpookyPath','EastEnd'))
            f.write(connect('SpookyPath','WestEnd','Ruins','Exit'))
            f.write(connect('City','NorthEnd','ForestPath','EastEnd'))
            f.write(connect('ForestPath','WestEnd','Farm','Exit'))
            f.write(connect('City','WestEnd','Port','Exit'))
            f.write('\n\telif(i == \'input Open_Door Port.BigShip\'):\n\t\taction(\'FadeOut()\')\n\t\taction(\'SetPosition(Bob, CastleCrossroads.WestEnd)\')\n\t\taction(\'FadeIn()\')\n\telif(i == \'input arrived Bob position CastleCrossroads.WestEnd\'):\n\t\taction(\'FadeOut()\')\n\t\taction(\'SetPosition(Bob, Port.BigShip)\')\n\t\taction(\'FadeIn()\')')
            f.write(connect('CastleCrossroads','Gate','Courtyard','Exit'))
            f.write(connect('Courtyard','Gate','Hallway','Door'))
            f.write(connect('Hallway','Stairs','Library','Door'))
            f.write(connect('Hallway','BackDoor','GreatHall','Gate'))
            f.write(connect('GreatHall','BasementDoor','Dungeon','Door'))
            f.write(connect('GreatHall','LeftDoor','CastleBedroom','Door'))
            f.write(connect('GreatHall','RightDoor','DiningRoom','Door'))
            f.write(connect('DiningRoom','BackDoor','Storage','Door'))

            # Select Item from Inv.
            for i in items:
                f.write(itemInput(i))
                     
    except IOError as e:
        print("I/O error({0}): {1}").format(e.errno, e.strerror)
    finally:
        # close file
        f.close()
        

    # connect 2 places at the given doors within the input handler
def connect(place1, door1, place2, door2):
    if(place1 in places and place2 in places):
        input1 = f'input arrived Bob position {place1}.{door1}'
        input2 = f'input arrived Bob position {place2}.{door2}'

        # create elif branch
        output = f'\n\telif(i == \'{input1}\'):\n\t\taction(\'Exit(Bob, {place1}.{door1}, true)\')\n\t\taction(\'Enter(Bob, {place2}.{door2}, true)\')\n\telif(i == \'{input2}\'):\n\t\taction(\'Exit(Bob, {place2}.{door2}, true)\')\n\t\taction(\'Enter(Bob, {place1}.{door1}, true)\')'
    
        return output   
    else:
        print("One of the places given in connect() is not valid.")
        return "Invalid Input"
    

# create input handling for item interactions
def itemInput(item):
    if(item in items):
        output = f'\n\telif(i == \'input un_pocket {item}\'):\n\t\taction(\'Unpocket(Bob, {item})\')\n\telif(i == \'input pocket {item}\'):\n\t\taction(\'Pocket(Bob, {item})\')\n\telif(i == \'input pickup {item}\'):\n\t\taction(\'Pickup(Bob, {item})\')\n\telif(i == \'input putdown {item}\'):\n\t\taction(\'PutDown(Bob, {item})\')'
        return output
    else: 
        print("Item given to itemInput() is not valid.")
        return "Invalid Input"


initialize()

