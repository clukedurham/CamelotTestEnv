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
action('SetPosition(Bob, BobsHouse.Door)')
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
	elif(i == 'input arrived Bob position Bridge.NorthEnd'): # enter Ruins
		action('Exit(Bob, Bridge.NorthEnd, true)')
		action('Enter(Bob, Ruins.Exit, true)')
	elif(i == 'input arrived Bob position Ruins.Exit'): # exit Ruins
		action('Exit(Bob, Ruins.Exit, true)')
		action('Enter(Bob, Bridge.NorthEnd, true)')
	elif(i == 'input arrived Bob position City.SouthEnd'): # enter ForestPath
		action('Exit(Bob, City.SouthEnd, true)')
		action('Enter(Bob, ForestPath.EastEnd, true)')
	elif(i == 'input arrived Bob position ForestPath.EastEnd'): # exit ForestPath
		action('Exit(Bob, ForestPath.EastEnd, true)')
		action('Enter(Bob, City.SouthEnd, true)')
	elif(i == 'input Key Pause'):
		action('ShowMenu()')
	elif(i == 'input Selected Quit'):
		action('Quit()')
	elif(i == 'input Close Narration'):
		action('HideNarration()')