
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
    gameState, commandsState = initDataStructs()







main()