from tmodule import TModule 

m = TModule("Test") 
m.ocPathInDot = "TestOpenCommand"
m.ocPath = "TestOpenCommand.lua"

from addCommand import addOpenCommand
try:
    addOpenCommand(m)
except Exception as e:
    print(e)

from addMediator import addMediator
m.medPathInDot = "TestMediator"
m.medPath = "TestMediator.lua"
m.medABPath = "test/testpanel.u3d"

try:
    addMediator(m)
except Exception as e:
    print(e)


