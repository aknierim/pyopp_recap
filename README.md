# pyopp_recap

Recap of the ErUM-Data-Hub PYOPP 2025 workshop in Aachen.

## Prerequisites

Install the custom `pygments_style` module in an environment of your choice, e.g. using uv:
```
$ uv pip install ./pygments_style
```
Make sure you activate that environment whenever you build the slides.

Alternatively, a mamba environment is also provided:
```
$ mamba env create --file=environment.yml
```
Activate the environment:
```
$ mamba activate codetheme
```


## Building the slides

You can build the slides using make (requires latexmk):
```
$ make all
```
or in preview mode:
```
$ make preview
```



