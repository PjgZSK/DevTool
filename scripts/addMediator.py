
MEDIATOR_TEMPLATE = """
--[[
-- filepath: {0} 
-- AssetbundlePath:{1} 
-- PrefabName:{2}Panel
--]]


local {2}Mediator = OzClass("{2}Mediator", Mediator)

{2}Mediator.AssetbundlePath = "{1}"
{2}Mediator.PrefabName = "{2}Panel"
{2}Mediator.ShowType = MVCConst.ShowType.MAIN
{2}Mediator.NotShowClose = false

function {2}Mediator:listNotificationInterests()
    return {
    }
end

function {2}Mediator:handleNotification(notification)
end

function {2}Mediator:onRegister(data)
    self:initView()
    self:initData(data)
    self:initEvent() 
end

function {2}Mediator:onRemove()
end

function {2}Mediator:initData(data)
end

function {2}Mediator:initView()
end

function {2}Mediator:initEvent()
end


return {2}Mediator.new()
"""


from utility import safeWrite 

"""
module(mediator module)
  - name(module name)
  - medPathInDot(mediator file path in dot)
  - medPath(mediator file path)
  - medABPath(mediator Assetbundle path)

force
  - if force is false, write raise fileexistexception when file exist
"""
def addMediator(module, force = False):
    from re import sub
    fileContent = MEDIATOR_TEMPLATE
    fileContent = sub(r"\{0\}", module.medPathInDot, fileContent)
    fileContent = sub(r"\{1\}", module.medABPath, fileContent)
    fileContent = sub(r"\{2\}", module.name, fileContent)
    safeWrite(module.medPath, fileContent, force) 

def main():
    pass

if __name__ == "__main__":
    main()
