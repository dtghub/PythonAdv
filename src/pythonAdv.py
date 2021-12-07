import re



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
    commandState = {
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




class lowLevelCommand():

    # //
    # //"Low level" commands
    # //
    # //The "B" instruction is the inverse of the "C" Conditional test - if true then we skip the next instruction.
    # //B100 - is the item in the players inventory
    # //B101 - are any items in the location number defined in gameState.classicActiveNumber
    def B(parsedValue, i, gameState, commandState):
      clRooms = commandState["clRooms"]
      if (parsedValue < 100):
        if (commandState["clRooms"][clRooms.currentRoomIndex()][parsedValue] != 1):
          return i + 1
      else:
        if ((parsedValue == 100) and (clItems[gameState.classicItemID].location != 0)):
          return i + 1
        else:
          if ((parsedValue == 101) and (clItems.testForItemsAtLocation(gameState.classicActiveNumber))):
            return i + 1
        
      return i
    
    # //The "C" instruction is a Conditional test - if false then we skip the next instruction. - see related "B" and "S"
    # //In practice this means that a lot of the time the next instruction will be an 'X'
    # //At the moment this has only been implemented for the rooms table.
    # //classicParsedValue range of 1 to 99 is reserved for flags attached to the item objects
    # //C100 - is the item in the players inventory
    # //C101 - are any items in the location number defined in gameState.classicActiveNumber
    def C(classicParsedValue,i, gameState, commandState) {
      if (classicParsedValue < 100) {
        if (clRooms[clRooms.currentRoomIndex()][classicParsedValue] == 1) {
          return i + 1;
        }
      } else {
        if (classicParsedValue == 100 && clItems[gameState.classicItemID].location == 0) {
          return i + 1;
        }
        if (classicParsedValue == 101 && !clItems.testForItemsAtLocation(gameState.classicActiveNumber)) {
          return i + 1;
        }
      }
      return i;
    };
    //The "D" instruction adds a message number for Display to the classicMessageList string
    //The messages are retrieved and displayd after all instructions have been processed
    classicCommands.D = function (classicParsedValue,i) {
      gameState.classicMessageList += classicParsedValue.toString() + "~";
      return i;
    };
    //The "I" instruction changes the active "item" to which subsequent incstructions refer
    //See also the related "N" instruction
    classicCommands.I = function (classicParsedValue,i) {
      gameState.classicItemID = clItems.itemsArrayIndex(classicParsedValue);
      return i;
    };
    //The "L" instruction sets the location of the acitive item
    //location 0 is your own inventory
    //location -1 is the current location
    classicCommands.L = function (classicParsedValue,i) {
      if (classicParsedValue == -1) {
        classicParsedValue = clItems.currentRoomNumber();
      }
      clItems[gameState.classicItemID].location = classicParsedValue;
      if (clItems[gameState.classicItemID].ID == 0) {
        clItems.setCurrentRoomNumber(classicParsedValue);
      }
      return i;
    };
    //The "N" instruction changes the active "number" to which subsequent incstructions refer
    //See the related "I" instruction
    classicCommands.N = function (classicParsedValue,i) {
      if (classicParsedValue == -1) {
        gameState.classicActiveNumber = clItems.currentRoomNumber();
      } else {
        gameState.classicActiveNumber = classicParsedValue;
      }
      return i;
    };
    //The "P" instruction executes sPecial cases
    //Probably the goal is to develop the interpreter to the point where P is never needed
    //P1 adds the names of items located at the location matching gameState.classicActiveNumber to the display queue.
    classicCommands.P = function (classicParsedValue,i) {
      if (classicParsedValue == 1) {
        clItems.printListOfItemsAtLocation(gameState.classicActiveNumber);
      }
      return i;
    };
    //The "R" instruction unsets the flag used for the "C" and "B" conditional tests. ("S" Sets it)
    classicCommands.R = function (classicParsedValue,i) {
      clRooms[clRooms.currentRoomIndex()][classicParsedValue] = 0;
      return i;
    };
    //The "S" instruction Sets the flag used for the "C" and "B" conditional tests. ("R" unsets it)
    classicCommands.S = function (classicParsedValue,i) {
      clRooms[clRooms.currentRoomIndex()][classicParsedValue] = 1;
      return i;
    };
    //The "X" instruction looks up the instruction code from the snippets table and executes the instructions by calling classicProcessLowLevelInstruction recursively.
    classicCommands.X = function (classicParsedValue,i) {
      classicProcessLowLevelInstruction(clTabs.snippets[classicParsedValue]);
      return i;
    };




















#   //This splits the string of low level commands (in the form e.g. "D999I0L1C1D1000B1D1001N1X7") into an array, with one instruction in each element of the array
#   //The for loop then steps through the array, calling the function associated with each instruction e.g "D9999" will execute a function call within the for loop 'classicCommands.D(9999);'
#   //See function classicSetupCommands() for the details of the low level commands.
def processLowLevelInstruction(userInstruction):
    llc = lowLevelCommand()

    parsedValue = 0
    commandParts = []
    commandPartsArrayLength = 0

    # classicCommandParts = classicInstruction.match(/[A-Z][\-]?[0-9]+/g);
    commandParts = re.split('/[A-Z][\-]?[0-9]+/g',  userInstruction)

    commandPartsArrayLength = commandParts.length;

    for i in range(commandPartsArrayLength):
        clValue = commandParts[i]
        parsedValue = clValue[1:]

        commandToProcess = clValue[0] + "(" + parsedValue + ", " + str(i) + ", gameState, commandState)"
        i = getattr(llc, commandToProcess)

        i = classicCommands[clValue[0]](parsedValue,i)
        #The function is able to manipulate the 'i' index - (skip next command = i++)
    
    


















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
        # gameState.classicMessages = classicGetMessages;
        # });

        # because of the way the code flowed in the JS version, an output was built up and then the updateDescription() function was called. 
        updateDescription(gameState)




main()