#!/usr/bin/python -O

from save_switcher import SaveSwitcher
from utils import *

def main():
    try:
        save_switcher = SaveSwitcher()

    except OSError:
        print "Invalid OS"

    except IOError:
        print "No save file found. Please start VVVVVV ",
        print "and run this program again."

    else:
        menu_items = ['show', 'backup', 'restore', 'exit']

        if save_switcher.first_run:
            print "First run detected... "
            print save_switcher.profiledir + " created"
            print

        else:
            print "Backup directory is " + save_switcher.profiledir
            print

        not_done = True

        print "Welcome to VVVVVV MultiSave"

        while not_done:
            print
            print "Main Menu:"
            print "1. Show backups"
            print "2. Create Backup of Save"
            print "3. Restore from Backup of Save"
            print "4. Delete Backup"
            print "q. Quit"
            choice = raw_input("Choice: ")
            print
            
            if choice == "1":
                if save_switcher.get_backups():
                    print "Here's a list of your backups"
                    show_list(save_switcher.get_backups())

                else:
                    print "There are currently no backups"
                        

            elif choice == "2":
                not_finished = True
                while not_finished:
                    if save_switcher.get_backups():
                        print "Here's a list of your backups"
                        num_backups = show_list(save_switcher.get_backups())
                        print "You have " + str(num_backups) + " backup(s)"

                    else:
                        print "There are currently no backups"
                        
                    print "Please enter a name for the backup"
                    print "or 'quit' (without the quotes) to return to the ",
                    print "main menu"
                    backup_name = raw_input("Name: ")
                    if backup_name == 'quit':
                        not_finished = False
                        break
                    elif ';' in backup_name:
                        print "Sorry, we don't take semicolons. It throws a ",
                        print "spanner in our cogs"
                        print
                        continue
                    try:
                        success = save_switcher.backup_save(backup_name)

                    except IOError:
                        print "You do not have access to the directory."
                        continue

                    else:
                        if not success:
                            print "An Error Occurred. Perhaps use a ",
                            print "different backup name?"
                            continue
                        not_finished = False
                        break

            elif choice == "3" and save_switcher.get_backups():
                print "WARNING: WILL OVERWRITE CURRENT SAVE"
                print "If you have not done so already, it is strongly advised to"
                print "enter 'quit' at the next prompt and make a backup NOW"
                print
                print "Here's a list of your backups"
                num_backups = show_list(save_switcher.get_backups())
                print "You have " + str(num_backups) + " backup(s)"
                print "Enter the name of the backup that you wish to restore"
                print "or 'quit' (without quotes) to return to the main menu"

                backup_name = raw_input("Name: ")
                if backup_name == 'quit':
                    continue

                save_switcher.restore_save(backup_name)
                print "Done!"

            elif choice == "4" and save_switcher.get_backups():
                print "Here's a list of your backups"
                num_backups = show_list(save_switcher.get_backups())
                
                print "You have " + str(num_backups) + " backup(s)"
                print "Enter the name of the backup that you wish to delete"
                print "or 'quit' (without quotes) to return to the main menu"
                print "WARNING: THIS CANNOT BE UNDONE"

                backup_name = raw_input("Name: ")

                if backup_name == 'quit':
                    continue

                save_switcher.delete_save(backup_name)
                print "Done!"
                
            elif choice == "q" or choice == "Q":
                not_done = False
                print "Quitting..."

            else:
                print "Invalid Choice"
                
if __name__ == "__main__":
    main()
