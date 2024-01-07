try:
    a = open("a.txt")
    try:
        a.write("this is new content")
    except:
        print("exception occured while inserting")
    finally:
        a.close()
except:
    print("something went wrong")