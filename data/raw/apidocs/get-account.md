---
url: https://docs.xendit.co/apidocs/get-account
title: "Get account"
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

# Get account

- Updated on Jan 8, 2026
- Published on Dec 6, 2024

 [Prev](/apidocs/list-accounts "List accounts")  [Next](/apidocs/update-account "Update account") 

Get

/v2/accounts/{id}

The Get Account API allows you to retrieve a sub-account's information.

Security

HTTP

Type basic

Path parameters

id

stringRequired

Example5cafeb170a2b18519b1b8761

Responses

200

404

Show example

application/json

Owned Sub-account

Owned Sub-account

Code snippet

```
{
  "id": "5cafeb170a2b18519b1b8761",
  "created": "2021-01-01T10:00:00Z",
  "updated": "2021-01-01T10:00:00Z",
  "type": "OWNED",
  "email": "angie@pinkpanther.com",
  "public_profile": {
    "business_name": "Angie's lemonade stand"
  },
  "status": "LIVE"
}
```

JSON

Copy

Collapse all

object

id

string

ID of your Account, use this in the for-user-id header to create transactions on behalf of your Account

created

string (date-time)

Timestamp of when the object was created

updated

string (date-time)

Timestamp of when the object was updated

type

string

The type of account created

Valid values[
"MANAGED",
"OWNED"
]

email

string (email)

A valid email address associated with the object

Max length255

Exampletest@example.co

public\_profile

object (public\_profile)

business\_name

string

Public name of the account.

description

string

Additional description visible publicly.

country

string

The country (based on ISO 3166-1 Alpha-2) of incorporation for a business, or the country of residence for an individual.

Valid values[
"ID",
"PH",
"VN",
"MY",
"TH"
]

status

string

Status of the Account you are creating.

Valid values[
"INVITED",
"REGISTERED",
"AWAITING\_DOCS",
"PENDING\_VERIFICATION",
"LIVE",
"SUSPENDED"
]

Show example

Not found error

application/json

DATA\_NOT\_FOUND

DATA\_NOT\_FOUND

Code snippet

```
{
  "error_code": "DATA_NOT_FOUND",
  "message": "Could not find payout with the corresponding ID. Please try again with a valid ID.",
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

List accounts

Next article

Update account

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

id \*

 Try it & see response

Response

Available responses

application/json

application/json

200404

 

```
 "created": "2026-04-23T07:10:12.023Z",
```