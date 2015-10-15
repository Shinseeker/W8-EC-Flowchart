#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Demonstrating a flowchart."""


bank_charge = 5
account_bal = -5
if account_bal < 0:
    account_bal = account_bal - bank_charge
print('The account balance is ' + str(account_bal))
