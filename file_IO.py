from encodings.hex_codec import hex_encode

# open("File name" , "mode") => yaha filename first parameter
# pass kiya phir second parameter mode pass kiya

f = open("demo.txt" , "r")

data = f.read()
#isse hum file mein read bhi krr sakhte hee
#agar number as a argument dee diya toh utna hee letter read karte aayega see
# code
# data = f.read(5)
print(data)
#jab bhi file open karre close bhi karna

# print("And now readline will execute after this sentence")
# .readline() => method read karta line by line okk
# data_line = f.readline()
# print(data_line)
#
f.close()

# write => overwrite mode hota hee
# append => yeeh add karta data in the end simple


#code to append the data

fa = open('demo.txt' ,'a')

fa.write("\nAppending this line to it okk")

fa.close

#code to write a data and newly made it

fw = open("write.txt" , 'w')

fw.write("Hii I created a write file using the .write method of python \nHappy that file is created :) ")

fw.close()

#best alternative syntax to use for file without assigning a variable to it
with open("example.txt", "w") as file:
    file.write("This is the file I created by alternative syntax \nHappy I learned too much of concept :)")
    file.close()

# yaha indentation important hee okk


