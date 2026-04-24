---
url: https://docs.xendit.co/apidocs/get-transfer-by-reference
title: "Get transfer by reference"
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

# Get transfer by reference

- Updated on Jan 8, 2026
- Published on Dec 6, 2024

 [Prev](/apidocs/update-account-holder "Update account holder")  [Next](/apidocs/create-transfers "Create transfers") 

Get

/transfers/reference={reference}

This endpoint queries the current status of a transfer. This is often used for checking the status of a transaction.

Security

HTTP

Type basic

Path parameters

reference

stringRequired

Examplemonthly\_transfers\_1234

Responses

200

400

401

Show example

application/json

Default Transfer

Default Transfer

Code snippet

```
{
  "created": "2020-11-30T02:47:53.061Z",
  "transfer_id": "bd1cc56b-ce7f-4ad7-8901-3eaa689e90eb",
  "source_user_id": "`5cafeb170a2b18519b1b8768",
  "destination_user_id": "5f8d0c0603ffe06b7d4d9fcf",
  "status": "SUCCESSFUL",
  "amount": "90000",
  "reference": "Monthly_Transfers_1234"
}
```

JSON

Copy

object

Object that would be generated upon creation of a Transfer

created

string (date-time)

Timestamp of when the object was created

transfer\_id

string

A unique reference for this Transfer set by Xendit systems

reference

string

A unique reference for this Transfer that you set when making the request

source\_user\_id

string

The source of the transfer. This is the user\_id of either your master or sub account

destination\_user\_id

string

The destination of the transfer. This is the `user_id` of either your master or sub account

status

string

The status of the Transfer. Available values `SUCCESSFUL`,`PENDING`, `FAILED`

amount

number

The amount that was transferred

Show example

application/json

DATA\_NOT\_FOUND

DATA\_NOT\_FOUND

Code snippet

```
{
  "error_code": "DATA_NOT_FOUND",
  "message": "Could not find transfer by reference because reference may be invalid.",
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

Show example

application/json

INVALID\_API\_KEY

INVALID\_API\_KEY

Code snippet

```
{
  "error_code": "INVALID_API_KEY",
  "message": "API key is not authorized for this API service, access to xenPlatform is needed",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

object

Invalid API key

error\_code

string

Valid values[
"INVALID\_API\_KEY"
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

Update account holder

Next article

Create transfers

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

reference \*

 Try it & see response

Response

Available responses

application/json

application/json

200400401

 

```
 "created": "2026-04-23T07:09:58.829Z",
```