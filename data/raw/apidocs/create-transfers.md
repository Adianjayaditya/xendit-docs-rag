---
url: https://docs.xendit.co/apidocs/create-transfers
title: "Create transfers"
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

# Create transfers

- Updated on Jan 8, 2026
- Published on Dec 6, 2024

 [Prev](/apidocs/get-transfer-by-reference "Get transfer by reference")  [Next](/apidocs/owned-account-status-webhook-notification "Owned account status webhook notification") 

Post

/transfers

The Transfers API allows you to transfer balances: i) from your sub-accounts to your master account and vice versa, ii) between your sub-accounts. Use this to manage, or split payments between your platform and your sub accounts within the Xendit ecosystem.

> You can only create transfers using the Platform's API key. Sub-accounts that you manage through xenPlatform have no ability to create transfers through this endpoint

Security

HTTP

Type basic

Body parameters

application/json

object

reference

string Required

A unique reference for this Transfer that you set when making the request

amount

number Required

source\_user\_id

string Required

The source of the transfer. This is the user\_id of either your master or sub account

destination\_user\_id

string Required

The destination of the transfer. This is the `user_id` of either your master or sub account

Responses

200

400

401

403

425

Show example

application/json

Transfer

Transfer

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

API\_VALIDATION\_ERROR
INVALID\_JSON\_FORMAT
INVALID\_SOURCE\_OR\_DESTINATION\_ERROR
INSUFFICIENT\_BALANCE
MISMATCH\_PAYLOAD\_FOR\_REFERENCE
INVALID\_AMOUNT

API\_VALIDATION\_ERROR

Code snippet

```
{
  "error_code": "API_VALIDATION_ERROR",
  "message": "Inputs are failing validation. The errors field contains details about which fields are violating validation.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

INVALID\_JSON\_FORMAT

Code snippet

```
{
  "error_code": "INVALID_JSON_FORMAT",
  "message": "The request body is not a valid JSON format.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

INVALID\_SOURCE\_OR\_DESTINATION\_ERROR

Code snippet

```
{
  "error_code": "INVALID_SOURCE_OR_DESTINATION_ERROR",
  "message": "Source or destination account does not exist. Please input a valid business ID within your xenPlatform account.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

INSUFFICIENT\_BALANCE

Code snippet

```
{
  "error_code": "INSUFFICIENT_BALANCE",
  "message": "The cash balance of your source account is insufficient.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

MISMATCH\_PAYLOAD\_FOR\_REFERENCE

Code snippet

```
{
  "error_code": "MISMATCH_PAYLOAD_FOR_REFERENCE",
  "message": "Reference has been used before. If you'd like to retry this transfer, please use the same payload as your previous request.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

INVALID\_AMOUNT

Code snippet

```
{
  "error_code": "INVALID_AMOUNT",
  "message": "Transfer amount has to be greater than 0, Transfer amount of IDR currency should not have decimal point, Transfer amount of PHP currency can only have max 2 decimal point.",
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

INVALID\_API\_KEY

INVALID\_API\_KEY

Code snippet

```
{
  "error_code": "INVALID_API_KEY",
  "message": "The API key format is invalid",
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

Show example

application/json

REQUEST\_FORBIDDEN\_ERROR
DUPLICATE\_REFERENCE
XEN\_PLATFORM\_SUB\_ACCOUNT\_NOT\_LIVE
API\_KEY\_ENVIRONMENT\_NOT\_MATCH

REQUEST\_FORBIDDEN\_ERROR

Code snippet

```
{
  "error_code": "REQUEST_FORBIDDEN_ERROR",
  "message": "API key in use does not have necessary permissions to perform the request. Please assign proper permissions for the key",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

DUPLICATE\_REFERENCE

Code snippet

```
{
  "error_code": "DUPLICATE_REFERENCE",
  "message": "The reference parameter should be unique.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

XEN\_PLATFORM\_SUB\_ACCOUNT\_NOT\_LIVE

Code snippet

```
{
  "error_code": "XEN_PLATFORM_SUB_ACCOUNT_NOT_LIVE",
  "message": "Your source or destination account is not live yet. Please specify live accounts for live transfers.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

API\_KEY\_ENVIRONMENT\_NOT\_MATCH

Code snippet

```
{
  "error_code": "API_KEY_ENVIRONMENT_NOT_MATCH",
  "message": "Use your LIVE API key to transfer between LIVE accounts, or use TEST API key to transfer between TEST accounts.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

object

Forbidden request

error\_code

string

Valid values[
"REQUEST\_FORBIDDEN\_ERROR",
"FEATURE\_NOT\_ACTIVATED",
"DUPLICATE\_REFERENCE",
"XEN\_PLATFORM\_SUB\_ACCOUNT\_NOT\_LIVE",
"API\_KEY\_ENVIRONMENT\_NOT\_MATCH",
"CHANNEL\_ACTIVATION\_IN\_PROGRESS",
"CHANNEL\_HAS\_BEEN\_ACTIVATED",
"KYC\_VERIFICATION\_IN\_PROGRESS"
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

TRANSFER\_IN\_PROGRESS

TRANSFER\_IN\_PROGRESS

Code snippet

```
{
  "error_code": "TRANSFER_IN_PROGRESS",
  "message": "Transfer is currently being processed. Use `GET Transfer By Reference` to check its latest status",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

object

Transfer is currently being processed. Use GET Transfer By Reference to check its latest status

error\_code

string

Valid values[
"TRANSFER\_IN\_PROGRESS"
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

Get transfer by reference

Next article

Owned account status webhook notification

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

 

6

1

```
{
```

2

```
 "reference": "string",
```

3

```
 "amount": 1,
```

4

```
 "source_user_id": "string",
```

5

```
 "destination_user_id": "string"
```

6

```
}
```

 Try it & see response

Response

Available responses

application/json

application/json

200400401403425

 

```
 "created": "2026-04-23T07:10:41.456Z",
```