---
url: https://docs.xendit.co/apidocs/refund-payment-request
title: "Refund a payment request"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payments](/apidocs/introduction)
  - Refund

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

post

 [Refund a payment request](/apidocs/refund-payment-request)

post

 [Refund webhook notification](/apidocs/refund-webhook-notification)

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

# Refund a payment request

- Updated on Apr 8, 2026
- Published on Feb 13, 2025

 [Prev](/apidocs/webhook-notification-sent-defined-webhook-url-updates-payment-session "Webhook notification that will be sent to your defined webhook url for updates to payment session status.")  [Next](/apidocs/refund-webhook-notification "Refund webhook notification") 

Post

/refunds

Initiate a refund for a given successful payment request.

Security

HTTP

Type basic

Header parameters

for-user-id

string

The XenPlatform subaccount user id that will perform this transaction.

Body parameters

Show example

application/json

Refund\_With\_Amount
Refund\_Without\_Amount

Refund\_With\_Amount

Code snippet

```
{
  "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
  "payment_request_id": "pr-90392f42-d98a-49ef-a7f3-abcezas123",
  "currency": "IDR",
  "amount": 10000,
  "reason": "REQUESTED_BY_CUSTOMER"
}
```

JSON

Copy

Refund\_Without\_Amount

Code snippet

```
{
  "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
  "payment_request_id": "pr-90392f42-d98a-49ef-a7f3-abcezas123",
  "reason": "REQUESTED_BY_CUSTOMER"
}
```

JSON

Copy

Collapse all

object

Create refund API request body

payment\_request\_id

string Required

Xendit unique Payment Request ID generated as reference after creation of payment request.

Examplepr-1102feb0-bb79-47ae-9d1e-e69394d3949c

reference\_id

string

A Reference ID from merchants to identify their request.

Min length1

Max length255

currency

string

ISO 4217 three-letter currency code for the payment.

Valid values[
"IDR",
"PHP",
"VND",
"THB",
"SGD",
"MYR",
"USD",
"HKD",
"AUD",
"GBP",
"EUR",
"JPY",
"MXN"
]

ExampleIDR

amount

number

The intended payment amount to be refunded to the end user.

Minimum0.0

Example10000.0

reason

string Required

Status of the refund.

Valid values[
"FRAUDULENT",
"DUPLICATE",
"REQUESTED\_BY\_CUSTOMER",
"CANCELLATION",
"OTHERS"
]

metadata

object (Payments\_API\_MerchantMetadata)

Key-value entries for your custom data.
You can specify up to 50 keys, with key names up to 40 characters and values up to 500 characters.
This is for your convenience. Xendit will not use this data for any processing.

Example{
"my\_custom\_id": "merchant-123",
"my\_custom\_order\_id": "order-123"
}

Responses

200

400

403

404

500

503

Refund is pending. Check the final status of the refund via webhook.

application/json

Collapse all

object

Refund object

id

string

Xendit unique Refund ID generated as reference after creation of refund.

Examplerfd-69e77490-d2cc-4bf3-8319-e064e121db93

payment\_request\_id

string

Xendit unique Payment Request ID generated as reference after creation of payment request.

Examplepr-1102feb0-bb79-47ae-9d1e-e69394d3949c

payment\_id

string

To be deprecated. Xendit unique Payment ID generated as reference for a payment.

Examplepy-1402feb0-bb79-47ae-9d1e-e69394d3949c

invoice\_id

string

To be deprecated. Xendit unique Invoice ID generated as reference after creation of an invoice or payment link.

Example65fc7522ff846905c2fc1c8d

payment\_method\_type

string

To be deprecated. Type of the payment method used in the original payment.'

Valid values[
"CARD",
"EWALLET",
"DIRECT\_DEBIT"
]

reference\_id

string

A Reference ID from merchants to identify their request.

Min length1

Max length255

channel\_code

string

Channel code used to select the payment method provider.

currency

string

ISO 4217 three-letter currency code for the payment.

Valid values[
"IDR",
"PHP",
"VND",
"THB",
"SGD",
"MYR",
"USD",
"HKD",
"AUD",
"GBP",
"EUR",
"JPY",
"MXN"
]

ExampleIDR

amount

number

The intended payment amount to be refunded to the end user.

Minimum0.0

Example10000.0

status

string

Status of the refund.

Valid values[
"SUCCEEDED",
"FAILED",
"PENDING",
"CANCELLED"
]

reason

string

Status of the refund.

Valid values[
"FRAUDULENT",
"DUPLICATE",
"REQUESTED\_BY\_CUSTOMER",
"CANCELLATION",
"OTHERS"
]

failure\_code

string

Reasons of the refund failure.

Valid values[
"ACCOUNT\_ACCESS\_BLOCKED",
"ACCOUNT\_NOT\_FOUND",
"DUPLICATE\_ERROR",
"INSUFFICIENT\_BALANCE",
"REFUND\_FAILED"
]

refund\_fee\_amount

number

Fee for processing the refund

metadata

object (Payments\_API\_MerchantMetadata)

Key-value entries for your custom data.
You can specify up to 50 keys, with key names up to 40 characters and values up to 500 characters.
This is for your convenience. Xendit will not use this data for any processing.

Example{
"my\_custom\_id": "merchant-123",
"my\_custom\_order\_id": "order-123"
}

