try:
    my_data2 = open("mydata2.txt", encoding="UTF-8")

except FileNotFoundError as ex:
    print("File does not exist")
    print(ex.args)
else:
    print(my_data2.read())
    my_data2.close()
finally:
    print("Finished working with File")
