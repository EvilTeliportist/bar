# Bar

Bar is a very simple python progress bar class that allows you to implement printable progress bars into your programs.

## Installation
`$ pip install bar`

## Usage
```
from bar import ProgressBar

bar = ProgressBar(minimum, maximum)
bar.update(value) # value must be in between minimum and maximum
```
