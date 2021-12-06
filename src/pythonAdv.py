
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
    
    keepGoing = True

    while (keepGoing):

        userCommands = {}
        userInstruction = ""

        userCommands = parseEnteredCommand()
        userInstruction = processParsedCommand(userCommands)
        processHighLevelInstruction(userInstruction)



        # This was the JS callback to read the 'messages' table in from the ostgres server side database - for this project we'll dump the data into a JSON which gets read into memory (possibly the gameState object, but may be better as an object on its own?
        # classicGetMessages(function(classicGetMessages) {
        # classicGameStatus.classicMessages = classicGetMessages;
        # });

        # because of the way the code flowed in the JS version, an output was built up and then the updateDescription() function was called. 
        updateDescription(gameState)




main()