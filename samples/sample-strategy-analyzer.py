from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.stratanalyzer import returns
from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import drawdown
import smacross_strategy

# Load the yahoo feed from the CSV file
feed = yahoofeed.Feed()
feed.addBarsFromCSV("orcl", "orcl-2000.csv")

# Evaluate the strategy with the feed's bars.
myStrategy = smacross_strategy.Strategy(feed, 20)

# Attach different analyzers to a strategy before executing it.
retAnalyzer = returns.ReturnsAnalyzer()
myStrategy.attachAnalyzer(retAnalyzer)
sharpeRatioAnalyzer = sharpe.SharpeRatio()
myStrategy.attachAnalyzer(sharpeRatioAnalyzer)
drawDownAnalyzer = drawdown.DrawDown()
myStrategy.attachAnalyzer(drawDownAnalyzer)

# Run the strategy.
myStrategy.run()

print "Final portfolio value: $%.2f" % myStrategy.getResult()
print "Cumulative returns: %.2f %%" % (retAnalyzer.getCumulativeReturn() * 100)
print "Sharpe ratio: %.2f" % (sharpeRatioAnalyzer.getSharpeRatio(0.05, 252))
print "Max. drawdown: %.2f %%" % (drawDownAnalyzer.getMaxDrawDown() * 100)
print "Max. drawdown duration: %d days" % (drawDownAnalyzer.getMaxDrawDownDuration())

