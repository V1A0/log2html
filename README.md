# Log2HTML

Log2HTML is a application for VkScrapper. For convert your log to simple HTML page.

## Libraries Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```python
pip install argparse | pip install progress.bar | pip install Bar
```

## Usage

### Before you start
Add your own HTML code to defaut.txt
For set log-taple place add to code line:
```html
<!--LOG-TABLE-HERE-->
```

### Converting
For run a converter:
```python
py log2html.py -f log_file.txt
```
For see help:
```python
py log2html.py -h
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)