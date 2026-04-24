---
url: https://docs.xendit.co/apidocs/split-payment-status-notification-webhook
title: "Split payment status notification webhook"
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

# Split payment status notification webhook

- Updated on Jan 8, 2026
- Published on Aug 21, 2025

 [Prev](/apidocs/account-holder-capabilities-notification-webhook "Account holder capabilities notification webhook")  [Next](/apidocs/set-webhook-url "Set webhook URL") 

Post

/your\_split\_payment\_webhook\_url

These events will be sent when a split payment is completed or has failed to execute

Body parameters

Show example

application/json

Split Payment Completed
Split Payment Failed

Split Payment Completed

Code snippet

```
{
  "event": "split.payment",
  "created": "2021-01-01T10:00:00Z",
  "business_id": "5fe2b0137b7d62542fe6d7de",
  "data": {
    "id": "57fb4e076fa3fa296b7f5a97",
    "split_rule_id": "splitru_d9e069f2-4da7-4562-93b7-ded87023d749",
    "reference_id": "my_unique_route_reference_12345",
    "payment_id": "py-1402feb0-bb79-47ae-9d1e-e69394d3949c",
    "payment_reference_id": "my_unique_payment_reference_12345",
    "source_account_id": "5fe2b0137b7d62542fe6d7de",
    "destination_account_id": "67514ce3b045c2ebade1d94e",
    "status": "COMPLETED",
    "amount": 150.45,
    "currency": "PHP"
  }
}
```

JSON

Copy

Split Payment Failed

Code snippet

```
{
  "event": "split.payment",
  "created": "2021-01-01T10:00:00Z",
  "business_id": "5fe2b0137b7d62542fe6d7de",
  "data": {
    "id": "57fb4e076fa3fa296b7f5a97",
    "split_rule_id": "splitru_d9e069f2-4da7-4562-93b7-ded87023d749",
    "reference_id": "my_unique_route_reference_12345",
    "payment_id": "py-1402feb0-bb79-47ae-9d1e-e69394d3949c",
    "payment_reference_id": "my_unique_payment_reference_12345",
    "source_account_id": "5fe2b0137b7d62542fe6d7de",
    "destination_account_id": "67514ce3b045c2ebade1d94e",
    "status": "FAILED",
    "amount": 150.45,
    "currency": "PHP",
    "failure_code": "INSUFFICIENT_BALANCE"
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
"split.payment"
]

Examplesplit.payment

business\_id

string

ID of your Account, use this in the for-user-id header to create transactions on behalf of your Account

created

string

Timestamp of when the webhook was sent

data

object

id

string

The unique Split Payment ID created for every split

split\_rule\_id

string

The unique Split Rule ID

reference\_id

string

Reference ID which acts as an identifier of the route itself. This is used to distinguish in case one split rule has multiple routes of the same destinations.
Its value must be unique and case sensitive for every route object under the same Split Rule.

payment\_id

string

The original payment ID that the Split payment was processed for, or that the Split Rule was linked to using the with-split-rule header.
The payment ID is the unique identifier for the payment. Its prefix varies based on the payment method type.

payment\_reference\_id

string

Reference ID of the Payment object

source\_account\_id

string

Business ID of the account where the split was sent from. This is also the account that received the original payment.

destination\_account\_id

string

Business ID of the destination account where the amount is routed to.This could be the Business ID of your Master or Sub-account.

status

string

The status of the split payment.

Valid values[
"COMPLETED",
"FAILED"
]

amount

number

The total currency amount that is sent to the destination\_account\_id

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

failure\_code

string

The failure code for FAILED events

ExampleINSUFFICIENT\_BALANCE

Responses

200

400

OK

Bad Request - Invalid webhook payload

Was this article helpful?

Yes  No

Previous article

Account holder capabilities notification webhook

Next article

Set webhook URL

- Try It
- Code samples

Request

URL

Body

application/json

application/json

Split Payment Completed

Split Payment Completed

Split Payment Failed

 Reset to default

 

17

1

```
{
```

2

```
  "event": "split.payment",
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
    "split_rule_id": "splitru_d9e069f2-4da7-4562-93b7-ded87023d749",
```

8

```
    "reference_id": "my_unique_route_reference_12345",
```

9

```
    "payment_id": "py-1402feb0-bb79-47ae-9d1e-e69394d3949c",
```

10

```
    "payment_reference_id": "my_unique_payment_reference_12345",
```

11

```
    "source_account_id": "5fe2b0137b7d62542fe6d7de",
```

12

```
    "destination_account_id": "67514ce3b045c2ebade1d94e",
```

13

```
    "status": "COMPLETED",
```

14

```
    "amount": 150.45,
```

15

```
    "currency": "PHP"
```

16

```
  }
```

17

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