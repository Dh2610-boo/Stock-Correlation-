from vnstock import *

df1 = stock_historical_data("CEO", "2016-01-01", "2023-12-14", "1D", "stock")

# Save to local computer
# df1.to_csv("E:\BCTC các loại\CEO to test 2\price1.csv")

# Overview about company
overview = company_overview("CEO")

# Get news
info = company_news(symbol="CEO", page_size=10, page=0)

# Check insider deal
inside_deal = company_insider_deals(symbol="CEO", page_size=20, page=0)

# Check ratios:
basic_ratios = company_fundamental_ratio(symbol="CEO", mode="simplify", missing_pct=0.8)
financial_ratios = financial_ratio(symbol="CEO", report_range="yearly", is_all=False)
compare_ratios = financial_ratio_compare(
    symbol_ls=["CEO", "DXG"],
    industry_comparison=True,
    frequency="Quaterly",
    start_year=2013,
)

# Check correlation by quaterly (Ghép file thông qua Excel)
file = "E:\BCTC các loại\CEO to test\Touse.xlsx"
df2 = pd.read_excel(file, header=0)
head = df2.head()
print(head)
dftest = df2.drop("Time", axis=1)
corr = dftest.corr()
# corr.to_csv("E:\BCTC các loại\CEO to test 2\correlation.csv")
