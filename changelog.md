# Changelog
All notable changes to this project will be documented in this file using Semantic Versioning 2.0.0.


## [X.Y.Z] - yyyy-mm-dd
- X is Major
- Y is Minor
- Z is Patch
### Added
- New features
### Changed
- Changes in existing functionality
### Deprecated
- For once-stable features removed in upcoming releases
### Removed
- For deprecated features removed in this release
### Fixed
- For any bug fixes


## [1.6.4] - 2022-04-12
### Changed
- Look up stock quotes no longer uses Finnhub API function
- Quoting uses requests library to fetch stock information from Finnhub
### Fixed
- 403 Error when looking up stock quotes with Finnhub API function


## [1.6.3] - 2022-04-08
### Added
- Quoting functionality to look up daily stock information


## [1.6.2] - 2022-03-25
### Added
- import finnhub api with token


## [1.6.1] - 2022-03-18
### Added
- Heads or Tails function for some fun lottery plays


## [1.6.0] - 2022-03-11
### Added
- Created quote.py for finnhub stock quoting
- !sheesh function for fun
- randomize emoticons within sheesh function


## [1.5.3] - 2022-03-04
### Added 
- Download charts into /charts directory
- Charting( ) also deletes file after being sent to Discord
### Changed
- Send chart method changed from posting link to sending chart.png
### Fixed
- No longer displays link to chart from Finviz when a user tries to download or sees a notification from Discord


## [1.4.0] - 2022-03-03
Meeting with Project Advisor
### Added
- Send link to chart from Finviz with specified symbol into Discord chat
### Changed
- Commands begin with '!' instead of '$'
- !help message sent to chat instead of Discord DMs


## [1.3.0] - 2022-02-25
### Added
- chart.py for chart fetching function
### Changed
- Bot will send some messages as an embedded message for readability


## [1.2.1] - 2022-02-18
### Added
- bot.py for main bot functionality
### Changed
- Get stock information from any US market stock symbol with command
### Removed
- main.py removed to make Discord bot functions modular and readability
- Specific function for GME and AMC information fetch


## [1.1.0] - 2022-01-28
### Added
- Stock and options information fetch on 'GME' with command
### Changed
- Presentation of stock and options information with tabulate for readability


## [1.0.0] - 2022-01-14
### Added
- Stock information fetch on 'AMC' with command
- Options information fetch on 'AMC' with command


## [0.4.1] - 2021-12-20
### Added
- Basic Discord bot functionality of sending messages on command
- Import libaries for stock information


## [0.3.2] - 2021-12-17
### Added
- Discord command parsing
### Changed
- Initializing Discord client with Tickr Bot token


## [0.2.3] - 2021-11-26
### Added
- Tickr Bot created on Discord
- Tickr Bot token set as secret environment variable
- Discord bot linked to test channel


## [0.1.1] - 2021-10-29
### Added
- main.py created
- import discord