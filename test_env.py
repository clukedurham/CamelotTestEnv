def action(command):
	print('start ' + command)
	while(True):
		i = input()
		if(i == 'succeeded ' + command):
			return True
		elif(i == 'failed ' + command):
			return False
		elif(i.startswith('error')):
			return False

items = ['Apple','Bag','BlueBook','BlueCloth','BlueKey','BluePotion','Bottle','Bread','ChickenLeg','Coin','Compass','Cup','EvilBook','GoldCup','GreenBook','GreenKey','GreenPotion','Hammer','Helmet','InkandQuill','JewelKey','LitTorch','Lock','MagnifyingGlass','OpenScroll','PurpleBook','PurpleCloth','PurpleKey','PurplePotion','Rags','RedBook','RedCloth','RedKey','RedPotion','Scroll','Skull','SpellBook','Sword','Torch']
places = ['AlchemyShop','Blacksmith','Bridge','Camp','CastleBedroom','CastleCrossroads','City','Cottage','Courtyard','DiningRoom','Dungeon','Farm','ForestPath','GreatHall','Hallway','Library','Port','Ruins','SpookyPath','Storage','Tavern']

action('CreateCharacter(Bob, D)')
action('SetClothing(Bob, Peasant)')
action('SetHairStyle(Bob, Spiky)')

for p in places:
	action(f'CreatePlace({p},{p})')

for i in items:
	action(f'CreateItem({i},{i})')
	action(f'AddToList({i})')

action('EnableIcon("Open_Door", exit, Port.BigShip, "Go to CastleCrossroads", true)')
action('SetPosition(Bob, Cottage.Door)')
action('ShowMenu()')

