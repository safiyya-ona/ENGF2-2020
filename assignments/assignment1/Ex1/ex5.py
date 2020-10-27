#alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# data for frequency table from http://letterfrequency.org/
def break_cipher(text):
    text = text.upper() #makes text upper case
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintexts = []
    for cipherKey in range(len(alphabet)): #checks each comnination in alphabet
        plaintext = ""
        for letter in text:
            index = alphabet.find(letter) #finds the letter's index in alphabet
            shift = index - cipherKey #adjusts the possible shift
            if shift < 0: #ensures the shift isnt negative
                shift += len(alphabet) #makes shift positive
            plaintext += alphabet[shift] #adds letter to plaintext combination
        plaintexts.append(plaintext)
    
    #prints all possibilities
    print("These are all possibilities")
    for plaintext in plaintexts:
        print(plaintext)
    
    #makes frequent pairs into a list
    
    fPairs = "th he an in er on re ed nd ha at en es of nt ea ti to io le is ou ar as de rt ve"
    fPairs = fPairs.upper() #makes pairs upper case
    frequent_pairs = list(map(str, fPairs.split(" "))) #splits the fpairs string and creates a list of frequent pairs
    
    #searches for pairs through strings, doesnt work all the time
    print("These could be most probable plaintext combinations")
    for plaintext in plaintexts:
        for pair in frequent_pairs:
            if pair in plaintext:
                print(plaintext)

ciphertext = input("Enter cipher text ")
break_cipher(ciphertext)