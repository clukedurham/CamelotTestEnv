def action(command):
	print('start ' + command)
	while(True):
		i = input()
		if(i == 'succeeded ' + command):
			return True
		elif(i == 'failed ' + command): # Error
			return False
		elif(i.startswith('error')): # Error
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
	action(f'EnableIcon("un_pocket", draw, {i})')
	action(f'EnableIcon("pocket", return, {i})')
	action(f'EnableIcon("pickup", hand, {i})')
	action(f'EnableIcon("putdown", cancel, {i})')

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
	elif(i == 'input un_pocket Apple'):
		action('Unpocket(Bob, Apple)')
	elif(i == 'input pocket Apple'):
		action('Pocket(Bob, Apple)')
	elif(i == 'input pickup Apple'):
		action('Pickup(Bob, Apple)')
	elif(i == 'input putdown Apple'):
		action('PutDown(Bob, Apple)')
	elif(i == 'input un_pocket Bag'):
		action('Unpocket(Bob, Bag)')
	elif(i == 'input pocket Bag'):
		action('Pocket(Bob, Bag)')
	elif(i == 'input pickup Bag'):
		action('Pickup(Bob, Bag)')
	elif(i == 'input putdown Bag'):
		action('PutDown(Bob, Bag)')
	elif(i == 'input un_pocket BlueBook'):
		action('Unpocket(Bob, BlueBook)')
	elif(i == 'input pocket BlueBook'):
		action('Pocket(Bob, BlueBook)')
	elif(i == 'input pickup BlueBook'):
		action('Pickup(Bob, BlueBook)')
	elif(i == 'input putdown BlueBook'):
		action('PutDown(Bob, BlueBook)')
	elif(i == 'input un_pocket BlueCloth'):
		action('Unpocket(Bob, BlueCloth)')
	elif(i == 'input pocket BlueCloth'):
		action('Pocket(Bob, BlueCloth)')
	elif(i == 'input pickup BlueCloth'):
		action('Pickup(Bob, BlueCloth)')
	elif(i == 'input putdown BlueCloth'):
		action('PutDown(Bob, BlueCloth)')
	elif(i == 'input un_pocket BlueKey'):
		action('Unpocket(Bob, BlueKey)')
	elif(i == 'input pocket BlueKey'):
		action('Pocket(Bob, BlueKey)')
	elif(i == 'input pickup BlueKey'):
		action('Pickup(Bob, BlueKey)')
	elif(i == 'input putdown BlueKey'):
		action('PutDown(Bob, BlueKey)')
	elif(i == 'input un_pocket BluePotion'):
		action('Unpocket(Bob, BluePotion)')
	elif(i == 'input pocket BluePotion'):
		action('Pocket(Bob, BluePotion)')
	elif(i == 'input pickup BluePotion'):
		action('Pickup(Bob, BluePotion)')
	elif(i == 'input putdown BluePotion'):
		action('PutDown(Bob, BluePotion)')
	elif(i == 'input un_pocket Bottle'):
		action('Unpocket(Bob, Bottle)')
	elif(i == 'input pocket Bottle'):
		action('Pocket(Bob, Bottle)')
	elif(i == 'input pickup Bottle'):
		action('Pickup(Bob, Bottle)')
	elif(i == 'input putdown Bottle'):
		action('PutDown(Bob, Bottle)')
	elif(i == 'input un_pocket Bread'):
		action('Unpocket(Bob, Bread)')
	elif(i == 'input pocket Bread'):
		action('Pocket(Bob, Bread)')
	elif(i == 'input pickup Bread'):
		action('Pickup(Bob, Bread)')
	elif(i == 'input putdown Bread'):
		action('PutDown(Bob, Bread)')
	elif(i == 'input un_pocket ChickenLeg'):
		action('Unpocket(Bob, ChickenLeg)')
	elif(i == 'input pocket ChickenLeg'):
		action('Pocket(Bob, ChickenLeg)')
	elif(i == 'input pickup ChickenLeg'):
		action('Pickup(Bob, ChickenLeg)')
	elif(i == 'input putdown ChickenLeg'):
		action('PutDown(Bob, ChickenLeg)')
	elif(i == 'input un_pocket Coin'):
		action('Unpocket(Bob, Coin)')
	elif(i == 'input pocket Coin'):
		action('Pocket(Bob, Coin)')
	elif(i == 'input pickup Coin'):
		action('Pickup(Bob, Coin)')
	elif(i == 'input putdown Coin'):
		action('PutDown(Bob, Coin)')
	elif(i == 'input un_pocket Compass'):
		action('Unpocket(Bob, Compass)')
	elif(i == 'input pocket Compass'):
		action('Pocket(Bob, Compass)')
	elif(i == 'input pickup Compass'):
		action('Pickup(Bob, Compass)')
	elif(i == 'input putdown Compass'):
		action('PutDown(Bob, Compass)')
	elif(i == 'input un_pocket Cup'):
		action('Unpocket(Bob, Cup)')
	elif(i == 'input pocket Cup'):
		action('Pocket(Bob, Cup)')
	elif(i == 'input pickup Cup'):
		action('Pickup(Bob, Cup)')
	elif(i == 'input putdown Cup'):
		action('PutDown(Bob, Cup)')
	elif(i == 'input un_pocket EvilBook'):
		action('Unpocket(Bob, EvilBook)')
	elif(i == 'input pocket EvilBook'):
		action('Pocket(Bob, EvilBook)')
	elif(i == 'input pickup EvilBook'):
		action('Pickup(Bob, EvilBook)')
	elif(i == 'input putdown EvilBook'):
		action('PutDown(Bob, EvilBook)')
	elif(i == 'input un_pocket GoldCup'):
		action('Unpocket(Bob, GoldCup)')
	elif(i == 'input pocket GoldCup'):
		action('Pocket(Bob, GoldCup)')
	elif(i == 'input pickup GoldCup'):
		action('Pickup(Bob, GoldCup)')
	elif(i == 'input putdown GoldCup'):
		action('PutDown(Bob, GoldCup)')
	elif(i == 'input un_pocket GreenBook'):
		action('Unpocket(Bob, GreenBook)')
	elif(i == 'input pocket GreenBook'):
		action('Pocket(Bob, GreenBook)')
	elif(i == 'input pickup GreenBook'):
		action('Pickup(Bob, GreenBook)')
	elif(i == 'input putdown GreenBook'):
		action('PutDown(Bob, GreenBook)')
	elif(i == 'input un_pocket GreenKey'):
		action('Unpocket(Bob, GreenKey)')
	elif(i == 'input pocket GreenKey'):
		action('Pocket(Bob, GreenKey)')
	elif(i == 'input pickup GreenKey'):
		action('Pickup(Bob, GreenKey)')
	elif(i == 'input putdown GreenKey'):
		action('PutDown(Bob, GreenKey)')
	elif(i == 'input un_pocket GreenPotion'):
		action('Unpocket(Bob, GreenPotion)')
	elif(i == 'input pocket GreenPotion'):
		action('Pocket(Bob, GreenPotion)')
	elif(i == 'input pickup GreenPotion'):
		action('Pickup(Bob, GreenPotion)')
	elif(i == 'input putdown GreenPotion'):
		action('PutDown(Bob, GreenPotion)')
	elif(i == 'input un_pocket Hammer'):
		action('Unpocket(Bob, Hammer)')
	elif(i == 'input pocket Hammer'):
		action('Pocket(Bob, Hammer)')
	elif(i == 'input pickup Hammer'):
		action('Pickup(Bob, Hammer)')
	elif(i == 'input putdown Hammer'):
		action('PutDown(Bob, Hammer)')
	elif(i == 'input un_pocket Helmet'):
		action('Unpocket(Bob, Helmet)')
	elif(i == 'input pocket Helmet'):
		action('Pocket(Bob, Helmet)')
	elif(i == 'input pickup Helmet'):
		action('Pickup(Bob, Helmet)')
	elif(i == 'input putdown Helmet'):
		action('PutDown(Bob, Helmet)')
	elif(i == 'input un_pocket InkandQuill'):
		action('Unpocket(Bob, InkandQuill)')
	elif(i == 'input pocket InkandQuill'):
		action('Pocket(Bob, InkandQuill)')
	elif(i == 'input pickup InkandQuill'):
		action('Pickup(Bob, InkandQuill)')
	elif(i == 'input putdown InkandQuill'):
		action('PutDown(Bob, InkandQuill)')
	elif(i == 'input un_pocket JewelKey'):
		action('Unpocket(Bob, JewelKey)')
	elif(i == 'input pocket JewelKey'):
		action('Pocket(Bob, JewelKey)')
	elif(i == 'input pickup JewelKey'):
		action('Pickup(Bob, JewelKey)')
	elif(i == 'input putdown JewelKey'):
		action('PutDown(Bob, JewelKey)')
	elif(i == 'input un_pocket LitTorch'):
		action('Unpocket(Bob, LitTorch)')
	elif(i == 'input pocket LitTorch'):
		action('Pocket(Bob, LitTorch)')
	elif(i == 'input pickup LitTorch'):
		action('Pickup(Bob, LitTorch)')
	elif(i == 'input putdown LitTorch'):
		action('PutDown(Bob, LitTorch)')
	elif(i == 'input un_pocket Lock'):
		action('Unpocket(Bob, Lock)')
	elif(i == 'input pocket Lock'):
		action('Pocket(Bob, Lock)')
	elif(i == 'input pickup Lock'):
		action('Pickup(Bob, Lock)')
	elif(i == 'input putdown Lock'):
		action('PutDown(Bob, Lock)')
	elif(i == 'input un_pocket MagnifyingGlass'):
		action('Unpocket(Bob, MagnifyingGlass)')
	elif(i == 'input pocket MagnifyingGlass'):
		action('Pocket(Bob, MagnifyingGlass)')
	elif(i == 'input pickup MagnifyingGlass'):
		action('Pickup(Bob, MagnifyingGlass)')
	elif(i == 'input putdown MagnifyingGlass'):
		action('PutDown(Bob, MagnifyingGlass)')
	elif(i == 'input un_pocket OpenScroll'):
		action('Unpocket(Bob, OpenScroll)')
	elif(i == 'input pocket OpenScroll'):
		action('Pocket(Bob, OpenScroll)')
	elif(i == 'input pickup OpenScroll'):
		action('Pickup(Bob, OpenScroll)')
	elif(i == 'input putdown OpenScroll'):
		action('PutDown(Bob, OpenScroll)')
	elif(i == 'input un_pocket PurpleBook'):
		action('Unpocket(Bob, PurpleBook)')
	elif(i == 'input pocket PurpleBook'):
		action('Pocket(Bob, PurpleBook)')
	elif(i == 'input pickup PurpleBook'):
		action('Pickup(Bob, PurpleBook)')
	elif(i == 'input putdown PurpleBook'):
		action('PutDown(Bob, PurpleBook)')
	elif(i == 'input un_pocket PurpleCloth'):
		action('Unpocket(Bob, PurpleCloth)')
	elif(i == 'input pocket PurpleCloth'):
		action('Pocket(Bob, PurpleCloth)')
	elif(i == 'input pickup PurpleCloth'):
		action('Pickup(Bob, PurpleCloth)')
	elif(i == 'input putdown PurpleCloth'):
		action('PutDown(Bob, PurpleCloth)')
	elif(i == 'input un_pocket PurpleKey'):
		action('Unpocket(Bob, PurpleKey)')
	elif(i == 'input pocket PurpleKey'):
		action('Pocket(Bob, PurpleKey)')
	elif(i == 'input pickup PurpleKey'):
		action('Pickup(Bob, PurpleKey)')
	elif(i == 'input putdown PurpleKey'):
		action('PutDown(Bob, PurpleKey)')
	elif(i == 'input un_pocket PurplePotion'):
		action('Unpocket(Bob, PurplePotion)')
	elif(i == 'input pocket PurplePotion'):
		action('Pocket(Bob, PurplePotion)')
	elif(i == 'input pickup PurplePotion'):
		action('Pickup(Bob, PurplePotion)')
	elif(i == 'input putdown PurplePotion'):
		action('PutDown(Bob, PurplePotion)')
	elif(i == 'input un_pocket Rags'):
		action('Unpocket(Bob, Rags)')
	elif(i == 'input pocket Rags'):
		action('Pocket(Bob, Rags)')
	elif(i == 'input pickup Rags'):
		action('Pickup(Bob, Rags)')
	elif(i == 'input putdown Rags'):
		action('PutDown(Bob, Rags)')
	elif(i == 'input un_pocket RedBook'):
		action('Unpocket(Bob, RedBook)')
	elif(i == 'input pocket RedBook'):
		action('Pocket(Bob, RedBook)')
	elif(i == 'input pickup RedBook'):
		action('Pickup(Bob, RedBook)')
	elif(i == 'input putdown RedBook'):
		action('PutDown(Bob, RedBook)')
	elif(i == 'input un_pocket RedCloth'):
		action('Unpocket(Bob, RedCloth)')
	elif(i == 'input pocket RedCloth'):
		action('Pocket(Bob, RedCloth)')
	elif(i == 'input pickup RedCloth'):
		action('Pickup(Bob, RedCloth)')
	elif(i == 'input putdown RedCloth'):
		action('PutDown(Bob, RedCloth)')
	elif(i == 'input un_pocket RedKey'):
		action('Unpocket(Bob, RedKey)')
	elif(i == 'input pocket RedKey'):
		action('Pocket(Bob, RedKey)')
	elif(i == 'input pickup RedKey'):
		action('Pickup(Bob, RedKey)')
	elif(i == 'input putdown RedKey'):
		action('PutDown(Bob, RedKey)')
	elif(i == 'input un_pocket RedPotion'):
		action('Unpocket(Bob, RedPotion)')
	elif(i == 'input pocket RedPotion'):
		action('Pocket(Bob, RedPotion)')
	elif(i == 'input pickup RedPotion'):
		action('Pickup(Bob, RedPotion)')
	elif(i == 'input putdown RedPotion'):
		action('PutDown(Bob, RedPotion)')
	elif(i == 'input un_pocket Scroll'):
		action('Unpocket(Bob, Scroll)')
	elif(i == 'input pocket Scroll'):
		action('Pocket(Bob, Scroll)')
	elif(i == 'input pickup Scroll'):
		action('Pickup(Bob, Scroll)')
	elif(i == 'input putdown Scroll'):
		action('PutDown(Bob, Scroll)')
	elif(i == 'input un_pocket Skull'):
		action('Unpocket(Bob, Skull)')
	elif(i == 'input pocket Skull'):
		action('Pocket(Bob, Skull)')
	elif(i == 'input pickup Skull'):
		action('Pickup(Bob, Skull)')
	elif(i == 'input putdown Skull'):
		action('PutDown(Bob, Skull)')
	elif(i == 'input un_pocket SpellBook'):
		action('Unpocket(Bob, SpellBook)')
	elif(i == 'input pocket SpellBook'):
		action('Pocket(Bob, SpellBook)')
	elif(i == 'input pickup SpellBook'):
		action('Pickup(Bob, SpellBook)')
	elif(i == 'input putdown SpellBook'):
		action('PutDown(Bob, SpellBook)')
	elif(i == 'input un_pocket Sword'):
		action('Unpocket(Bob, Sword)')
	elif(i == 'input pocket Sword'):
		action('Pocket(Bob, Sword)')
	elif(i == 'input pickup Sword'):
		action('Pickup(Bob, Sword)')
	elif(i == 'input putdown Sword'):
		action('PutDown(Bob, Sword)')
	elif(i == 'input un_pocket Torch'):
		action('Unpocket(Bob, Torch)')
	elif(i == 'input pocket Torch'):
		action('Pocket(Bob, Torch)')
	elif(i == 'input pickup Torch'):
		action('Pickup(Bob, Torch)')
	elif(i == 'input putdown Torch'):
		action('PutDown(Bob, Torch)')