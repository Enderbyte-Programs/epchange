#!/usr/bin/python3
import sys
import enum
import os

if os.path.isdir("/usr/lib/epchange"):
    sys.path.insert(0,"/usr/lib/epchange")

import epappdata
import cursesplus

appdata:epappdata.AppDataFile

class Modes(enum.Enum):
    Command = 0
    User = 1
    SingleCommand = 2
    RunningFile = 2

class Config:
    args: list
    mode: Modes

def show_help():
    print("===== EPCHANGE HELP =====")
    print("usage: epchange [help|cmd|ui [options] [-c command] [-f file]")
    print("By default, if no args are provided, cmd mode will be started normally.")
    print("UI mode is user-friendly. To get that, run epchange-ui instead of just epchange")
    print("Or you can run 'epchange ui'")
    print("epchange cmd -c [command] runs that singular command then exits")
    print("epchange cmd -f [file] runs each line in that file as a command")

def args_has_cf_args():
    return "-c" in Config.args or "-f" in Config.args

def interpret(command:str):
    print("interpreting",command)

def ctrl_cf_args():
    if "-c" in Config.args:
        Config.mode = Modes.SingleCommand
        try:
            command = Config.args[Config.args.index("-c")+1]
        except:
            print("ERROR! Malformed -c argument")
        else:
            interpret(command)
    if "-f" in Config.args:
        Config.mode = Modes.RunningFile
        try:
            ftop = Config.args[Config.args.index("-f")+1]
            with open(ftop) as f:
                f.write()
def main_user_interface(stdscr):
    cursesplus.messagebox.showinfo(stdscr,["UI Mode"])

def main():
    global appdata
    args = sys.argv[1:]
    Config.args = args
    epappdata.register_app_name("epchange")
    appdata = epappdata.AppDataFile("config")
    appdata.default = {
        
    }
    appdata.load()
    if len(args) == 0:
        show_help()
        sys.exit()
    rtcommand = args[0]
    if rtcommand == "help" or rtcommand == "--help":
        show_help()
        sys.exit()
    elif rtcommand == "cmd":
        Config.mode = Modes.Command
        ctrl_cf_args()
    elif args_has_cf_args():
        ctrl_cf_args()
    elif rtcommand == "ui":
        Config.mode = Modes.User
    
if __name__ == "__main__":
    main()