created

string (date-time)

ISO 8601 date-time format.

Example2021-12-31T23:59:59Z

updated

string (date-time)

ISO 8601 date-time format.

Example2021-12-31T23:59:59Z

Bad request

application/json

OneOf

Payments\_API\_Http400InvalidValueError

object (Payments\_API\_Http400InvalidValueError)

error\_code

string

Valid values[
"INVALID\_VALUE\_ERROR"
]

message

string

Values in the payment request is not within expected range or expected configurations. Check the specific error message for debugging.

Payments\_API\_Http400ApiValidationError

object (Payments\_API\_Http400ApiValidationError)

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR"
]

message

string

Fields or values in the payment request does not comply with our API specification. Check the specific error message for debugging.

Payments\_API\_Http400RefundAmountExceeded

object (Payments\_API\_Http400RefundAmountExceeded)

error\_code

string

Valid values[
"REFUND\_AMOUNT\_EXCEEDED"
]

message

string

Refund amount specified in refund request must be less than or equal to unrefunded capture amount.

Payments\_API\_Http400TemporarilyUnavailable

object (Payments\_API\_Http400TemporarilyUnavailable)

error\_code

string

Valid values[
"TEMPORARILY\_UNAVAILABLE"
]

message

string

Requested feature is unavailable during this timing.

Payments\_API\_Http400RefundInProgress

object (Payments\_API\_Http400RefundInProgress)

error\_code

string

Valid values[
"REFUND\_IN\_PROGRESS"
]

message

string

Please wait for the pending refund request to be completed before initiating a new one.

Payments\_API\_Http400IneligibleTransactionStatus

object (Payments\_API\_Http400IneligibleTransactionStatus)

error\_code

string

Valid values[
"INELIGIBLE\_TRANSACTION\_STATUS"
]

message

string

Feature is not allowed for the payment request because of its current status. Check the specific error message for debugging.

Payments\_API\_Http400InsufficientBalance

object (Payments\_API\_Http400InsufficientBalance)

error\_code

string

Valid values[
"INSUFFICIENT\_BALANCE"
]

message

string

There is insufficient balance in your account to perform a refund. Please top up your balance with a sufficient amount before retrying the refund.

Payments\_API\_Http400PartialRefundCountsExceeded

object (Payments\_API\_Http400PartialRefundCountsExceeded)

error\_code

string

Valid values[
"PARTIAL\_REFUND\_COUNTS\_EXCEEDED"
]

message

string

Number of partial refunds for this payment request has exceeded what is allowed by payment channel. Please check our documentations for refund limitations.

Forbidden

application/json

OneOf

Payments\_API\_Http403Skip3dsForbidden

object (Payments\_API\_Http403Skip3dsForbidden)

error\_code

string

Valid values[
"SKIP\_3DS\_FORBIDDEN"
]

message

string

Non 3DS payment request for cards is not allowed. Please activate the feature on Xendit dashboard before proceeding.

Payments\_API\_Http403InvalidMerchantSettings

object (Payments\_API\_Http403InvalidMerchantSettings)

error\_code

string

Valid values[
"INVALID\_MERCHANT\_SETTINGS"
]

message

string

Merchant credentials met with an error with the provider. Please contact Xendit customer support to resolve this issue.

Payments\_API\_Http403RefundNotSupported

object (Payments\_API\_Http403RefundNotSupported)

error\_code

string

Valid values[
"REFUND\_NOT\_SUPPORTED"
]

message

string

Refund feature is not available for this payment channel.

Payments\_API\_Http403PartialRefundNotSupported

object (Payments\_API\_Http403PartialRefundNotSupported)

error\_code

string

Valid values[
"PARTIAL\_REFUND\_NOT\_SUPPORTED"
]

message

string

Partial Refund feature is not available for this payment channel.

Not found

application/json

OneOf

Payments\_API\_Http404DataNotFound

object (Payments\_API\_Http404DataNotFound)

error\_code

string

Valid values[
"DATA\_NOT\_FOUND"
]

message

string

ID specified in request cannot be found.

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

Service unavailable

application/json

OneOf

Payments\_API\_Http503ChannelUnavailable

object (Payments\_API\_Http503ChannelUnavailable)

error\_code

string

Valid values[
"CHANNEL\_UNAVAILABLE"
]

message

string

The channel requested is currently experiencing unexpected issues. The provider will be notified to resolve this issue.

Was this article helpful?

Yes  No

Previous article

Webhook notification that will be sent to your defined webhook url for updates to payment session status.

Next article

Refund webhook notification

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

for-user-id

Body

application/json

application/json

Refund\_With\_Amount

Refund\_With\_Amount

Refund\_Without\_Amount

 Reset to default

 

7

1

```
{
```

2

```
  "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
```

3

```
  "payment_request_id": "pr-90392f42-d98a-49ef-a7f3-abcezas123",
```

4

```
  "currency": "IDR",
```

5

```
  "amount": 10000,
```

6

```
  "reason": "REQUESTED_BY_CUSTOMER"
```

7

```
}
```

 Try it & see response

Response

Available responses

application/json

application/json

200400403404500503

 

```
 "payment_request_id": "pr-1102feb0-bb79-47ae-9d1e-e69394d3949c",
```