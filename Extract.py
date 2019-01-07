from pathlib import Path

# If you are using backslashes (\) use double backslashes (\\).
# The LOCATION IS THE XML FILE not the folder.
# Example: C:\\Program Files\\Bitdefender\\Bitdefender Security\\settings\\system\\excludemgr.xml
fileLocation = Path("C:\\Program Files\\Bitdefender\\Bitdefender Security\\settings\\system\\excludemgr.xml")

def main():
    excluded = []
    
    # Check if the file exists, then read the data and assign it to the "data" var.
    if(fileLocation.is_file()):
        print("File Found!")
        with open(fileLocation) as file:
            data = file.readlines()
    else:
        print("ERROR: File location not found!")
        exit(1)

    print("\nExcluded Locations:")
    # Read the data and output all excluded locations. Note: All excluded locations are put in the "excluded" list.
    for i in range(len(data)):
        if("ExcludeFlag" in data[i]):
            excluded.append((((data[i].split(">"))[1]).split("<")[0]))
            # Append each excluded location to the excluded list for future use.
            # (((data[i].split(">"))[1]).split("<")[0]) is the filter. This ensures it only prints the relevant information.

    # Print the list.
    print(*excluded, sep = "\n")


if __name__ == "__main__":
    main()