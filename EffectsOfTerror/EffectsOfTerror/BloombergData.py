# This program exports a finction which extracts Bloomberg data from csv files
# containing details regarding specific entries

def getData():
    migration = []
    for line in open("./bloombergSecurities/MigrationData.txt"):
        terms = line[0:-1].split(",")
        migration.append(terms)

    risk = []
    for line in open("./bloombergSecurities/RiskData.txt"):
        terms = line[0:-1].split(",")
        risk.append(terms)

    stocks = []
    for line in open("./bloombergSecurities/StockIndexData.txt"):
        terms = line[0:-1].split(",")
        stocks.append(terms)

    bonds = []
    for line in open("./bloombergSecurities/BondsData.txt"):
        terms = line[0:-1].split(",")
        bonds.append(terms)

    return {
            "migration":migration,
            "risk":risk,
            "stocks":stocks,
            "bonds":bonds
            }
