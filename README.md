All python tools mentioned below are registered with pypi under the same name, so are 
"pip installable", meaning you just need to do a 
```
pip install PKGNAME
```
for the `PKGNAME` you want to try out!)

# Data tools

## [py2store](https://pypi.org/project/py2store)
Storage CRUD how and where you want it.

List, read, write, and delete data in a structured data source/target, as if manipulating simple python builtins (dicts, lists), or through the interface you want to interact with, with configuration or physical particularities out of the way. Also, being able to change these particularities without having to change the business-logic code.

Note: py2store doesn't require any third party libraries to function, except if using specialized tools (like mongoDB, sql, audio tools...). It's pure builtin python (so very light weight). On the other hand if you try to use a specialized tool, you'll have to pip install the dependencies yourself.

[dol](https://pypi.org/project/dol) contains the no-dependencies (all builtin) core tools of py2store.
Source-specific packages use `dol` (along with specific dependencies) such as 
[mongodol](https://pypi.org/project/mongodol/), 
[s3dol](https://pypi.org/project/s3dol/), 
[redisdol](https://pypi.org/project/redisdol/), 
[dynamodol](https://pypi.org/project/dynamodol/), 
[sshdol](https://pypi.org/project/sshdol/), etc.

Further, several packages use `dol` to create the same consistent dict-like intervace to all kinds of objects, such as:
- [haggle](https://pypi.org/project/haggle): Easily search, download, and use kaggle datasets.
- [hubcap](https://pypi.org/project/hubcap/): Dict-like interface to github.
- [graze](https://pypi.org/project/graze): Cache the internet.
- [grub](https://pypi.org/project/grub): A ridiculously simple search engine maker. 
- [msword](https://pypi.org/project/msword/): Simple mapping view to docx (Word Doc) elements
- [pyckup](https://pypi.org/project/pyckup): Grab data simply and define protocols for others to do the same.
- [hear](https://pypi.org/project/hear): Read/write audio data flexibly. 
- [tabled](https://pypi.org/project/tabled): Data as `pandas.DataFrame` from various sources


## [slang](https://pypi.org/project/slang)
Basic tools for a "syntactic approach" to sound recognition. 
For instance, allows one to map signals (e.g. sound) ML to computational linguistics problems.


## [meshed](https://pypi.org/project/meshed)
Nibble utils to link functions (e.g. pipelines, DAGs, and such).
Also see [lined](https://github.com/otosense/lined/blob/master/README.md) for tools specific to pipelines (linear DAGs).


## [haggle](https://pypi.org/project/haggle)
A very convenient tool to search, download, and use kaggle datasets as easily as it gets. 
Based on py2store.


## [more stream2py](https://pypi.org/project/stream2py)
Bring data streams to python, with ease.


# Deployment tools

## [front](https://pypi.org/project/front/)

Core tools to build UIs (CLIs, GUIs) from backend python code.
For example [streamlitfront](https://pypi.org/project/streamlitfront/) and [dag2app](https://pypi.org/project/dagapp/).

## [py2http](https://pypi.org/project/py2http)
Dispatching Python functions as http services.

Note: Also worth mentioning [py2api](https://github.com/i2mint/py2api/blob/master/README.md), 
the original version of py2http. It's less flexible, but at the time or writing this, 
still has useful stuff not yet transferred. Namely, it has more documentation and examples.

## [http2py](https://pypi.org/project/http2py)
Tools to create python binders to http web services. Here, we develop python data access to web content through http request such as web services or web pages.

## [http2js](https://pypi.org/project/http2js)
http2py, but for... JS instead of python.

## oui
Reusable UI components for JavaScript with Python interfaces

For example:
[multi_time_vis](https://github.com/otosense/oui/blob/master/oui/multi_time_vis/README.md)
[splatters](https://github.com/otosense/oui/tree/master/oui/splatter)

[more info](https://github.com/otosense/oui)



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
