# blockchain-currency
This chat bot solves the problem of instant conversion of your cryptocurrencies and currencies.
The code also includes a calculator of currencies of interest.



<<<To get started, we need to import the libraries:

  < Import files:

   import telebot
   from telebot import types




<<<Enter on the command line:

   pip install pyTelegramBotAPI
   pip3 uninstall telebot




<<<To work with exchange rates - install CoinGeckoAPI

  < Import files:

   from pycoingecko import CoinGeckoAPI
  
   
  < Enter on the command line:

   pip install pycoingecko

  
  < To set the id of currencies, we use this document:

   https://docs.google.com/spreadsheets/d/1wTTuxXt8n9q7C4NDXqQpI3wpKu1_5bGVmP9Xz0XGSyU/edit#gid=0




<<<To convert, install this file:

   https://pypi.org/project/py-currency-converter/

  
 < Import files:

   from py_currency_converter import convert

  
 < Enter on the command line:

   pip install py-currency-converter




***
Default base currency is USD:

.. code-block:: python

>>> convert(amount=1, to=['SGD', 'EUR'])
{'SGD': 1.364903, 'EUR': 0.904506}



