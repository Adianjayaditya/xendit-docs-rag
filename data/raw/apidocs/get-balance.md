---
url: https://docs.xendit.co/apidocs/get-balance
title: "Get balance"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Balance & Transactions](/apidocs/introduction-1)
  - Balance

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

get

 [Get balance](/apidocs/get-balance)

Reports

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

# Get balance

- Updated on Nov 26, 2025
- Published on Jul 24, 2025

 [Prev](/apidocs/introduction-1 "Introduction")  [Next](/apidocs/generate-report "Generate Report") 

Get

/balance

Balance is like your wallet since it will tell you how much money is available to you on Xendit. You can retrieve it to see the current balance on your Xendit cash account. Your balance is debited on any money out transaction, e.g. when performing disbursements or Xendit fees are charged. Your balance is credited when money comes into your account.

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

Query parameters

account\_type

string

The selected balance type

Valid values[
"CASH",
"HOLDING"
]

Default"CASH"

at\_timestamp

string (date-time)

ISO 8601 date-time format (URI encoded)

Balance returned in the response will be based on the timestamp provided.
The timestamp value must be URI encoded when passed as a query parameter.

Example2024-01-01T00:00:00Z

currency

string

Currency filter for customers with multi-currency accounts. Only the following currencies are supported for balance and balance history:

- IDR, PHP, USD, VND, THB, MYR, SGD, EUR, GBP, HKD, AUD

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

Responses

200

400

Successful operation

application/json

object

balance

integer (float)

Example1241231

Inputs are failing validation. The errors field contains details about which fields are violating validation.

application/json

object

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR",
"FEATURE\_NOT\_AVAILABLE"
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

Introduction

Next article

Generate Report

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

account\_type 

CASH 

-  CASH  HOLDING

at\_timestamp

currency 

- 

-  IDR  PHP  USD  VND  THB  MYR  SGD  EUR  GBP  HKD  AUD

for-user-id

 Try it & see response

Response

Available responses

application/json

application/json

200400

 

```
 "balance": 1241231
```