import os,sys
os.system("ls -l")


def connect(name, port):
    os.system("whatsAppClient " , name , " yoda 04", port)

def send_message(receiver, msg):
    os.system("send " , receiver, " " ,msg)

if __name__ == "__main__":
    if sys.argv != 4:
        print("error number of arument need to be: name, port, receiver")

    connect(sys.argv[1], sys.argv[2])
    Number_of_iterations = 1000
    for i in range(Number_of_iterations):
        print("send msg number: " , i)
        send_message(sys.argv[3], "test msg " + i)
