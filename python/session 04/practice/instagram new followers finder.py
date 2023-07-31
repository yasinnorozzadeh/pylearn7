from getpass import getpass
import instaloader

username = input("Username: ")
password = getpass("Password: ")
follower = input("Follower_usernem: ")

log = instaloader.Instaloader()
log.login(username, password)
profile = instaloader.Profile.from_username(log.context, follower)

file = open("followers.txt", "r")
oldf = []
for line in file:
    oldf.append(line.strip())
file.close()

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower.username)

f = open("followers.txt", "w")
for new_follower in new_followers:
    file.write(new_follower + "\n")
file.close()