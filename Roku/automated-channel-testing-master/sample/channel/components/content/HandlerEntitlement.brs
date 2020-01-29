sub ConfigureEntitlements(config as Object)
    config.mode = "UserPass"
end sub

function CheckAuthentication() as Boolean
    ?"CheckAuthentication()"
    
    ' look for token cached in global node
    token = m.global.token
    if token = invalid
        ' look for token in registry
        reg = CreateObject("roRegistrySection", "auth")
        
        if reg.Exists("token")
            ' read token from registry
            token = reg.Read("token")
            
            ' and cache it in global node
            Utils_forceSetFields(m.global, {token: token})
        end if
    end if
    
    return token <> invalid and token.Len() > 0
end function

function Authenticate(username as String, password as String) as Boolean
    ?"Authenticate("username","password")"
    
    ' simulate successful auth API calls
    sleep(2000)
    token = "authtoken1234567890"

    ' save token to registry
    reg = CreateObject("roRegistrySection", "auth")
    reg.Write("token", token)
    reg.Flush()
    
    ' and to global node
    Utils_forceSetFields(m.global, {token: token})
    
    return true
end function

function DeAuthenticate() as Boolean
    ?"DeAuthenticate()"
    
    ' remove token from global node
    m.global.RemoveField("token")
    
    ' and from registry
    reg = CreateObject("roRegistrySection", "auth")
    reg.Delete("token")
    reg.Flush()
    
    return true
end function
