function ShowDetailsScreen(content, index)
    details = CreateObject("roSGNode", "DetailsView")
    
    ' save details to local m to be able to refer to it from other callbacks
    m.details = details
    
    details.jumpToItem = index
    details.content = content
    details.ObserveField("currentItem", "OnDetailsCurrentItem")
    details.ObserveField("buttonSelected", "OnDetailsButtonSelected")

    m.top.ComponentController.callFunc("show", {view: details})

    return details
end function

sub OnDetailsCurrentItem()
    ' arrange details view buttons according to user auth status
    buttonsList = []
    if HelperIsUserAuthenticated()
        buttonsList.Push({title:"Play", id:"play"})
    else
        buttonsList.Push({title: "Authenticate to watch", id: "authenticate"})
    end if
    
    m.details.buttons = Utils_ContentList2Node(buttonsList)
end sub

sub OnDetailsButtonSelected(event as Object)
    if m.details.currentItem <> invalid
        buttonIndex = event.GetData()
        button = m.details.buttons.GetChild(buttonIndex)
        
        if button.id = "play"
            ' play piece of content
            OpenVideoPlayer(m.details.content, m.details.itemFocused)
        else if button.id = "authenticate"
            ' cannot play content, initiate authentication flow
            HelperAuthenticate("OnDetailsIsAuthenticatedToPlay")
        end if
    end if
end sub

sub OnDetailsIsAuthenticatedToPlay(event as Object)
    isAuthenticated = event.GetData()
    if isAuthenticated
        OpenVideoPlayer(m.details.content, m.details.itemFocused)
    end if
end sub

