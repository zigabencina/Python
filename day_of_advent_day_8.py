dict1 = {
    "0":(" aaaa " ,  "b    c", "b    c"," .... ","e    f", "e    f", " gggg "),
    '1':(" .... " ,  ".    c", ".    c"," .... ",".    f", ".    f", " .... "),
    '2':(" aaaa " ,  ".    c", ".    c"," dddd ","e    .", "e    .", " gggg "),
    '3':(" aaaa " ,  ".    c", ".    c"," dddd ",".    f", ".    f", " gggg "),
    '4':(" .... " ,  "b    c", "b    c"," dddd ",".    f", ".    f", " .... "),
    '5':(" aaaa " ,  "b    .", "b    ."," dddd ",".    f", ".    f", " gggg "),
    '6':(" aaaa " ,  "b    .", "b    ."," dddd ","e    f", "e    f", " gggg "),
    '7':(" aaaa " ,  ".    c", ".    c"," .... ",".    f", ".    f", " .... "),
    '8':(" aaaa " ,  "b    c", "b    c"," dddd ","e    f", "e    f", " gggg "),
    '9':(" aaaa " ,  "b    c", "b    c"," dddd ",".    f", ".    f", " .... ")
}


stevilo = input("Vnesi stevilo: ")
stevilo2 = ()

for row in range(len(dict1[stevilo])):
    if stevilo > 9:
        stevilo2
    print(dict1[stevilo][row])
    print(end= "")
