---
url: https://docs.xendit.co/apidocs/simulate-payment-test-mode
title: "Simulate payment [test mode]"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payments](/apidocs/introduction)
  - [Payment Request](/apidocs/create-payment-request)

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

post

 [Create a payment request](/apidocs/create-payment-request)

post

 [Payment webhook notification](/apidocs/payment-webhook-notification)

get

 [Get the status of a payment request](/apidocs/get-payment-request)

post

 [Cancel a payment request](/apidocs/cancel-payment-request)

post

 [Simulate payment [test mode]](/apidocs/simulate-payment-test-mode)

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

Webhook Settings

Others

Download API reference

[Introduction](/apidocs/others-introduction)

Customers

Bill Payments

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Simulate payment [test mode]

- Updated on Apr 8, 2026
- Published on Jan 9, 2025

 [Prev](/apidocs/cancel-payment-request "Cancel a payment request")  [Next](/apidocs/get-payment "Get the status of a payment") 

Post

/v3/payment\_requests/{payment\_request\_id}/simulate

Simulate payment completion. Test-only endpoint for payment flow validation.

Security

HTTP

Type basic

Header parameters

api-version

string

Valid values[
"2024-11-11"
]

Path parameters

payment\_request\_id

stringRequired

Min length39

Max length39

Examplepr-8877c08a-740d-4153-9816-3d744ed197a5

Body parameters

application/json

object

amount

number

Amount to simulate.

Responses

200

500

Simulate payment for a Payment Request

application/json

object

status

string

Status of a simulation will always be `PENDING`

message

string

A simulated payment for the specified payment request id is being processed. You will be informed of the result via a webhook.

Internal server error

application/json

OneOf

Payments\_API\_Http500ServerError

object (Payments\_API\_Http500ServerError)

error\_code

string

Valid values[
"SERVER\_ERROR"
]

message

string

An unexpected error occured, our team has been notified and will troubleshoot the issue

Was this article helpful?

Yes  No

Previous article

Cancel a payment request

Next article

Get the status of a payment

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

payment\_request\_id \*

api-version 

2024-11-11 

-  2024-11-11

Body

application/json

application/json

 

3

1

```
{
```

2

```
 "amount": 1
```

3

```
}
```

 Try it & see response

Response

Available responses

application/json

application/json

200500

 

```
 "status": "string",
```