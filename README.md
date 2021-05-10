# DjangoRangeMiddleware

<p><a href="https://github.com/othneildrew/Best-README-Template/graphs/contributors"><img src="https://camo.githubusercontent.com/6a58189bfdc0586c06288c336cc805272bf16b06ce1ba81f9d299e4ff46992fe/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f6f74686e65696c647265772f426573742d524541444d452d54656d706c6174652e7376673f7374796c653d666f722d7468652d6261646765" alt="Contributors" data-canonical-src="https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge" style="max-width:100%;"></a>



### A Django Middleware Service

* `Implements HTTP bytes-range requests`


<br>

#### When to use?
`If you have ever served video file with django you will see
that you can't rewind/forward the video, and thats because you
don't have bytes-range requests implemented.So if you want to
solve this problem you have to implement bytes-range requests.
And Using this package you can easily do it :)
`
#### `Bytes range:`
`
Byte-range requests occur when a client asks the server
for only a portion of the requested file.
The purpose of this is essentially to conserve bandwidth
usage by avoiding the need to download a complete file
when all that is required is a small section
`

## Installation

1. install the package using pip
    ```shell script
    C:/User> pip install DjangoRangeMiddleware
    ```

2. Add this to middleware `settings.py`
   ```python
   MIDDLEWARE = [
       '.........',
       'DjangoRangeMiddleware.middleware.RangesMiddleware',
   ]
   ```

* `And thats it.You're Done.Enjoy ;)`
