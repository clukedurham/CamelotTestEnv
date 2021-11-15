import Util

def test_connect():
    # correct usage

    assert Util.connect('Cottage','Door','City','GreenHouseDoor') == '\n\telif(i == \'input arrived Bob position Cottage.Door\'):\n\t\taction(\'Exit(Bob, Cottage.Door, true)\')\n\t\taction(\'Enter(Bob, City.GreenHouseDoor, true)\')\n\telif(i == \'input arrived Bob position City.GreenHouseDoor\'):\n\t\taction(\'Exit(Bob, City.GreenHouseDoor, true)\')\n\t\taction(\'Enter(Bob, Cottage.Door, true)\')'
    assert Util.connect('City','BrownHouseDoor','Blacksmith','Door') == '\n\telif(i == \'input arrived Bob position City.BrownHouseDoor\'):\n\t\taction(\'Exit(Bob, City.BrownHouseDoor, true)\')\n\t\taction(\'Enter(Bob, Blacksmith.Door, true)\')\n\telif(i == \'input arrived Bob position Blacksmith.Door\'):\n\t\taction(\'Exit(Bob, Blacksmith.Door, true)\')\n\t\taction(\'Enter(Bob, City.BrownHouseDoor, true)\')'
    assert Util.connect('City','RedHouseDoor','Tavern','Door') == '\n\telif(i == \'input arrived Bob position City.RedHouseDoor\'):\n\t\taction(\'Exit(Bob, City.RedHouseDoor, true)\')\n\t\taction(\'Enter(Bob, Tavern.Door, true)\')\n\telif(i == \'input arrived Bob position Tavern.Door\'):\n\t\taction(\'Exit(Bob, Tavern.Door, true)\')\n\t\taction(\'Enter(Bob, City.RedHouseDoor, true)\')'
   
    # incorrect usage, make sure errors are handled
    
    # City (place1) is misspelled 
    assert Util.connect('city', 'RedHouseDoor', 'Tavern', 'Door') == "Invalid Input", "Should be Invalid Input"
    # Tavern (place2) is misspelled
    assert Util.connect('city', 'RedHouseDoor', 'TiverN', 'Door') == "Invalid Input", "Should be Invalid Input"

def test_itemInput():
    # correct usage

    assert Util.itemInput("Sword") == '\n\telif(i == \'input un_pocket Sword\'):\n\t\taction(\'Unpocket(Bob, Sword)\')\n\telif(i == \'input pocket Sword\'):\n\t\taction(\'Pocket(Bob, Sword)\')\n\telif(i == \'input pickup Sword\'):\n\t\taction(\'Pickup(Bob, Sword)\')\n\telif(i == \'input putdown Sword\'):\n\t\taction(\'PutDown(Bob, Sword)\')'
    assert Util.itemInput("LitTorch") == '\n\telif(i == \'input un_pocket LitTorch\'):\n\t\taction(\'Unpocket(Bob, LitTorch)\')\n\telif(i == \'input pocket LitTorch\'):\n\t\taction(\'Pocket(Bob, LitTorch)\')\n\telif(i == \'input pickup LitTorch\'):\n\t\taction(\'Pickup(Bob, LitTorch)\')\n\telif(i == \'input putdown LitTorch\'):\n\t\taction(\'PutDown(Bob, LitTorch)\')'
    assert Util.itemInput("RedKey") == '\n\telif(i == \'input un_pocket RedKey\'):\n\t\taction(\'Unpocket(Bob, RedKey)\')\n\telif(i == \'input pocket RedKey\'):\n\t\taction(\'Pocket(Bob, RedKey)\')\n\telif(i == \'input pickup RedKey\'):\n\t\taction(\'Pickup(Bob, RedKey)\')\n\telif(i == \'input putdown RedKey\'):\n\t\taction(\'PutDown(Bob, RedKey)\')'
    
    # incorrect usage, make sure errors are handled

    assert Util.itemInput("sword") == "Invalid Input", "Should be Invalid Input"

test_connect()
test_itemInput()
print("All tests passed.")