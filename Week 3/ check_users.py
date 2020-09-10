def check_users(current_users, new_users):
    pass
    lowercased_current_users= [username.lower() for username in current_users]

    for new_user in new_users:
        if new_user.lower() in lowercased_current_users:
            print("We're sorry, " + new_user + " is no longer available.")
        else:
            print("Excellent, " + new_user + "  is still available.")

if __name__ == "__main__":
    current_us = ['chris','haritha', 'sally', 'darnell', 'superman']
    new_us = ['george', 'ringo', 'superman', 'hannibal']
    check_users(current_us, new_us)