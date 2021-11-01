# Send a command to Camelot.
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

# Create Bob's House
action('CreatePlace(BobsHouse, Cottage)')
action('CreateCharacter(Bob, B)')
action('CreateItem(Sword, Sword)')
action('SetPosition(Sword, BobsHouse.Table)')
action('EnableIcon("Pick_Up", draw, Sword, "Pick up Sword", true)')
action('SetClothing(Bob, Peasant)')
# action('SetPosition(Bob, BobsHouse.Door)')
action('EnableIcon("Open_Door", exit, BobsHouse.Door, "Go to City", true)')
action('ShowMenu()')

# Create City
action('CreatePlace(City, City)')
action('EnableIcon("Open_Door", exit, City.GreenHouseDoor, "Go to Bob\'s house", true)')
# Create Blacksmith
action('EnableIcon("Open_Door", exit, City.BrownHouseDoor, "Go to Black Smith", true)')
action('CreatePlace(Blacksmith, Blacksmith)')
action('EnableIcon("Open_Door", exit, Blacksmith.Door, "Go to City", true)')
# Create Tavern
action('EnableIcon("Open_Door", exit, City.RedHouseDoor, "Go to Tavern", true)')
action('CreatePlace(Tavern, Tavern)')
action('EnableIcon("Open_Door", exit, Tavern.Door, "Go to City", true)')
# Create Alchemy Shop
action('EnableIcon("Open_Door", exit, City.BlueHouseDoor, "Go to Alchemy Shop", true)')
action('CreatePlace(AlchemyShop, AlchemyShop)')
action('EnableIcon("Open_Door", exit, AlchemyShop.Door, "Go to City", true)')

# Create Bridge
action('CreatePlace(Bridge, Bridge)')
# Create Camp
action('CreatePlace(Camp, Camp)')
# Create Ruins
action('CreatePlace(Ruins, Ruins)')
# Create Forest Path
action('CreatePlace(ForestPath, ForestPath)')
# Create Farm
action('CreatePlace(Farm, Farm)')
# Create CityPort
action('CreatePlace(CityPort, Port)')
action('EnableIcon("Open_Door", exit, CityPort.BigShip, "Go to Castle Port", true)')
# Create SpookyPath
action('CreatePlace(SpookyPath, SpookyPath)')
# Create CastlePort
action('CreatePlace(CastlePort, Port)')
action('EnableIcon("Open_Door", exit, CastlePort.BigShip, "Go to City Port", true)')
# Create Crossroads
action('CreatePlace(Crossroads, CastleCrossroads)')
action('EnableIcon("Open_Door", exit, Crossroads.Gate, "Go to Hallway", true)')
#Create Courtyard
action('CreatePlace(Courtyard, Courtyard)')
action('EnableIcon("Open_Door", exit, Courtyard.Gate, "Go to Hallway", true)')

# Create Hallway
action('CreatePlace(Hallway, Hallway)')
action('EnableIcon("Open_Door", exit, Hallway.Door, "Go to Crossroads", true)')
action('EnableIcon("Open_Door", exit, Hallway.BackDoor, "Go to Great Hall", true)')
# Create GreatHall
action('CreatePlace(GreatHall, GreatHall)')
action('EnableIcon("Open_Door", exit, GreatHall.Gate, "Go to Hallway", true)')
action('EnableIcon("Open_Door", exit, GreatHall.BasementDoor, "Go to Dungeon", true)')
action('EnableIcon("Open_Door", exit, GreatHall.LeftDoor, "Go to Bedroom", true)')
action('EnableIcon("Open_Door", exit, GreatHall.RightDoor, "Go to Dining Room", true)')
# Create Library
action('CreatePlace(Library, Library)')
action('EnableIcon("Open_Door", exit, Library.Door, "Go to Hallway", true)')
# Create Dungeon
action('CreatePlace(Dungeon, Dungeon)')
action('EnableIcon("Open_Door", exit, Dungeon.Door, "Go to Great Hall", true)')
# Create Bedroom
action('CreatePlace(Bedroom, CastleBedroom)')
action('EnableIcon("Open_Door", exit, Bedroom.Door, "Go to Great Hall", true)')
# Create Dining Room
action('CreatePlace(DiningRoom, DiningRoom)')
action('EnableIcon("Open_Door", exit, DiningRoom.Door, "Go to Great Hall", true)')
action('EnableIcon("Open_Door", exit, DiningRoom.BackDoor, "Go to Storage", true)')
# Create Storage
action('CreatePlace(Storage, Storage)')
action('EnableIcon("Open_Door", exit, Storage.Door, "Go to Dining Room", true)')

# Place Bob
action('SetPosition(Bob, Crossroads.WestEnd)')

