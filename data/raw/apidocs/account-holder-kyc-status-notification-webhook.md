---
url: https://docs.xendit.co/apidocs/account-holder-kyc-status-notification-webhook
title: "Account holder KYC status notification webhook"
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

# Account holder KYC status notification webhook

- Updated on Jan 8, 2026

 [Prev](/apidocs/account-suspension-webhook-notification "Account suspension webhook notification")  [Next](/apidocs/account-holder-capabilities-notification-webhook "Account holder capabilities notification webhook") 

Post

/your\_account\_holder\_kyc\_webhook\_url

These events will be sent when there is an update on a sub-account's KYC status

Body parameters

Show example

application/json

Account Holder KYC Callback

Account Holder KYC Callback

Code snippet

```
{
  "event": "account_holder.kyc.status",
  "created": "2021-01-01T10:00:00Z",
  "business_id": "5fe2b0137b7d62542fe6d7de",
  "data": {
    "id": "57fb4e076fa3fa296b7f5a97",
    "created": "2021-01-01T10:00:00Z",
    "updated": "2021-01-01T10:00:00Z",
    "kyc": {
      "status": "PASSED",
      "verified_at": "2021-01-01T10:00:00Z",
      "requested_at": "2021-01-01T10:00:00Z",
      "kyc_passed_at": "2021-01-01T10:00:00Z"
    }
  }
}
```

JSON

Copy

Collapse all

object

event

string

Event that occurred for this webhook

Valid values[
"account\_holder.kyc.status"
]

Exampleaccount\_holder.kyc.status

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

object

id

string

The unique ID of an Account Holder object

created

string

Timestamp of when the webhook was sent

updated

string

Timestamp of when the webhook was updated

kyc

object (account\_holder\_kyc\_response)

status

string

Valid values[
"PASSED",
"FAILED",
"RESUBMISSION\_REQUIRED"
]

requested\_at

string (date-time)

Timestamp of when the object was updated

kyc\_passed\_at

string (date-time)

Timestamp of when the object was updated

verified\_at

string (date-time)

Timestamp of when the object was updated

capabilities

Array of object (account\_holder\_capability\_response)

object

An object containing the details of the Account Holder capabilities activation process

type

string

channel\_code

string

status

string

Valid values[
"LIVE",
"VERIFICATION\_IN\_PROGRESS",
"RESUBMISSION\_REQUIRED",
"DECLINED"
]

failure\_reason

string

activated\_at

string (date-time)

Timestamp of when the object was updated

verified\_at

string (date-time)

Timestamp of when the object was updated

requested\_at

string (date-time)

Timestamp of when the object was updated

Responses

200

400

OK

Bad Request - Invalid webhook payload

Was this article helpful?

Yes  No

Previous article

Account suspension webhook notification

Next article

Account holder capabilities notification webhook

- Try It
- Code samples

Request

URL

Body

application/json

application/json

Account Holder KYC Callback

Account Holder KYC Callback

 Reset to default

 

16

1

```
{
```

2

```
  "event": "account_holder.kyc.status",
```

3

```
  "created": "2021-01-01T10:00:00Z",
```

4

```
  "business_id": "5fe2b0137b7d62542fe6d7de",
```

5

```
  "data": {
```

6

```
    "id": "57fb4e076fa3fa296b7f5a97",
```

7

```
    "created": "2021-01-01T10:00:00Z",
```

8

```
    "updated": "2021-01-01T10:00:00Z",
```

9

```
    "kyc": {
```

10

```
      "status": "PASSED",
```

11

```
      "verified_at": "2021-01-01T10:00:00Z",
```

12

```
      "requested_at": "2021-01-01T10:00:00Z",
```

13

```
      "kyc_passed_at": "2021-01-01T10:00:00Z"
```

14

```
    }
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