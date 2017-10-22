# Midterm Project
 **Categories:** web
 
 **Description:** 
 
> An informant told me that our old friend dustin backups all of his data into a private Xenon server in a pretty new and small Firm that does web hosting, you can find their website here -
> https://superwebhosting.xyz
> Reach out to them and help me find his website so I can steal his semester project and hand it to my professor before him.

> Hint:my informant just sent me this message:
> All "Xenon File Repositories" don't have access to the internet.
> do you think you can still find a loophole in thier system?

## Story-time!

We started browsing site and one of the first things we tried was checking for a /admin page(due to some of the previous challenges we did here having such a page).

![](https://gyazo.com/40419f1b853f9212e26477a63cfd4de7.png)

As you can see from the file system paths disclosed by this nice and informative error, the challenge is labeled "DnsChal", so after a quick look at whois(which didn't do us much good), we went to our trusty friend sublist3r so it might find some subdomains for us to explore:) 

![](https://gyazo.com/573a56c0ac39333d3d744bb12b708b33.png)


- www.superwebhosting.xyz
- networktoolkit.admin.superwebhosting.xyz
- older.sublist3r.versions.work.better.for.superwebhosting.xyz

We already knew the first one(duh!), and the third one appears to be dead, but the second one brings us to some sort of admin panel!

The three availble commands:

- Ping(/ping.do) - pings a host to see if it's alive, returns alive/dead status.
- DNS lookup(/dnssearch.do) - looks like output of the dig command, so it probably is exactly that^^
- Tracert(/trace.do) - traces the route to a host, shows every hop along the path.

The first thing we tried is to pull off some command injection or at least inject some parameters to the commands used, but things seemed well-handled and every try along those lines resulted in something like this:

![](https://gyazo.com/916de12337729c2c36967b1fa338ccdb.png)
(we tried that direction for quite a while, because "don't try to hack us" seemed pretty encouraging^^)

Anyway... fast forward to the more interesting parts! one of the other things we noticed pretty early on was that /dnssearch.do receives two extra parameters apart from the one supplied on the web page:

![](https://gyazo.com/fa44a4dbe8428cf56db2b8008a79b196.png)

dnsAddr is the original user input, and dnsServer/dnsType are presumably used in their respective places in the dig command for queried server/request type. This can be confirmed to indeed be the case when you supply an address that won't respond in the dnsServer parameter:

![](https://gyazo.com/05373744a6618235d35e2d19a3a36a93.png)


One more thing we noticed while playing with the commands is that the first hop tracert goes through is 192.168.0.254, we then traced the path to 192.168.0.254 and saw this output: 

![](https://gyazo.com/50e8348da3203317b7e489b75d1fa2d7.png)

This means that our beloved networktoolkit.admin.superwebhosting.xyz probably has some mysterious internal network shenanigans going, and his IP is 192.168.0.40! 

At this point we tried sending some dns queries with dnsServer=127.0.0.1 or 192.168.0.40 but to no avail, it seems that our host is not the droid(erm... I mean, internal DNS server) we are looking for. Good thing we can pingsweep the internal network with /ping.do that was so kindly supplied to us, maybe we will find some DNS server to query!

(the logic behind trying to find an internal DNS server at this point was something like that... the only "useful" command we have available is dig, and if we aren't supposed to use it on some internal server but on a publicly accessible one, why did we even need it there? if it were true, we could have solved the challenge from our own PC, which is very unlikely to be the case)

So let's pingsweep:

```javascript
for(var i=1;i<255;i++){$.post('./ping.do','pinghost=192.168.0.'+i,function result(res){console.log(res)})}
```

![](https://gyazo.com/92a58e8e1eda8b8664fcd3254ed9e481.png)

Nice! so we have 192.168.0.47 and 192.168.0.1 as well now. 192.168.0.1 didn't seem to be very helpful to our cause, but 192.168.0.47 actually responds to DNS queries. Woohoo!

![](https://gyazo.com/d1458ee3c50e4b264749b6a4c38520e3.png)

It is also nice to compare this with the output for the same dnsAddr when querying a public DNS server as a sanity check(they should be different hopefully):

![](https://gyazo.com/d7df37ce256aa2c8a99c186d401b48ee.png)

And now we are going to use the last parameter we didn't really use yet, dnsType. We did actually play around with it throughout the challenge(setting it to ANY,NS,...), but up until now it didn't really yield any results worth mentioning. But now... Due to internal servers having a much higher likelihood of being misconfigured, we thought it could be worth to try to send a zone transfer request([if you aren't familiar with it, wiki-time!](https://en.wikipedia.org/wiki/DNS_zone_transfer)) to the internal server, maybe we'll get all the records in one go:)

Lo and behold, an unexpected end to our journey^^

![](https://gyazo.com/1158271c89cceb2ddd970b9c2d2a0add.png)







