---
url: https://docs.xendit.co/apidocs/refund-webhook-notification
title: "Refund webhook notification"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payments](/apidocs/introduction)
  - [Refund](/apidocs/refund-payment-request)

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

# Refund webhook notification

- Updated on Apr 8, 2026
- Published on Apr 9, 2025

 [Prev](/apidocs/refund-payment-request "Refund a payment request")  [Next](/apidocs/create-recurring-plan "Create Subscription Plan") 

Post

/your\_refund\_webhook\_url

Webhook notification that will be sent to your defined webhook url for updates to refund status.

Header parameters

x-callback-token

string

Your Xendit unique webhook token to verify the origin of the webhook. It is highly recommended for your integration to verify this value.

Body parameters

Refund status callback

Show example

application/json

Code snippet

```
{
  "refundSucceeded": {
    "value": {
      "event": "refund.succeeded",
      "business_id": "6094fa76c2fd53701b8e079c",
      "created": "2021-12-02T14:52:21.566Z",
      "data": {
        "event": "refund.succeeded",
        "business_id": "5f27a14a9bf05c73dd040bc8",
        "created": "2020-08-29T09:12:33.001Z",
        "data": {
          "id": "rfd-6f4a377d-a201-437f-9119-f8b00cbbe857",
          "payment_id": "ddpy-3cd658ae-25b9-4659-aa36-596ae41a809f",
          "invoice_id": null,
          "amount": 10000,
          "payment_method_type": "DIRECT_DEBIT",
          "channel_code": "BPI",
          "currency": "PHP",
          "status": "SUCCEEDED",
          "reason": "CANCELLATION",
          "reference_id": "b2756a1e-e6cd-4352-9a68-0483aa2b6a2",
          "failure_code": null,
          "refund_fee_amount": null,
          "created": "2020-08-30T09:12:33.001Z",
          "updated": "2020-08-30T09:12:33.001Z",
          "metadata": null
        }
      }
    }
  },
  "refundFailed": {
    "value": {
      "event": "refund.failed",
      "business_id": "6094fa76c2fd53701b8e079c",
      "created": "2021-12-02T14:52:21.566Z",
      "data": {
        "event": "refund.failed",
        "business_id": "5f27a14a9bf05c73dd040bc8",
        "created": "2020-08-29T09:12:33.001Z",
        "data": {
          "id": "rfd-fca8d8bc-497c-42a5-b16f-97825323502a",
          "payment_id": "ddpy-3cd658ae-25b9-4659-aa36-596ae41a809f",
          "invoice_id": null,
          "amount": 10000,
          "payment_method_type": "DIRECT_DEBIT",
          "channel_code": "BPI",
          "currency": "PHP",
          "status": "FAILED",
          "reason": "CANCELLATION",
          "reference_id": "b2756a1e-e6cd-4352-9a68-0483aa2b6a2",
          "failure_code": "DUPLICATE_ERROR",
          "refund_fee_amount": null,
          "created": "2020-08-30T09:12:33.001Z",
          "updated": "2020-08-30T09:12:33.001Z",
          "metadata": null
        }
      }
    }
  }
}
```

JSON

Copy

Collapse all

object

Refund status callback for refund

event

string

Webhook event names for payment capture status updates.

Valid values[
"refund.succeeded",
"refund.failed"
]

business\_id

string

Xendit-generated identifier for the business that owns the transaction

Example5f27a14a9bf05c73dd040bc8

created

string (date-time)

Timestamp of webhook delivery attempt in ISO 8601 date-time format.

Example2021-12-31T23:59:59Z

data

object (Payments\_API\_RefundSchema)

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

Responses

200

OK

Was this article helpful?

Yes  No

Previous article

Refund a payment request

Next article

Create Subscription Plan

- Try It
- Code samples

Request

URL

x-callback-token

Body

application/json

application/json

 

60

1

```
{
```

2

```
  "refundSucceeded": {
```

3

```
    "value": {
```

4

```
      "event": "refund.succeeded",
```

5

```
      "business_id": "6094fa76c2fd53701b8e079c",
```

6

```
      "created": "2021-12-02T14:52:21.566Z",
```

7

```
      "data": {
```

8

```
        "event": "refund.succeeded",
```

9

```
        "business_id": "5f27a14a9bf05c73dd040bc8",
```

10

```
        "created": "2020-08-29T09:12:33.001Z",
```

11

```
        "data": {
```

12

```
          "id": "rfd-6f4a377d-a201-437f-9119-f8b00cbbe857",
```

13

```
          "payment_id": "ddpy-3cd658ae-25b9-4659-aa36-596ae41a809f",
```

14

```
          "invoice_id": null,
```

15

```
          "amount": 10000,
```

16

```
          "payment_method_type": "DIRECT_DEBIT",
```

17

```
          "channel_code": "BPI",
```

18

```
          "currency": "PHP",
```

19

```
          "status": "SUCCEEDED",
```

20

```
          "reason": "CANCELLATION",
```

21

```
          "reference_id": "b2756a1e-e6cd-4352-9a68-0483aa2b6a2",
```

22

```
          "failure_code": null,
```

23

```
          "refund_fee_amount": null,
```

24

```
          "created": "2020-08-30T09:12:33.001Z",
```

 Try it & see response

Response

Available responses

200

 

```
null
```