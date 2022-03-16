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
- For deprecated feaures removed in this release
### Fixed
- For any bug fixes


## [Unreleased] - 2022-03-04
Implement stock quoting


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