---
url: https://docs.xendit.co/apidocs/generate-report
title: "Generate Report"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Balance & Transactions](/apidocs/introduction-1)
  - Reports

What information are you looking for?

Overview

Use ↑/↓ to navigate

[Quick setup](/apidocs/quick-setup)

[Rate limits](/apidocs/rate-limits)

[Webhook behavior](/apidocs/webhook-behavior)

Payments

Download API reference

[Introduction](/apidocs/introduction)

Payment Request

Payment

Payment Token

Session

Refund

Subscriptions

[Payment Link](/apidocs/payment-link)

[BI SNAP](/apidocs/bi-snap)

Payouts

Download API reference

[Introduction](/apidocs/payouts-introduction)

Payout

Cross-Border Payout

Balance & Transactions

Download API reference

[Introduction](/apidocs/introduction-1)

Balance

Reports

post

 [Generate Report](/apidocs/generate-report)

get

 [Get Report by ID](/apidocs/get-report)

post

 [Report webhook notification](/apidocs/report-webhook-notification)

Transaction

xenPlatform

Download API reference

[Introduction](/apidocs/accounts-misc-introduction)

xenPlatform

Webhook Settings

Others

Download API reference

[Introduction](/apidocs/others-introduction)

Customers

Bill Payments

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Generate Report

- Updated on Nov 26, 2025
- Published on Jul 24, 2025

 [Prev](/apidocs/get-balance "Get balance")  [Next](/apidocs/get-report "Get Report by ID") 

Post

/reports

Request this endpoint to generate the report. You can specify the type and filter the content of the report. The flow of this endpoint is asynchronous. Xendit will send callbacks to you after the report is done.

**Currency parameter usage:**

- If `type` is `BALANCE_HISTORY`, the `currency` field in the request body must be one of: IDR, PHP, USD, VND, THB, MYR, SGD, EUR, GBP, HKD, AUD.
- For all other report types, the `currency` field in the request body may be any applicable ISO 4217 currency code (e.g., IDR, PHP, USD, EUR, etc.).

Once the report is generated, you can use the get report endpoint to download the report file.

Security

HTTP

Type basic

API Key authentication using HTTPS Basic Auth.
Use your API key as the username. The password field can be left empty.
Note: In the API documentation "Try it" section, password is required, you may include any value.

Header parameters

for-user-id

string

The sub-account user-id that you want to make this transaction for.

This header is only used if you have access to xenPlatform. See xenPlatform for more information

Body parameters

application/json

Collapse all

object

type

string Required

The type of report that will be generated

Valid values[
"BALANCE\_HISTORY",
"TRANSACTIONS",
"UPCOMING\_TRANSACTIONS",
"DETAILED\_TRANSACTIONS"
]

filter

object (ReportFilter) Required

Filtering that are applied to report

The combination of `from` and `to` must be less than 92 days.

from

string (date-time) Required

The start time of the transaction to be filtered (ISO 8601)

Example2025-07-01T00:00:00Z

to

string (date-time) Required

The end time of the transaction to be filtered (ISO 8601)

Example2025-07-31T23:59:59Z

format

string

The format of the report. Available format is `CSV`.

Valid values[
"CSV"
]

Default"CSV"

currency

string

The currency to filter.

Valid values[
"IDR",
"PHP",
"USD",
"VND",
"THB",
"MYR",
"SGD",
"EUR",
"GBP",
"HKD",
"AUD"
]

Default"IDR"

report\_version

string

Report version indicates which version of report you need. This parameter is only applicable to Transaction Report and is request-only (not returned in response).

Version value <> changelog:
VERSION\_0: Original version
VERSION\_1: Includes Settlement Status, Actual Settlement Time, and Estimated Settlement Time
VERSION\_2: Includes Early Settlement Fee Columns, swapped Payment ID with Product ID

Valid values[
"VERSION\_0",
"VERSION\_1",
"VERSION\_2"
]

Default"VERSION\_0"

Responses

200

404

Show example

Successful operation

application/json

Basic Transaction Report
Complete Request

Basic Transaction Report

Code snippet

```
{
  "type": "TRANSACTIONS",
  "filter": {
    "from": "2025-07-01",
    "to": "2025-07-31T23:59:59Z"
  }
}
```

JSON

Copy

Complete Request

Code snippet

```
{
  "type": "DETAILED_TRANSACTIONS",
  "filter": {
    "from": "2025-07-01",
    "to": "2025-07-15T23:59:59Z"
  },
  "format": "CSV",
  "currency": "USD",
  "report_version": "VERSION_2"
}
```

JSON

Copy

Collapse all

object

id

string

Report ID

type

string

The type of report that will be generated

Valid values[
"BALANCE\_HISTORY",
"TRANSACTIONS",
"UPCOMING\_TRANSACTIONS",
"DETAILED\_TRANSACTIONS"
]

status

string

Valid values[
"PENDING",
"COMPLETED",
"FAILED"
]

filter

object (ReportFilter)

Filtering that are applied to report

The combination of `from` and `to` must be less than 92 days.

from

string (date-time)

The start time of the transaction to be filtered (ISO 8601)

Example2025-07-01T00:00:00Z

to

string (date-time)

The end time of the transaction to be filtered (ISO 8601)

Example2025-07-31T23:59:59Z

format

string

The format of the report. Available format is `CSV`.

Valid values[
"CSV"
]

Default"CSV"

currency

string

The currency to filter.

Valid values[
"IDR",
"PHP",
"USD",
"VND",
"THB",
"MYR",
"SGD",
"EUR",
"GBP",
"HKD",
"AUD"
]

Default"IDR"

business\_id

string

Unique ID generated by Xendit for the particular file

created

string

The time when the report request is created at UTC+0.

updated

string

The time when the report is updated at UTC+0.

report\_version

string

Report version indicates which version of report you need. This parameter is only applicable to Transaction Report and is request-only (not returned in response).

Version value <> changelog:
VERSION\_0: Original version
VERSION\_1: Includes Settlement Status, Actual Settlement Time, and Estimated Settlement Time
VERSION\_2: Includes Early Settlement Fee Columns, swapped Payment ID with Product ID

Valid values[
"VERSION\_0",
"VERSION\_1",
"VERSION\_2"
]

Default"VERSION\_0"

The provided `id` does not exist. Please review the `id` and try again

application/json

object

error\_code

string

Valid values[
"RATE\_LIMIT\_EXCEEDED"
]

message

string

errors

Array

OneOf

string

string

object

object

Was this article helpful?

Yes  No

Previous article

Get balance

Next article

Get Report by ID

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

for-user-id

Body

application/json

application/json

 

10

1

```
{
```

2

```
 "type": "BALANCE_HISTORY",
```

3

```
 "filter": {
```

4

```
  "from": "2025-07-01T00:00:00Z",
```

5

```
  "to": "2025-07-31T23:59:59Z"
```

6

```
 },
```

7

```
 "format": "CSV",
```

8

```
 "currency": "IDR",
```

9

```
 "report_version": "VERSION_0"
```

10

```
}
```

 Try it & see response

Response

Available responses

application/json

application/json

200404

 

```
  "from": "2025-07-01T00:00:00Z",
```