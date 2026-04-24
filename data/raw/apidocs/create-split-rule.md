---
url: https://docs.xendit.co/apidocs/create-split-rule
title: "Create split rule"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [xenPlatform](/apidocs/accounts-misc-introduction)
  - [xenPlatform](/apidocs/create-account)

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

Transaction

xenPlatform

Download API reference

[Introduction](/apidocs/accounts-misc-introduction)

xenPlatform

post

 [Create account](/apidocs/create-account)

get

 [List accounts](/apidocs/list-accounts)

get

 [Get account](/apidocs/get-account)

pat

 [Update account](/apidocs/update-account)

post

 [Create split rule](/apidocs/create-split-rule)

post

 [Create account holder](/apidocs/create-account-holder)

get

 [Get account holder](/apidocs/get-account-holder)

pat

 [Update account holder](/apidocs/update-account-holder)

get

 [Get transfer by reference](/apidocs/get-transfer-by-reference)

post

 [Create transfers](/apidocs/create-transfers)

post

 [Owned account status webhook notification](/apidocs/owned-account-status-webhook-notification)

post

 [Managed account status webhook notification](/apidocs/managed-account-status-webhook-notification)

post

 [Account suspension webhook notification](/apidocs/account-suspension-webhook-notification)

post

 [Account holder KYC status notification webhook](/apidocs/account-holder-kyc-status-notification-webhook)

post

 [Account holder capabilities notification webhook](/apidocs/account-holder-capabilities-notification-webhook)

post

 [Split payment status notification webhook](/apidocs/split-payment-status-notification-webhook)

Webhook Settings

Others

Download API reference

[Introduction](/apidocs/others-introduction)

Customers

Bill Payments

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Create split rule

- Updated on Jan 8, 2026
- Published on Dec 6, 2024

 [Prev](/apidocs/update-account "Update account")  [Next](/apidocs/create-account-holder "Create account holder") 

Post

/split\_rules

A Split Rule object defines how payments in xenPlatform can be routed and split to multiple sub-accounts or the Master account.

Include the `split_rule_id` returned in the response in supported transaction endpoints to automatically route and split payments to multiple account destinations once payments settle.

Security

HTTP

Type basic

Body parameters

Show example

application/json

Code snippet

```
{
  "name": "Platform and Delivery Fees",
  "description": "Platform fee and delivery fee for a Marketplace",
  "routes": [
    {
      "flat_amount": 3000,
      "currency": "IDR",
      "destination_account_id": "5f8d0c0603ffe06b7d4d9fcf",
      "reference_id": "reference-1"
    },
    {
      "percent_amount": 5.25,
      "currency": "IDR",
      "destination_account_id": "5f8d0c0603ffe06b7d4d9fcf",
      "reference_id": "reference-2"
    }
  ]
}
```

JSON

Copy

Collapse all

object

name

string Required

Name to identify a split rule. Typically based on transaction and/or sub-merchant types and does not have to be unique. e.g. "standard platform fee and delivery fee", "commission"

description

string

Describes the purpose of the object

routes

Array of object (route) Required

object

Defines a single amount and destination within a split rule

flat\_amount

number

Amount of payments to be split, using a flat rate as a unit. This will be null if not applicable, and is required if `percent_amount` is null. All units must be a positive number

percent\_amount

number

Amount of payments to be split, using a percent rate as unit. This will be null if not applicable. This will be required if `flat_amount` is null All units must be a positive number, with decimals supported up to 2 decimal places. Percent amounts have to be between 0 and 100 Percent amounts are rounded off to the nearest monetary unit (e.g. 0.50 IDR will be rounded to 1 IDR; 0.49 IDR will be rounded to 0 IDR)

currency

string

ISO 4217 Currency Code

Valid values[
"IDR",
"PHP",
"VND",
"MYR",
"THB",
"SGD",
"USD"
]

destination\_account\_id

string

Business ID of the destination account where the amount is routed to.This could be the Business ID of your Master or Sub-account.

reference\_id

string

Reference ID which acts as an identifier of the route itself. This is used to distinguish in case one split rule has multiple routes of the same destinations.
Its value must be unique and case sensitive for every route object under the same Split Rule.

Responses

200

400

404

Show example

application/json

Code snippet

```
{
  "id": "splitru_d9e069f2-4da7-4562-93b7-ded87023d749",
  "name": "Standard platform fee",
  "description": "Platform fee for all transactions accepted on behalf of vendors",
  "routes": [
    {
      "flat_amount": 3000,
      "currency": "IDR",
      "destination_account_id": "5f8d0c0603ffe06b7d4d9fcf",
      "reference_id": "reference-1"
    },
    {
      "percent_amount": 5.25,
      "currency": "IDR",
      "destination_account_id": "5cafeb170a2b18519b1b8768",
      "reference_id": "reference-2"
    }
  ],
  "created": "2020-09-01T07:00:00.007Z",
  "updated": "2020-09-01T07:00:00.007Z",
  "metadata": {}
}
```

