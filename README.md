# Clustering NBA Players 
> How many types of players are in the NBA and what five person combination of these player types is best?

The primary file is the notebook file cluster_nba_players.ipynb. It reads the final data file and steps through the process of analysis. The file get_nba_data.py is sloppily used for getting data from stats.nba.com. The file structure_nba_data.py reads in the data from the web scrape and structures it so it's ready for analysis.

![](header.png)

## Installation

Because the data set is not large I have included it ('data-(w_FGA).csv') in the files to be used in the Jupyter Notebook. If you are interested in how the data was gathered the three files get_nba_data.py, nba_urls.txt, and structure_nba_data.py were used. I'll give instructions on using those files later.

## Usage example

This analysis is a simple look into the roles of NBA players. It can be used and altered to explore other signals in the same or similar data sets. Thanks to NBA.com for the data.

## Development setup

None

## Release History

* 0.1.0
    * The first proper release

## Meta

Scott Siegel – [@scootsiegel](https://twitter.com/scootsiegel) 

Distributed under the MIT license. See ``LICENSE`` for more information.

[My Github](https://github.com/scootsiegel/)

## TODO
- [ ] Finish Appendix A (PCA) with further explanation, 3D plot, and conclusion.
- [ ] Do an Appendix B that explores weighting the features and comparing results.
- [ ] Add an Appendix C that uses DBScan (or another clustering alg) and compares results.
- [ ] Make the plots more robust so the groups of players is similar between plots. Currently it changes every time.
- [ ] Make the get_nba_data.py file robust to headers so it can be written to pull all data as an independent program.
- [ ] Once get_nba_data.py runs without error then make sure the entire pipeline runs without error.

