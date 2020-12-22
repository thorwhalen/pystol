All python tools mentioned below are registered with pypi under the same name, so are 
"pip installable", meaning you just need to do a 
```
pip install PKGNAME
```
for the `PKGNAME` you want to try out!)

# Data tools

## py2store
Storage CRUD how and where you want it.

List, read, write, and delete data in a structured data source/target, as if manipulating simple python builtins (dicts, lists), or through the interface you want to interact with, with configuration or physical particularities out of the way. Also, being able to change these particularities without having to change the business-logic code.

[more info](https://github.com/i2mint/py2store/blob/master/README.md)

Note: py2store doesn't require any third party libraries to function, except if using specialized tools (like mongoDB, sql, audio tools...). It's pure builtin python (so very light weight). On the other hand if you try to use a specialized tool, you'll have to pip install the dependencies yourself.

Note: py2store is in the process of being broken up in smaller pieces to make it even more light weight, and separate specialized tools as separate add-ons.

## slang
Basic tools for a "syntactic approach" to sound recognition. 

[more info](https://github.com/otosense/slang/blob/master/README.md)

## lined
Nibble utils to build pipelines.

[more info](https://github.com/otosense/lined/blob/master/README.md)

## haggle
A very convenient tool to search, download, and use kaggle datasets as easily as it gets. 
Based on py2store.

[more info](https://github.com/otosense/haggle)


## stream2py
Bring data streams to python, with ease.

[more info](https://i2mint.github.io/stream2py/index.html)


# Deployment tools

## oui
Reusable UI components for JavaScript with Python interfaces

For example:
[multi_time_vis](https://github.com/otosense/oui/blob/master/oui/multi_time_vis/README.md)
[splatters](https://github.com/otosense/oui/tree/master/oui/splatter)

[more info](https://github.com/otosense/oui)


## py2http
Dispatching Python functions as http services.

[more info](https://github.com/i2mint/py2http/blob/master/README.md)

Note: Also worth mentioning [py2api](https://github.com/i2mint/py2api/blob/master/README.md), 
the original version of py2http. It's less flexible, but at the time or writing this, 
still has useful stuff not yet transferred. Namely, it has more documentation and examples.

## http2py
Tools to create python binders to http web services. Here, we develop python data access to web content through http request such as web services or web pages.

[more info](https://github.com/i2mint/http2py/blob/master/README.md)

## http2js
http2py, but for... JS instead of python.

[more info](https://github.com/i2mint/http2js/blob/master/README.md)



# A selection of fun (or useful) projects that use the above. 

## graze
Cache the internet. Was just a tiny (45mn) example application of py2store to keep local copies of url-referenced contents. 
Has become more useful than expected.

[more info](https://github.com/thorwhalen/graze)

## grub
A (py2store-based) ridiculously simple search engine maker. 

[more info](https://github.com/thorwhalen/grub)

## invest
Python access to structure stock market information
[more info](https://github.com/thorwhalen/invest)

## cult
Religious texts search engine. 18mn application of `grub`.

[more info](https://github.com/thorwhalen/cult)

## laugh
A (py2store-based) joke finder.

[more info](https://github.com/thorwhalen/laugh)

## elections
A (py2store-based) 2020 elections stats accessor. 

[more info](https://github.com/thorwhalen/elections)
