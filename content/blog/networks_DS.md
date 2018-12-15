---
date:   "2018-10-05"
publishdate: "2018-10-05"
draft: false
title: "Why do we as Data Scientists care about how computers communicate?"
tags: ['cyber', 'data-science-development', 'networks', 'tr-blog']
series: ['Cyber Data Science']
categories: ['English']
img: '/images/blog/2018-10/networks.png'
toc: true
---

You turn on your computer, and connect to the WiFi. You open your browser and
remember that you have to pay your credit card. You search for the bank's name
and click the first link you see, because the first one is *always* the correct
one. You submit the credit card information and then get an email confirming
your payment. But, how are you sure you submitted your information in the bank's
page? Or, how are you sure no one gained access to it?

  When you turned on your computer, connected to the WiFi, opened the browser and
started searching, your computer started sending little pieces of information in
what are called packets. This packets contain the message or information you
want to send, but also who sent it and where it is going. We identify the
computers communicating using primarily IP Addresses, which are numbers that
specify your internet address. However, how this computers communicate, validate
each other, and understand the messages varies greatly by the network protocol
you are using.

  But, why do we as Data Scientists care about how computers communicate? Over
the last years there has been a surge in the amount and complexity of data we
analyze. This has caused that many projects need to be developed in
what is called a 'cloud', which is really someone's else computers. Depending on
the project you are working you might need to know which network protocol to
use and how to use it to pull data from the cloud or from a database. In this
blog post I'm going to mention briefly a couple of protocols and some of their
usages. I divided the protocols by whether they are encrypted or not.
(We'll go back to this shortly)

## Non-Encrypted Protocols

### File Transfer Protocol

File Transfer Protocol, or FTP, as it's commonly known, is a client-server
protocol, meaning that there is a client (your computer) and
there is a server (someone's else computer) communicating. These protocols tend
 to communicate through a specific port. Imagine this as if you are calling a
 company, but already know the extension of the person you want to communicate
  with. When the client initiates a connection, the default in FTP is to use
  port 21. This protocol is fairly common in web development.

Some known GUI Clients for FTP are:
* FileZilla
* WinSCP

### Hypertext Transfer Protocol

Hypertext Transfer Protocol, or HTTP, is also a client-server protocol.
HTTP works with a series of methods that define how the communication between
the client and the server is going to work. These are:

* GET - to **get** information from the server
* POST - to **post** information to the server
* PUT - to **update** information in the server
* DELETE - to **delete** information in the server

One way in which organizations share data is through Application Programming
Interfaces. These API's as they are commonly known, are commonly written to
communicate through HTTP. If you need to evaluate HTTP resources you can do
so through the following methods:

* In R: The `httr` package.
* In Python: The `requests` package.
* GUI Application: Postman

## The importance of encryption in Data Science
The two methods I have mentioned are non-encrypted methods. But what does
encryption means and why is it useful? According to the
[Oxford Dictionaries](https://en.oxforddictionaries.com/definition/encryption)
it is defined as

> "The process of converting information or data into a code,
especially to prevent unauthorized access."

This 'process of converting information or data into a code' is done by
encryption algorithms. Encryption algorithms become necessary when dealing with
sensitive or confidential information as it protects it from unauthorized
access. They do this in multiple ways and levels, here I discuss TLS and SSH,
which are two of the most common encrypted protocols.

## Encrypted Protocols

### Transport Layer Security

Transport Layer Security is an encrypted client-server protocol based on the
sharing of some documents called certificates. These are documents validated
by an independent authority which validates that the website is owned by who
it says it's owned. Once the client tries to connect to the server, the server
sends part of its certificate to the client. This is known as the public key.
This public key and a private key which is stored on the server form a
cryptographic key which encrypts all the communication between the server and
the client. This is now the standard for all web pages in the internet. TLS
connections are represented by HTTPS, standing for HTTP Secure and are done
by default through port 403.

### Secure SHell

Secure Shell is also an encrypted client-server protocol based on the sharing of
 documents called SSH keys. Similar to in Transport Layer Security, these keys
 are used to form the cryptographic key that masks the communications. However,
 SSH is mostly used to gain remote access to other computers. It communicates
 through port 22 and is mostly used from the terminal. If you need to gain
 access to a server, it will probably be using SSH.

## Conclusion

In general, we can see the application of many of these protocols in our career
as data scientists. In this blog post I covered only a small amount of the depth
of computer networks, if you are interested, I encourage to look for more
resources or write to me.