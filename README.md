# MalaysiaStockMarket
Malaysia Stock Market related miscellaneous


# Build *.whl file
```
C:\Users\MalaysiaStockMarket> RMDIR /s /q build dist malaysia_stock_market_miscellaneous.egg-info
C:\Users\MalaysiaStockMarket> python setup.py sdist bdist_wheel
```

# Install package *.whl files under sub-directory, dist
```
C:\Users\MalaysiaStockMarket> python -m pip install --find-links=.\dist malaysia_stock_market_miscellaneous
```

# Uninstall package
```
C:\Users\MalaysiaStockMarket> python -m pip uninstall -y malaysia_stock_market_miscellaneous
```

# Applications

## Development
```
C:\Users\MalaysiaStockMarket> python
>>>
>>> from malaysia_stock_market_miscellaneous.misc import Price
>>>
>>> price = Price(value=1.00)
>>> price.value
1.0
>>> price.next.value
1.01
>>> price.prev.value
0.995
>>>
>>> from malaysia_stock_market_miscellaneous.misc import price_list
>>> price_list(min_value=0.3, max_value=0.35)
[0.3, 0.305, 0.31, 0.315, 0.32, 0.325, 0.33, 0.335, 0.34, 0.345, 0.35]
>>>
>>> from malaysia_stock_market_miscellaneous.misc import number_of_bid_diff
>>> number_of_bid_diff(a=0.3, b=0.35)
11
>>>
>>> exit()
C:\Users\MalaysiaStockMarket>
```
