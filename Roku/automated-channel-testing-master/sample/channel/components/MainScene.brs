' ********** Copyright 2019 Roku Corp.  All Rights Reserved. **********

'This is the main entry point to the channel scene.
'This function will be called by library when channel is ready to be shown.
sub show(args as Object)
    ' enable options icon in scene overhang
    m.top.theme = {
        global: {
            OverhangOptionsAvailable: true
            backgroundColor: "#000000"
        }
    }

    ' restore auth state
    HelperCheckAuthentication()

    ' show main grid
    m.grid = CreateObject("roSGNode", "GridView")
    m.grid.setFields({
        style: "standard"
        posterShape: "16x9"
    })
    content = CreateObject("roSGNode", "ContentNode")
    content.addfields({
        HandlerConfigGrid: {
            name: "ContentHandlerRoot"
        }
    })

    m.grid.ObserveField("rowItemSelected","OnGridItemSelected")

    m.grid.content = content

    'this will trigger job to show this screen
    m.top.ComponentController.callFunc("show", {
        view: m.grid
    })
end sub

sub OnGridItemSelected(event as Object)
    grid = event.GetRoSGNode()
    selectedIndex = event.getdata()
    rowContent = grid.content.getChild(selectedIndex[0])

    detailsScreen = ShowDetailsScreen(rowContent, selectedIndex[1])
    detailsScreen.ObserveField("wasClosed", "OnDetailsWasClosed")
end sub

sub OnDetailsWasClosed(event as Object)
    details = event.GetRoSGNode()
    m.grid.jumpToRowItem = [m.grid.rowItemFocused[0], details.itemFocused]
    
    ' remove details view from local m where it was cached 
    ' (see DetailsScreenLogic.brs) to release the component
    m.details = invalid
end sub

function onKeyEvent(key as String, press as Boolean) as Boolean
    isHandled = false
    
    if press then
        if (key = "options") then
            dialog = createObject("roSGNode", "Dialog")
            dialog.setFields({
                title: "Options Dialog"
                optionsDialog: true
            })
            
            if HelperIsUserAuthenticated()
                dialog.buttons = ["Log Out", "Exit"]
            else
                dialog.buttons = ["Log In", "Exit"]
            end if
            
            dialog.ObserveField("buttonSelected", "OnDialogButtonSelected")
            m.top.dialog = dialog
            
            isHandled = true
        end if
    end if
    
    return isHandled
end function

sub OnDialogButtonSelected()
    dialog = m.top.dialog
    buttonIndex = dialog.buttonSelected
    
    if buttonIndex = 0
        if HelperIsUserAuthenticated()
            ?"LOGOUT!!!"
            HelperDeAuthenticate("OnUserDeauthenticated")
        else
            ?"LOGIN!!!!"
            HelperAuthenticate()
        end if
    else if buttonIndex = 1
        m.top.exitChannel = true
    end if
    
    dialog.close = true
end sub

sub OnUserDeauthenticated()
    ' currently on details view? -> refresh buttons
    if m.details <> invalid
        OnDetailsCurrentItem()
    end if
end sub
