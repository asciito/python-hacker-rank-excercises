# Capitalize

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, *alison heck* should be capitalised correctly as <span style="font-weight: 200">Alison Heck</span>.

<span style="letter-spacing: .1rem">
    <i style="color: red">a</i>lison <i style="color: red">h</i>eck
</span>

Given a full name, your task is to capitalize the name appropriately.

**Input Format**

A single line of input containing the full name, $S$.

**Constraints**
- $0 < len(S) < 1000$
- The string consists of alphanumeric characters and spaces.

**Note**: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

**Output Format**

Print the capitalized string, $S$.

**Sample Input**
```
chris alan
```

**Sample Output**
```
Chris Alan
```