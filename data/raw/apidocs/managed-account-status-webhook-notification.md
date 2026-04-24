---
url: https://docs.xendit.co/apidocs/managed-account-status-webhook-notification
title: "Managed account status webhook notification"
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

# Managed account status webhook notification

- Updated on Jan 8, 2026

 [Prev](/apidocs/owned-account-status-webhook-notification "Owned account status webhook notification")  [Next](/apidocs/account-suspension-webhook-notification "Account suspension webhook notification") 

Post

/your\_xenplatform\_managed\_webhook\_url

Webhook events sent for your `MANAGED` sub-accounts when they have registered or are activated.

Body parameters

Show example

application/json

Account Registered
Account Activated

Account Registered

Code snippet

```
{
  "event": "account.registered",
  "created": "2021-01-01T10:00:00Z",
  "data": {
    "user_id": "5cafeb170a2b18519b1b8761",
    "account_info": {
      "payments_enabled": false
    }
  }
}
```

JSON

Copy

Account Activated

Code snippet

```
{
  "event": "account.activated",
  "created": "2021-01-01T10:00:00Z",
  "master_acc_business_id": "5cafeb170a2b18529b6120a4",
  "data": {
    "user_id": "5cafeb170a2b18519b1b8761",
    "created": "2021-01-01T10:00:00Z",
    "account_info": {
      "payments_enabled": true
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

`account.registered`: Your `MANAGED` sub-account has successfully registered
`account.activated`: Your `MANAGED` sub-account has been verified and enabled for live payments

Valid values[
"account.registered",
"account.activated"
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

object (AccountCallbackDataSchema)

user\_id

string

The sub-account business ID

account\_info

object

payments\_enabled

boolean

Indicates whether live payments are enabled for the account

Responses

200

400

OK

Bad Request - Invalid webhook payload

Was this article helpful?

Yes  No

Previous article

Owned account status webhook notification

Next article

Account suspension webhook notification

- Try It
- Code samples

Request

URL

Body

application/json

application/json

Account Registered

Account Registered

Account Activated

 Reset to default

 

10

1

```
{
```

2

```
  "event": "account.registered",
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
    "user_id": "5cafeb170a2b18519b1b8761",
```

6

```
    "account_info": {
```

7

```
      "payments_enabled": false
```

8

```
    }
```

9

```
  }
```

10

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