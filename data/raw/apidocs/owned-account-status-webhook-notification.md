---
url: https://docs.xendit.co/apidocs/owned-account-status-webhook-notification
title: "Owned account status webhook notification"
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

# Owned account status webhook notification

- Updated on Jan 8, 2026

 [Prev](/apidocs/create-transfers "Create transfers")  [Next](/apidocs/managed-account-status-webhook-notification "Managed account status webhook notification") 

Post

/your\_xenplatform\_owned\_webhook\_url

A webhook event sent when your `OWNED` sub-account has been successfully created

Body parameters

Show example

application/json

Account Created

Account Created

Code snippet

```
{
  "event": "account.created",
  "created": "2021-01-01T10:00:00Z",
  "data": {
    "id": "5cafeb170a2b18519b1b8761",
    "created": "2021-01-01T10:00:00Z",
    "updated": "2021-01-01T10:00:00Z",
    "type": "OWNED",
    "email": "test@xendit.co",
    "public_profile": {
      "business_name": "My Store"
    },
    "country": "ID",
    "status": "LIVE"
  }
}
```

JSON

Copy

Collapse all

object

event

string

Your `OWNED` sub-account has been successfully created

Valid values[
"account.created"
]

Exampleaccount.created

business\_id

string

ID of your Account, use this in the for-user-id header to create transactions on behalf of your Account

created

string

Timestamp of when the webhook was sent

updated

string

Timestamp of when the webhook was updated

data

object (CreateAccountResponseSchema)

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

Responses

200

400

OK

Bad Request - Invalid webhook payload

Was this article helpful?

Yes  No

Previous article

Create transfers

Next article

Managed account status webhook notification

- Try It
- Code samples

Request

URL

Body

application/json

application/json

Account Created

Account Created

 Reset to default

 

16

1

```
{
```

2

```
  "event": "account.created",
```

3

```
  "created": "2021-01-01T10:00:00Z",
```

4

```
  "data": {
```

5

```
    "id": "5cafeb170a2b18519b1b8761",
```

6

```
    "created": "2021-01-01T10:00:00Z",
```

7

```
    "updated": "2021-01-01T10:00:00Z",
```

8

```
    "type": "OWNED",
```

9

```
    "email": "test@xendit.co",
```

10

```
    "public_profile": {
```

11

```
      "business_name": "My Store"
```

12

```
    },
```

13

```
    "country": "ID",
```

14

```
    "status": "LIVE"
```

15

```
  }
```

16

```
}
```

 Try it & see response

Response

Available responses

200

 

```
null
```