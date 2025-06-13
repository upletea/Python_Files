swiftAlbums = ["Taylor Swift", "Fearless", "Speak Now", "Red", "1989", "Reputation", "Lover"]

print("Taylor Swift Albums:")
for album in swiftAlbums:
    print(album)  # Corrected placeholder with 'album'

albumToCheck = input("Enter an album to check: ")
if albumToCheck in swiftAlbums:  # Corrected placeholder with 'swiftAlbums'
    print(f"{albumToCheck} is in the list")
else:  # Corrected placeholder with 'else'
    print(f"{albumToCheck} is not in the list")  # Corrected indentation issue with 'albumToCheck'