while(True):
	i = input()
	if(i == 'input Selected Start' or i == 'input Selected Resume'):
		action('SetCameraFocus(Bob)')
		action('HideMenu()')
		action('EnableInput()')
	elif(i == 'input Key Inventory'):
		action('ShowList(Bob)')
	elif(i == 'input Close List'):
		action('HideList()')
	elif(i == 'input Key Pause'):
		action('ShowMenu()')
	elif(i == 'input Selected Quit'):
		action('Quit()')
	elif(i == 'input Close Narration'):
		action('HideNarration()')
	elif(i == 'input arrived Bob position Cottage.Door'):
		action('Exit(Bob, Cottage.Door, true)')
		action('Enter(Bob, City.GreenHouseDoor, true)')
	elif(i == 'input arrived Bob position City.GreenHouseDoor'):
		action('Exit(Bob, City.GreenHouseDoor, true)')
		action('Enter(Bob, Cottage.Door, true)')
	elif(i == 'input arrived Bob position City.BrownHouseDoor'):
		action('Exit(Bob, City.BrownHouseDoor, true)')
		action('Enter(Bob, Blacksmith.Door, true)')
	elif(i == 'input arrived Bob position Blacksmith.Door'):
		action('Exit(Bob, Blacksmith.Door, true)')
		action('Enter(Bob, City.BrownHouseDoor, true)')
	elif(i == 'input arrived Bob position City.RedHouseDoor'):
		action('Exit(Bob, City.RedHouseDoor, true)')
		action('Enter(Bob, Tavern.Door, true)')
	elif(i == 'input arrived Bob position Tavern.Door'):
		action('Exit(Bob, Tavern.Door, true)')
		action('Enter(Bob, City.RedHouseDoor, true)')
	elif(i == 'input arrived Bob position City.BlueHouseDoor'):
		action('Exit(Bob, City.BlueHouseDoor, true)')
		action('Enter(Bob, AlchemyShop.Door, true)')
	elif(i == 'input arrived Bob position AlchemyShop.Door'):
		action('Exit(Bob, AlchemyShop.Door, true)')
		action('Enter(Bob, City.BlueHouseDoor, true)')
	elif(i == 'input arrived Bob position City.EastEnd'):
		action('Exit(Bob, City.EastEnd, true)')
		action('Enter(Bob, Bridge.WestEnd, true)')
	elif(i == 'input arrived Bob position Bridge.WestEnd'):
		action('Exit(Bob, Bridge.WestEnd, true)')
		action('Enter(Bob, City.EastEnd, true)')
	elif(i == 'input arrived Bob position Bridge.SouthEnd'):
		action('Exit(Bob, Bridge.SouthEnd, true)')
		action('Enter(Bob, Camp.Exit, true)')
	elif(i == 'input arrived Bob position Camp.Exit'):
		action('Exit(Bob, Camp.Exit, true)')
		action('Enter(Bob, Bridge.SouthEnd, true)')
	elif(i == 'input arrived Bob position Bridge.NorthEnd'):
		action('Exit(Bob, Bridge.NorthEnd, true)')
		action('Enter(Bob, SpookyPath.EastEnd, true)')
	elif(i == 'input arrived Bob position SpookyPath.EastEnd'):
		action('Exit(Bob, SpookyPath.EastEnd, true)')
		action('Enter(Bob, Bridge.NorthEnd, true)')
	elif(i == 'input arrived Bob position SpookyPath.WestEnd'):
		action('Exit(Bob, SpookyPath.WestEnd, true)')
		action('Enter(Bob, Ruins.Exit, true)')
	elif(i == 'input arrived Bob position Ruins.Exit'):
		action('Exit(Bob, Ruins.Exit, true)')
		action('Enter(Bob, SpookyPath.WestEnd, true)')
	elif(i == 'input arrived Bob position City.NorthEnd'):
		action('Exit(Bob, City.NorthEnd, true)')
		action('Enter(Bob, ForestPath.EastEnd, true)')
	elif(i == 'input arrived Bob position ForestPath.EastEnd'):
		action('Exit(Bob, ForestPath.EastEnd, true)')
		action('Enter(Bob, City.NorthEnd, true)')
	elif(i == 'input arrived Bob position ForestPath.WestEnd'):
		action('Exit(Bob, ForestPath.WestEnd, true)')
		action('Enter(Bob, Farm.Exit, true)')
	elif(i == 'input arrived Bob position Farm.Exit'):
		action('Exit(Bob, Farm.Exit, true)')
		action('Enter(Bob, ForestPath.WestEnd, true)')
	elif(i == 'input arrived Bob position City.WestEnd'):
		action('Exit(Bob, City.WestEnd, true)')
		action('Enter(Bob, Port.Exit, true)')
	elif(i == 'input arrived Bob position Port.Exit'):
		action('Exit(Bob, Port.Exit, true)')
		action('Enter(Bob, City.WestEnd, true)')
	elif(i == 'input arrived Bob position Port.EastEnd'):
		action('Exit(Bob, Port.EastEnd, true)')
		action('Enter(Bob, Bridge.WestEnd, true)')
	elif(i == 'input arrived Bob position Bridge.WestEnd'):
		action('Exit(Bob, Bridge.WestEnd, true)')
		action('Enter(Bob, Port.EastEnd, true)')
	elif(i == 'input Open_Door Port.BigShip'):
		action('FadeOut()')
		action('SetPosition(Bob, CastleCrossroads.WestEnd)')
		action('FadeIn()')
	elif(i == 'input arrived Bob position CastleCrossroads.WestEnd'):
		action('FadeOut()')
		action('SetPosition(Bob, Port.BigShip)')
		action('FadeIn()')
	elif(i == 'input arrived Bob position CastleCrossroads.Gate'):
		action('Exit(Bob, CastleCrossroads.Gate, true)')
		action('Enter(Bob, Courtyard.Exit, true)')
	elif(i == 'input arrived Bob position Courtyard.Exit'):
		action('Exit(Bob, Courtyard.Exit, true)')
		action('Enter(Bob, CastleCrossroads.Gate, true)')
	elif(i == 'input arrived Bob position Courtyard.Gate'):
		action('Exit(Bob, Courtyard.Gate, true)')
		action('Enter(Bob, Hallway.Door, true)')
	elif(i == 'input arrived Bob position Hallway.Door'):
		action('Exit(Bob, Hallway.Door, true)')
		action('Enter(Bob, Courtyard.Gate, true)')
	elif(i == 'input arrived Bob position Hallway.Stairs'):
		action('Exit(Bob, Hallway.Stairs, true)')
		action('Enter(Bob, Library.Door, true)')
	elif(i == 'input arrived Bob position Library.Door'):
		action('Exit(Bob, Library.Door, true)')
		action('Enter(Bob, Hallway.Stairs, true)')
	elif(i == 'input arrived Bob position Hallway.BackDoor'):
		action('Exit(Bob, Hallway.BackDoor, true)')
		action('Enter(Bob, GreatHall.Gate, true)')
	elif(i == 'input arrived Bob position GreatHall.Gate'):
		action('Exit(Bob, GreatHall.Gate, true)')
		action('Enter(Bob, Hallway.BackDoor, true)')
	elif(i == 'input arrived Bob position GreatHall.BasementDoor'):
		action('Exit(Bob, GreatHall.BasementDoor, true)')
		action('Enter(Bob, Dungeon.Door, true)')
	elif(i == 'input arrived Bob position Dungeon.Door'):
		action('Exit(Bob, Dungeon.Door, true)')
		action('Enter(Bob, GreatHall.BasementDoor, true)')
	elif(i == 'input arrived Bob position GreatHall.LeftDoor'):
		action('Exit(Bob, GreatHall.LeftDoor, true)')
		action('Enter(Bob, CastleBedroom.Door, true)')
	elif(i == 'input arrived Bob position CastleBedroom.Door'):
		action('Exit(Bob, CastleBedroom.Door, true)')
		action('Enter(Bob, GreatHall.LeftDoor, true)')
	elif(i == 'input arrived Bob position GreatHall.RightDoor'):
		action('Exit(Bob, GreatHall.RightDoor, true)')
		action('Enter(Bob, DiningRoom.Door, true)')
	elif(i == 'input arrived Bob position DiningRoom.Door'):
		action('Exit(Bob, DiningRoom.Door, true)')
		action('Enter(Bob, GreatHall.RightDoor, true)')
	elif(i == 'input arrived Bob position DiningRoom.BackDoor'):
		action('Exit(Bob, DiningRoom.BackDoor, true)')
		action('Enter(Bob, Storage.Door, true)')
	elif(i == 'input arrived Bob position Storage.Door'):
		action('Exit(Bob, Storage.Door, true)')
		action('Enter(Bob, DiningRoom.BackDoor, true)')