# Respond to input.
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
	elif(i == 'input Pick_Up Sword'):
		action('Draw(Bob, Sword)')
		action('AddToList(Sword,"This is a sword!")')
		# TODO add sword to inventory
	elif(i == 'input Open_Door BobsHouse.Door'): # enter bob's house
		action('Exit(Bob, BobsHouse.Door, true)')
		action('Enter(Bob, City.GreenHouseDoor, true)')
	elif(i == 'input Open_Door City.GreenHouseDoor'): # exit bob's house
		action('Exit(Bob, City.GreenHouseDoor, true)')
		action('Enter(Bob, BobsHouse.Door, true)')
	elif(i == 'input Open_Door City.BrownHouseDoor'): # enter Blacksmith
		action('Exit(Bob, City.BrownHouseDoor, true)')
		action('Enter(Bob, Blacksmith.Door, true)')
	elif(i == 'input Open_Door Blacksmith.Door'): # exit Blacksmith
		action('Exit(Bob, Blacksmith.Door, true)')
		action('Enter(Bob, City.BrownHouseDoor, true)')
	elif(i == 'input Open_Door City.RedHouseDoor'): # enter Tavern
		action('Exit(Bob, City.RedHouseDoor, true)')
		action('Enter(Bob, Tavern.Door, true)')
	elif(i == 'input Open_Door Tavern.Door'): # exit Tavern
		action('Exit(Bob, Tavern.Door, true)')
		action('Enter(Bob, City.RedHouseDoor, true)')
	elif(i == 'input Open_Door City.BlueHouseDoor'): # enter AlchemyShop
		action('Exit(Bob, City.BlueHouseDoor, true)')
		action('Enter(Bob, AlchemyShop.Door, true)')
	elif(i == 'input Open_Door AlchemyShop.Door'): # exit AlchemyShop
		action('Exit(Bob, AlchemyShop.Door, true)')
		action('Enter(Bob, City.BlueHouseDoor, true)')
	elif(i == 'input arrived Bob position City.EastEnd'): # enter Bridge
		action('Exit(Bob, City.EastEnd, true)')
		action('Enter(Bob, Bridge.WestEnd, true)')
	elif(i == 'input arrived Bob position Bridge.WestEnd'): # exit Bridge
		action('Exit(Bob, Bridge.WestEnd, true)')
		action('Enter(Bob, City.EastEnd, true)')
	elif(i == 'input arrived Bob position Bridge.SouthEnd'): # enter Camp
		action('Exit(Bob, Bridge.SouthEnd, true)')
		action('Enter(Bob, Camp.Exit, true)')
	elif(i == 'input arrived Bob position Camp.Exit'): # exit Camp
		action('Exit(Bob, Camp.Exit, true)')
		action('Enter(Bob, Bridge.SouthEnd, true)')
	elif(i == 'input arrived Bob position Bridge.NorthEnd'): # enter Spooky Path
		action('Exit(Bob, Bridge.NorthEnd, true)')
		action('Enter(Bob, SpookyPath.EastEnd, true)')
	elif(i == 'input arrived Bob position SpookyPath.EastEnd'): # exit Spooky Path
		action('Exit(Bob, SpookyPath.EastEnd, true)')
		action('Enter(Bob, Bridge.NorthEnd, true)')
	elif(i == 'input arrived Bob position SpookyPath.WestEnd'): # enter Ruins
		action('Exit(Bob, SpookyPath.WestEnd, true)')
		action('Enter(Bob, Ruins.Exit, true)')
	elif(i == 'input arrived Bob position Ruins.Exit'): # exit Ruins
		action('Exit(Bob, Ruins.Exit, true)')
		action('Enter(Bob, SpookyPath.WestEnd, true)')
	elif(i == 'input arrived Bob position City.NorthEnd'): # enter ForestPath
		action('Exit(Bob, City.NorthEnd, true)')
		action('Enter(Bob, ForestPath.EastEnd, true)')
	elif(i == 'input arrived Bob position ForestPath.EastEnd'): # exit ForestPath
		action('Exit(Bob, ForestPath.EastEnd, true)')
		action('Enter(Bob, City.NorthEnd, true)')
	elif(i == 'input arrived Bob position ForestPath.WestEnd'): # enter Farm
		action('Exit(Bob, ForestPath.WestEnd, true)')
		action('Enter(Bob, Farm.Exit, true)')
	elif(i == 'input arrived Bob position Farm.Exit'): # exit Farm
		action('Exit(Bob, ForestPath.Exit, true)')
		action('Enter(Bob, ForestPath.WestEnd, true)')
	elif(i == 'input arrived Bob position City.WestEnd'): # enter CityPort
		action('Exit(Bob, City.WestEnd, true)')
		action('Enter(Bob, CityPort.Exit, true)')
	elif(i == 'input arrived Bob position CityPort.Exit'): # exit CityPort
		action('Exit(Bob, CityPort.Exit, true)')
		action('Enter(Bob, City.WestEnd, true)')
	elif(i == 'input Open_Door CityPort.BigShip'): # enter CastlePort
		action('FadeOut()')
		action('SetPosition(Bob, CastlePort.BigShip)')
		action('FadeIn()')
	elif(i == 'input Open_Door CastlePort.BigShip'): # exit CastlePort
		action('FadeOut()')
		action('SetPosition(Bob, CityPort.BigShip)')
		action('FadeIn()')
	elif(i == 'input arrived Bob position CastlePort.Exit'): # enter Crossroads
		action('Exit(Bob, CastlePort.Exit, true)')
		action('Enter(Bob, Crossroads.WestEnd, true)')
	elif(i == 'input arrived Bob position Crossroads.WestEnd'): # exit Crossroads
		action('Exit(Bob, Crossroads.WestEnd, true)')
		action('Enter(Bob, CastlePort.Exit, true)')
	elif(i == 'input Open_Door Crossroads.Gate'): # enter Courtyard
		action('Exit(Bob, Crossroads.Gate, true)')
		action('Enter(Bob, Courtyard.Exit, true)')
	elif(i == 'input arrived Bob position Courtyard.Exit'): # exit Courtyard
		action('Exit(Bob, Courtyard.Exit, true)')
		action('Enter(Bob, Crossroads.Gate, true)')
	elif(i == 'input Open_Door Courtyard.Gate'): # enter Hallway
		action('Exit(Bob, Courtyard.Gate, true)')
		action('Enter(Bob, Hallway.Door, true)')
	elif(i == 'input Open_Door Hallway.Door'): # exit Hallway
		action('Exit(Bob, Hallway.Door, true)')
		action('Enter(Bob, Courtyard.Gate, true)')
	elif(i == 'input Open_Door Hallway.BackDoor'): # enter GreatHall
		action('Exit(Bob, Hallway.BackDoor, true)')
		action('Enter(Bob, GreatHall.Gate, true)')
	elif(i == 'input Open_Door GreatHall.Gate'): # exit GreatHall
		action('Exit(Bob, GreatHall.Gate, true)')
		action('Enter(Bob, Hallway.BackDoor, true)')
	elif(i == 'input arrived Bob position Hallway.Stairs'): # enter Library
		action('Exit(Bob, Hallway.Stairs, true)')
		action('Enter(Bob, Library.Door, true)')
	elif(i == 'input Open_Door Library.Door'): # exit Library
		action('Exit(Bob, Library.Door, true)')
		action('Enter(Bob, Hallway.Stairs, true)')
	elif(i == 'input Open_Door GreatHall.BasementDoor'): # enter Dungeon
		action('Exit(Bob, GreatHall.BasementDoor, true)')
		action('Enter(Bob, Dungeon.Door, true)')
	elif(i == 'input Open_Door Dungeon.Door'): # exit Dungeon
		action('Exit(Bob, Dungeon.Door, true)')
		action('Enter(Bob, GreatHall.BasementDoor, true)')
	elif(i == 'input Open_Door GreatHall.LeftDoor'): # enter Bedroom
		action('Exit(Bob, GreatHall.LeftDoor, true)')
		action('Enter(Bob, Bedroom.Door, true)')
	elif(i == 'input Open_Door Bedroom.Door'): # exit Bedroom
		action('Exit(Bob, Bedroom.Door, true)')
		action('Enter(Bob, GreatHall.LeftDoor, true)')
	elif(i == 'input Open_Door GreatHall.RightDoor'): # enter Dining Room
		action('Exit(Bob, GreatHall.RightDoor, true)')
		action('Enter(Bob, DiningRoom.Door, true)')
	elif(i == 'input Open_Door DiningRoom.Door'): # exit Dining Room
		action('Exit(Bob, DiningRoom.Door, true)')
		action('Enter(Bob, GreatHall.RightDoor, true)')
	elif(i == 'input Open_Door DiningRoom.BackDoor'): # enter Dining Room
		action('Exit(Bob, DiningRoom.BackDoor, true)')
		action('Enter(Bob, Storage.Door, true)')
	elif(i == 'input Open_Door Storage.Door'): # exit Dining Room
		action('Exit(Bob, Storage.Door, true)')
		action('Enter(Bob, DiningRoom.BackDoor, true)')
	elif(i == 'input Key Pause'):
		action('ShowMenu()')
	elif(i == 'input Selected Quit'):
		action('Quit()')
	elif(i == 'input Close Narration'):
		action('HideNarration()')