' Helper function, checks user authentication state (not content-specific)
' @param onAuthCheckedCallback [String] name of the callback to process auth state
sub HelperCheckAuthentication(onAuthCheckedCallback = "" as String)
    ' use EntitlementView as headless component (no UI) to check auth
    ent = CreateObject("roSGNode", "EntitlementView")
    
    ' assign callback if non-empty
    if onAuthCheckedCallback.Len() > 0
        ent.ObserveField("isAuthenticated", onAuthCheckedCallback)
    end if
    
    ' set dummy config containing entitlement handler config
    content = CreateObject("roSGNode", "ContentNode")
    content.AddFields({
        handlerConfigEntitlement: {
            name : "HandlerEntitlement"
        }
    })
    ent.content = content
    
    ' initiate auth state checking
    ent.silentCheckAuthentication = true
end sub

' Helper function, initiates user authentication flow (not content-specific)
' @param onAuthenticatedCallback [String] name of the callback to process auth result
sub HelperAuthenticate(onAuthenticatedCallback = "" as String)
    ' use EntitlementView in headed (UI) mode
    ent = CreateObject("roSGNode","EntitlementView")
    
    ' assign callback if non-empty
    ent.ObserveField("isAuthenticated", onAuthenticatedCallback)
    
    ' set dummy config containing entitlement handler config
    content = CreateObject("roSGNode", "ContentNode")
    content.AddFields({
        handlerConfigEntitlement: {
            name : "HandlerEntitlement"
        }
    })
    ent.content = content

    ' initiate auth flow
    m.top.ComponentController.callFunc("show", {view: ent})
end sub

sub HelperDeAuthenticate(onDeAuthenticatedCallback = "" as String)
    ' use EntitlementView as headless component (no UI) to de-authenticate
    ent = CreateObject("roSGNode", "EntitlementView")
    
    ' assign callback if non-empty
    if onDeAuthenticatedCallback.Len() > 0
        ent.ObserveField("isAuthenticated", onDeAuthenticatedCallback)
    end if
    
    ' set dummy config containing entitlement handler config
    content = CreateObject("roSGNode", "ContentNode")
    content.AddFields({
        handlerConfigEntitlement: {
            name : "HandlerEntitlement"
        }
    })
    ent.content = content
    
    ' initiate auth state checking
    ent.silentDeAuthenticate = true
end sub

' Helper function, checks if user is authenticated
' @return [Boolean] true if authenticated, false otherwise
function HelperIsUserAuthenticated() as Boolean
    token = m.global.token
    return token <> invalid and token.Len() > 0
end function
