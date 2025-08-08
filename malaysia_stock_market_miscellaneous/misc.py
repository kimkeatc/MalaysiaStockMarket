#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Import standard libraries
from enum import Enum
import logging


class CandleStatus(Enum):
    bullish = 1
    no_change = 0
    bearish = -1


class Price:

    def __init__(self, value: float = 0.000):
        if not isinstance(value, (int, float)):
            raise ValueError("Given value not a numeric number.")
        self.value = round(number=float(value), ndigits=3)

    def __str__(self):
        return f"Price: {self.value:.3f}"

    @property
    def next(self):
        if self.value >= 10:
            return Price(value=self.value + 0.02)
        elif self.value >= 1:
            return Price(value=self.value + 0.01)
        else:
            return Price(value=self.value + 0.005)

    @property
    def prev(self):
        if self.value > 10:
            return Price(value=self.value - 0.02)
        elif self.value > 1:
            return Price(value=self.value - 0.01)
        elif self.value == 0:
            logging.warning("Reaching minimum stock price.")
            return self
        else:
            return Price(value=self.value - 0.005)


def price_list(min_value: float = 0.0, max_value: float = 100.0):
    if min_value > max_value:
        min_value, max_value = max_value, min_value

    min_value, max_value = Price(value=min_value), Price(value=max_value)
    results = []
    while min_value.value <= max_value.value:
        results.append(min_value.value)
        min_value = min_value.next
    return results


def number_of_bid_diff(a: float, b: float):
    if a > b:
        a, b = b, a
    numbers = price_list(min_value=a, max_value=b)
    return len(numbers)


def get_candle_ratios(oPrice: float, hPrice: float, lPrice: float, cPrice: float) -> list[int, float, float, float]:
    status, head_ratio, body_ratio, tail_ratio = None, 0.0, 0.0, 0.0

    if hPrice == lPrice:
        status = CandleStatus.no_change.value
    elif cPrice > oPrice:
        status = CandleStatus.bullish.value
        head_ratio = ((hPrice - cPrice) / (hPrice - lPrice)) * 100
        body_ratio = ((cPrice - oPrice) / (hPrice - lPrice)) * 100
        tail_ratio = ((oPrice - lPrice) / (hPrice - lPrice)) * 100
    elif cPrice == oPrice:
        status = CandleStatus.no_change.value
        head_ratio = ((hPrice - cPrice) / (hPrice - lPrice)) * 100
        tail_ratio = ((cPrice - lPrice) / (hPrice - lPrice)) * 100
    elif cPrice < oPrice:
        status = CandleStatus.bearish.value
        head_ratio = ((hPrice - oPrice) / (hPrice - lPrice)) * 100
        body_ratio = ((oPrice - cPrice) / (hPrice - lPrice)) * 100
        tail_ratio = ((cPrice - lPrice) / (hPrice - lPrice)) * 100

    head_ratio = round(number=head_ratio, ndigits=4)
    body_ratio = round(number=body_ratio, ndigits=4)
    tail_ratio = round(number=tail_ratio, ndigits=4)

    return status, head_ratio, body_ratio, tail_ratio