JSON

Copy

Collapse all

object

id

string

The unique Split Rule ID

name

string

Name to identify a split rule. Typically based on transaction and/or sub-merchant types and does not have to be unique. e.g. "standard platform fee and delivery fee", "commission"

description

string

Describes the purpose of the object

routes

Array of object (route)

object

Defines a single amount and destination within a split rule

flat\_amount

number

Amount of payments to be split, using a flat rate as a unit. This will be null if not applicable, and is required if `percent_amount` is null. All units must be a positive number

percent\_amount

number

Amount of payments to be split, using a percent rate as unit. This will be null if not applicable. This will be required if `flat_amount` is null All units must be a positive number, with decimals supported up to 2 decimal places. Percent amounts have to be between 0 and 100 Percent amounts are rounded off to the nearest monetary unit (e.g. 0.50 IDR will be rounded to 1 IDR; 0.49 IDR will be rounded to 0 IDR)

currency

string

ISO 4217 Currency Code

Valid values[
"IDR",
"PHP",
"VND",
"MYR",
"THB",
"SGD",
"USD"
]

destination\_account\_id

string

Business ID of the destination account where the amount is routed to.This could be the Business ID of your Master or Sub-account.

reference\_id

string

Reference ID which acts as an identifier of the route itself. This is used to distinguish in case one split rule has multiple routes of the same destinations.
Its value must be unique and case sensitive for every route object under the same Split Rule.

created

string (date-time)

Timestamp of when the object was created

updated

string (date-time)

Timestamp of when the object was updated

metadata

object (metadata)

Object of additional key-value pairs that the merchants may use like internal system parameters (business ID, shopping cart). User defines the JSON properties and values. You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long. Otherwise `NULL`

Show example

Validation error

application/json

API\_VALIDATION\_ERROR
INVALID\_FEE\_AMOUNT
DUPLICATE\_ERROR

API\_VALIDATION\_ERROR

Code snippet

```
{
  "error_code": "INVALID_CONFIGURATION",
  "message": "Inputs are failing validation. The errors field contains details about which fields are violating validation.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

INVALID\_FEE\_AMOUNT

Code snippet

```
{
  "error_code": "INVALID_FEE_AMOUNT",
  "message": "Fee amount and/or unit is negative number or incorrect format.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

DUPLICATE\_ERROR

Code snippet

```
{
  "error_code": "DUPLICATE_ERROR",
  "message": "Returned if provided `reference_id` is not unique for the routes",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

object

Inputs are failing validation. The errors field contains details about which fields are violating validation.

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR",
"INVALID\_CONFIGURATION",
"INVALID\_JSON\_FORMAT",
"TYPE\_AND\_CONFIGURATION\_CONFLICT",
"INVALID\_SOURCE\_OR\_DESTINATION\_ERROR",
"INSUFFICIENT\_BALANCE",
"INVALID\_FEE\_AMOUNT",
"DUPLICATE\_ERROR",
"INVALID\_AMOUNT",
"INSUFFICIENT\_ACCOUNT\_HOLDER\_DATA",
"MISMATCH\_PAYLOAD\_FOR\_REFERENCE",
"INVALID\_URL\_FORMAT"
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

Show example

Validation error

application/json

DESTINATION\_ACCOUNT\_NOT\_FOUND

DESTINATION\_ACCOUNT\_NOT\_FOUND

Code snippet

```
{
  "error_code": "DESTINATION_ACCOUNT_NOT_FOUND",
  "message": "Returned when destination_account_id is invalid or not connected to this xenPlatform account",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

object

The object being referenced does not exist

error\_code

string

Valid values[
"DESTINATION\_ACCOUNT\_NOT\_FOUND",
"DATA\_NOT\_FOUND",
"CALLBACK\_AUTHENTICATION\_TOKEN\_NOT\_FOUND\_ERROR"
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

Update account

Next article

Create account holder

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

Body

application/json

application/json

 

18

1

```
{
```

2

```
  "name": "Platform and Delivery Fees",
```

3

```
  "description": "Platform fee and delivery fee for a Marketplace",
```

4

```
  "routes": [
```

5

```
    {
```

6

```
      "flat_amount": 3000,
```

7

```
      "currency": "IDR",
```

8

```
      "destination_account_id": "5f8d0c0603ffe06b7d4d9fcf",
```

9

```
      "reference_id": "reference-1"
```

10

```
    },
```

11

```
    {
```

12

```
      "percent_amount": 5.25,
```

13

```
      "currency": "IDR",
```

14

```
      "destination_account_id": "5f8d0c0603ffe06b7d4d9fcf",
```

15

```
      "reference_id": "reference-2"
```

16

```
    }
```

17

```
  ]
```

18

```
}
```

 Try it & see response

Response

Available responses

application/json

application/json

200400404

 

```
 "created": "2026-04-23T07:10:02.407Z",
```