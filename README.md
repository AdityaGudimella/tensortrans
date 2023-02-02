# TensorTrans

## Introduction

TensorTrans is a tool transpiler that converts code written in one tensor library
to another. Initially, conversion between TensorFlow 2 and PyTorch 2 will be supported,
but in the future, JAX is also planned to be supported.

## Usage

### Installation

`pip install tensortrans`

### Command Line Interface

The command line interface is the easiest way to use TensorTrans. It can be used
to convert a single file or a directory of files. The following command will convert
code in the `examples` directory and save the converted code to the `converted` directory.

```bash
tensortrans tf2pytorch examples converted
```
