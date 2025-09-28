# Data Context (Fill Me In)

Describe your datasets, databases, and systems here so the agent can work correctly.

## Datasets
- `data/sample/sales.csv`: demo dataset with columns: date, region, product, quantity, price

## Databases
- (Example) `SalesDW` — SQL Server; tables: `Sales`, `Customers`, `Products`. Connection via ODBC DSN `SalesDW`.
  - KPIs: GM%, ASP, QTD, YTD, MoM.

## KPIs & Business Rules
- GM%: (Revenue - Cost)/Revenue. Confirm cost source before use.
- ASP: mean price excluding returns.

Update this file as your environment grows. The agent will read it at startup.
