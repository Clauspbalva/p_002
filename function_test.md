# **`function_test`**

Specification file for `function_test` function.

<br>

## 1. Requirements
---

### 1.1 ID
---
> f_000

<br>

### 1.2 Signature
---
> `test_results = function_test(test_config)`

<br>

### 1.3 Type and language
---
> Python function

<br>

### 1.4 Purpose
---
> Test a given function performing a set of test cases and computing its results (passed / failed)

<br>

### 1.5 Inputs
---

| Input | Description | Type & Domain |
|---|---|---|
| `test_config` | Configuration of tests to be performed | *key:value pairs* <br> `dict`

<br>

**`test_config`**: definition

| Input | Description | Type & Domain |
|---|---|---|
| `function` | Function identifier | Python identifier to a function object |
| `input_names` | List of *input names* | List of text elements <br> `list` |
| `tests` | List of tests to be performed | List of elements <br> `list` |
| `print_details` | Flag to indicate if details of test results should be printed in the output. Default `True` | Boolean <br> `bool` |

<br>

**`test_config.tests`**: definition

| Input | Description | Type & Domain |
|---|---|---|
| `id` | Test ID | Integer <br> `int` |
| `input_values` | List of *input values* | List of elements <br> `list` |
| `output_expected` | List of *expected output values* | List of elements <br> `list` |

<br>

### 1.6 Outputs
---



<br>

## 2. Algorithm
---

<span style='color:red'>TBD</span>

<br>

## 1. Test cases
---

<span style='color:red'>TBD</span>