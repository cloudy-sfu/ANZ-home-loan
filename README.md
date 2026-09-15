# ANZ home loan
Predict ANZ New Zealand home loan‘s interest rate

![](https://shields.io/badge/dependencies-Python_3.14-blue)
![](https://shields.io/badge/dependencies-PowerShell_7-navy)

## Install

Create a Python virtual environment and activate.

Create `.env` file and define the following environment variables. [Format](https://github.com/env-lang/env/blob/main/env.md)

| Variable | Description                         |
| -------- | ----------------------------------- |
| NEON_DB  | Connection string to Neon database. |

### Database

Create a [Neon](https://neon.com/) PostgreSQL 18.3 database. "Settings > Compute defaults > Scale to zero" must keep default (5 minutes) or longer.

Setup the database schema by `database_schema.sql`.

>   [!note]
>
>   Any other PostgreSQL database release may work, but is not tested. If using other database, replace the [connection string](https://neon.com/docs/connect/connect-from-any-app) to Neon database by the [connection string](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING) to your own PostgreSQL database.

### GitHub Actions

Deploy this program in GitHub and enable GitHub Actions for this repository. Manually run each scheduled job once, to initially save data into database and ensure all the GitHub Actions are active.

Add environment variables into GitHub repository settings "Secrets and variables > Actions > Secrets > Repository secrets".

### Historical mortgage interest rate

>   Acknowledgement & dependency: https://github.com/simonbetton/ratesapi.nz

To collect historical mortgage interest rate one-off since 2025-03-08, run the following command **with arguments** in PowerShell.

```
.\set_env.ps1
python get_data/ins_mortgage_rate_historical.py
```

Arguments of `get_data/ins_mortgage_rate_historical.py`

| Name           | Required? | Description                                                  |
| -------------- | --------- | ------------------------------------------------------------ |
| `--start_date` | ✓         | The first day (inclusive) of missing data, which must be no earlier than 2025-03-08. |
| `--end_date`   | ✓         | The last day (inclusive) of missing data.                    |



## Usage

