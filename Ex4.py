def caesar_cipher(file_name, shift, direction):
    if direction=="right":
        n=shift
    elif direction=="left":
        n=-shift
    else:
        print("Direction must be 'left' or 'right'")
        return
    output_file="ciphertext.txt"
    with open(file_name,"r",encoding="utf-8") as infile, \
         open(output_file,"w",encoding="utf-8") as outfile:
        for line in infile:
            new_line=""
            for char in line:
                x=ord(char)
                if 'A'<=char<='Z':
                    y=(x+n-65)%26+65
                    new_line+=chr(y)
                elif 'a'<=char<='z':
                    y=(x+n-97)%26+97
                    new_line+=chr(y)
                elif char.isdigit():
                    new_line+=char
                else:
                    new_line+=char
            outfile.write(new_line)
    print("Cipher text saved to: ", output_file)