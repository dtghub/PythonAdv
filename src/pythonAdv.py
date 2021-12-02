
def initGameState():
    gameState = {
        "gameStatus": "",
        "commandInput": "",

        "importedTables": {},

        "turnCommand": "",

        "messageList": "",
        "messages": "",
        "activeNumber": 0,
        "itemID": -1,

    }

    return(gameState)


def initCommandState():
    CommandState = {
        "clTabs": {},
        "clItems": {},
        "clRooms": {},
        "clTemplates": {},
        "clCommands": {}
    }

    return(CommandState)




def initDataStructs():
    gameState = initGameState()
    commandsState = initCommandState()
    return(gameState, commandsState)




def main():
    # initialise the state variables
    gameState, commandsState = initDataStructs()
    







main()