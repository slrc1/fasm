import string,random,sys

start = int(sys.argv[1])
end = int(sys.argv[2])
cnt = int(sys.argv[3])

alphabet = string.letters[0:52] + string.digits +string.punctuation
for count in range(cnt):
    p = ''
    for x in range(len(alphabet)):
        c =
alphabet[x]
        p += c
    print(p)
