import scripts.clean_temp as clean_temp
import scripts.check_network as check_network
import scripts.disk_usage as disk_usage
import scripts.restart_network as restart_network

def menu():
    print("\n your IT Help Desk automation BOT 🌋 ")
    print("1. Clean temp files.")
    print("2. Check your internet connection")
    print("3. Show the disk usage")
    print("4. restart the network adapter ( windows )")
    print("5. exit program")

while True:
    menu()
    choice = input("Choose an option to start (1-5): ")
    if choice == '1':
        clean_temp.run()
    elif choice == '2':
        check_network.run()
    elif choice == '3':
        disk_usage.run()
    elif choice == '4':
        restart_network.run()
    elif choice == '5':
        print("Exiting program ... 🌋")
        break
    else:
        print("Invalid choice, try again")