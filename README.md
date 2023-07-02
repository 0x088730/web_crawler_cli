# 🕷️ CLI-based Web Crawler


## This miniscule project attempts to satisfy the following requirements:
1. The start URL should be configurable
2. It should be able to restrict the traversal by one or several domains
3. It should never visit the same site twice
4. The crawler should remember its state
5. It should be able to shut it off, and restart it at a later time, and continue where it left off

## Installation
```zsh
git clone https://github.com/0x088730/web_crawler_cli.git
```
> Clone the project

```zsh
cd web_crawler_cli
```
> Enter into the directory

```zsh
python -m venv venv
```
> Setup a virtual environment

```zsh
source venv\Scripts\activate.bat
```
> Activate the virtual environment

```zsh
pip install -r requirements.txt
```
> Install the requirements


## Usage
```zsh
$ python main.py [-h] [--initial_url INITIAL_URL] [--allowed_domains ALLOWED_DOMAINS [ALLOWED_DOMAINS ...]] [--depth DEPTH]

optional arguments:
  -h, --help            show this help message and exit
  -i INITIAL_URL, --initial_url INITIAL_URL
                        Enter a start url (default: 'https://skillshow.vercel.app')
  -ad ALLOWED_DOMAINS [ALLOWED_DOMAINS ...], --allowed_domains ALLOWED_DOMAINS [ALLOWED_DOMAINS ...]
                        Enter allowed domains (defualt: 'skillshow.vercel.app')
  -d DEPTH, --depth DEPTH
                        Enter the depth, aka number of sites to crawl (default: 1)

```
### Examples
```zsh
$ python main.py
```
> Use default values

```zsh
$ python main.py -i https://skillshow.vercel.app -ad skillshow.vercel.app -d 2
```
> Start crawling from `https://skillshow.vercel.app`, restrict the traversal of domains to `skillshow.vercel.app` at `depth=2` 

## State
The state of the crawler can be saved using `pickle` or `JSON`. 
```YAML
{
  "imageUrl": "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Fcustomer1.png&w=128&q=75",
  "sourceUrl": [
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Ficons%2Ftop.png&w=128&q=75",
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Fcustomer2.png&w=128&q=75",
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Fworker3.png&w=1080&q=75",
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Fworker2.png&w=1080&q=75",
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Fworker4.png&w=1080&q=75",
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Ffeelgreat.png&w=828&q=75",
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Fcustomer4.png&w=128&q=75",
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Fworker6.png&w=1080&q=75",
    "http://skillshow.vercel.app/assets/images/logo.svg",
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Fworker5.png&w=1080&q=75",
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Ftogether.png&w=828&q=75",
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Fcustomer3.png&w=128&q=75",
    "http://skillshow.vercel.app/_next/image?url=%2Fassets%2Fimages%2Fworker1.png&w=1080&q=75",
    "http://skillshow.vercel.app/_next/image?url=https%3A%2F%2Fstatic.legitscript.com%2Fseals%2F11058625.png&w=384&q=75"
  ],
  "depth": 2
}
```
> State after running the 2nd example
## Future works
* Make it async 

