def user_info():    
    name = input("\n What You'd Like To Be Called: ").capitalize()
    username = input("\n Enter your username on this system: ").capitalize()
    ai_name = input("\n What You'd Like To Call Your Personal AI Assistant: ").capitalize()
    print("\n\n\t Welcome " + name + "...\n")
    return name, username, ai_name

user_info()

# print(f"Hello, I'm {user_info(ai_name)} & I'm here to help you... \n")
                
