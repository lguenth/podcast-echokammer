#!/usr/bin/env python3

import twint

# Solve compatibility issues with notebooks and RunTime errors.
# import nest_asyncio
# nest_asyncio.apply()

# Configure
config = twint.Config()
config.Search = "Covid-19"
config.Lang = "de" # This language filter doesn't work.
config.Since = "2021-01-01"
config.Until = "2021-01-31"
config.Store_csv = True
config.Output = "test.csv"
# config.Pandas = True

# Run
twint.run.Search(config)
