
# {0} -- the file path of open command, and its segment is dot
# {1} -- module name
OPEN_TEMPLATE = """
--[[
--filepath:{0}
--]]


{1}OpenCommand = OzDeclare("{1}OpenCommand", OzClass("{1}OpenCommand", SimpleCommand))

{1}OpenCommand.Main = "Main" -- open main page

function {1}OpenCommand:execute(notification)
    local type = notification.type
    -- local body = notification.body
    if type == {1}OpenCommand.Main then
        self.facade:registerMediator(MVCConst.Mediator.{1}Mediator)
    end
end


return {1}OpenCommand

"""

from utility import safeWrite 

# module(open command module)
#   - name(module name)
#   - ocPathInDot(open command file path in dot)
#   - ocPath(open command file path)
#
# force
#   - if force is false, write raise fileexistexception when file exist
def addOpenCommand(module, force = False):
    from re import sub
    fileContent = OPEN_TEMPLATE 
    fileContent = sub(r"\{0\}", module.ocPathInDot, fileContent)
    fileContent = sub(r"\{1\}", module.name, fileContent)

    safeWrite(module.ocPath, fileContent, force)
