# Remote Technician
 **Categories:** os, networking
 
 **Description:** 
 
> When a technician starts to work on field, he notifies the HQ using a client utility.
> Help us find vulnerabilities to make the world a better place.
> The server ip is 34.215.112.21

[TCPClient.exe](./TCPClient.exe)

## Story-time!

We started out by giving the binary a quick look in IDA, just to get the general idea of what it's supposed to do. Unsurprisingly(after all, it was named tcpclient..), it seemed to mostly just send and receive some data over tcp.

![Brief look in IDA](https://gyazo.com/e30ae7b27331a02f087487e957d594f5.png)

Wireshark, up!

Mysterious-executable-from-unknown-source-which-we-only-vaguely-trust, run!

We saw the following data exchange with 34.215.112.21 on port 5966:

![TCP Stream](https://gyazo.com/7956868966c161499ac5d82a67bff0c7.png)

```python
alive_packet = 'CMD: \x01\x01\x01\x05alive'
```

When we tried to resend the data while modifying the parameters a little, we noticed that while changing most of the things didn't really matter, changing \x05 actually made the "alive" command fail. Since alive is 5 bytes long we assumed that this byte indicates the length of the command that follows.

Testing the theory with some other commands:

```python
import socket

def sendp(cmd):
        
	packet = 'CMD: \x01\x01\x01'+chr(len(cmd))+cmd
	a=socket.socket()
	a.connect(('34.215.112.21',5966))
	print 'sending command: '+cmd
	print a.send(packet)
	print a.recv(1024)
	print '--'
	print a.recv(1024)
```

It seems that our theory was correct, but unfortunately, some of the commands are not allowed!

![some commands are filtered](https://gyazo.com/0c0ce84905ce728f3800cbc2b7814d13.png)

So now we just need to find a bypass for this and somehow read flag.

After a few more attempts...

![hurray!](https://gyazo.com/0587763f7a94063d5ff24952dea4b591.png)

Yay:)




