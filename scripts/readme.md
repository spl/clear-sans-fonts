# Scripts for Clear Sans

This directory contains scripts that were involved with generating the [UFO
sources][ufo-sources].

## Before running

We use [`poetry`][poetry] to run these scripts. Install it first.

All scripts in `scripts` expect you to be in the `scripts` directory. So first:

```sh
cd scripts
```

To install the dependencies, run:

```sh
./install.sh
```

## Running

# To create new UFO sources, run:

```sh
./extractUfo.sh
```

## Formatting code

# To format the Python code in this directory, run:

```sh
./format.sh
```

## License

The code in this directory is under the [Blue Oak Model License 1.0.0][license].

[license]: ./license.md
[poetry]: https://python-poetry.org/
[ufo-sources]: ../sources
