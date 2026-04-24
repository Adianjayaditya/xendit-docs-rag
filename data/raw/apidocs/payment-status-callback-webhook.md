---
url: https://docs.xendit.co/apidocs/payment-status-callback-webhook
title: "Payment Status Callback (Webhook)"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Others](/apidocs/others-introduction)
  - [Bill Payments](/apidocs/get-product-list)
  - [Payments](/apidocs/create-payment)

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

Webhook Settings

Others

Download API reference

[Introduction](/apidocs/others-introduction)

Customers

Bill Payments

Products

Inquiry

Payments

post

 [Create Payment](/apidocs/create-payment)

get

 [Get Payment Detail](/apidocs/get-payment-detail)

post

 [Payment Status Callback (Webhook)](/apidocs/payment-status-callback-webhook)

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Payment Status Callback (Webhook)

- Updated on Apr 1, 2026
- Published on Aug 8, 2025

 [Prev](/apidocs/get-payment-detail "Get Payment Detail")  [Next](/apidocs/get-file-by-id "Get file by ID") 

Post

/bill-payments/your-callback-url

Callback endpoint that Xendit will POST to your configured webhook URL when payment status updates occur.
This endpoint should be implemented by your server to receive payment notifications.

Header parameters

X-Callback-Signature

stringRequired

HMAC SHA256 signature for webhook verification

X-Callback-Timestamp

stringRequired

Unix timestamp when callback was generated

Body parameters

Show example

application/json

billPaymentSucceeded

billPaymentSucceeded

Bill Payment Succeeded Webhook

Code snippet

```
{
  "created": "2025-08-01T10:46:08.208Z",
  "business_id": "60c820d70d4499475d05adb2",
  "event": "bill_payment.succeeded",
  "data": {
    "data": {
      "status": "SUCCEEDDED",
      "created_at": "2025-08-01T10:46:03Z",
      "payment_id": "3dd4ebd4-f6cf-4042-bc65-dd847adcfb77",
      "product_id": "PLN_PREPAID_50K",
      "updated_at": "2025-08-01T10:46:03Z",
      "reference_id": "PLN-20250801174603-5TV45",
      "total_amount": 53200,
      "customer_number": "50170719442",
      "ledger_transaction_id": ""
    },
    "event": "bill_payment.succeeded",
    "business_id": "60c820d70d4499475d05adb2"
  },
  "api_version": "v1"
}
```

JSON

Copy

Collapse all

object

created

string (date-time) Required

Timestamp when callback was created

business\_id

string Required

Xendit's Business ID

event

string Required

Event type

Valid values[
"bill\_payment.succeeded",
"bill\_payment.failed"
]

data

object Required

data

object Required

status

string Required

Valid values[
"SUCCEEDDED",
"FAILED"
]

created\_at

string (date-time) Required

payment\_id

string Required

product\_id

string Required

updated\_at

string (date-time) Required

bill\_details

Array of object (BillPaymentDetailKeyValue)

object

key

string Required

Name of the detail field

value

string Required

Value of the detail field

failure\_code

string | null

fulfilled\_at

string (date-time) | null

reference\_id

string Required

total\_amount

number Required

failure\_reason

string | null

customer\_number

string Required

payment\_details

Array of object (BillPaymentDetailKeyValue)

object

key

string Required

Name of the detail field

value

string Required

Value of the detail field

product\_details

Array of object (BillPaymentDetailKeyValue)

object

key

string Required

Name of the detail field

value

string Required

Value of the detail field

customer\_details

Array of object (BillPaymentDetailKeyValue)

object

key

string Required

Name of the detail field

value

string Required

Value of the detail field

ledger\_transaction\_id

string

event

string Required

Valid values[
"bill\_payment.succeeded",
"bill\_payment.failed"
]

business\_id

string Required

api\_version

string Required

Valid values[
"v1"
]

Responses

200

Webhook acknowledged successfully

Was this article helpful?

Yes  No

Previous article

Get Payment Detail

Next article

Get file by ID

- Try It
- Code samples

Request

URL

X-Callback-Signature \*

X-Callback-Timestamp \*

Body

application/json

application/json

billPaymentSucceeded

billPaymentSucceeded

 Reset to default

 

21

1

```
{
```

2

```
  "created": "2025-08-01T10:46:08.208Z",
```

3

```
  "business_id": "60c820d70d4499475d05adb2",
```

4

```
  "event": "bill_payment.succeeded",
```

5

```
  "data": {
```

6

```
    "data": {
```

7

```
      "status": "SUCCEEDDED",
```

8

```
      "created_at": "2025-08-01T10:46:03Z",
```

9

```
      "payment_id": "3dd4ebd4-f6cf-4042-bc65-dd847adcfb77",
```

10

```
      "product_id": "PLN_PREPAID_50K",
```

11

```
      "updated_at": "2025-08-01T10:46:03Z",
```

12

```
      "reference_id": "PLN-20250801174603-5TV45",
```

13

```
      "total_amount": 53200,
```

14

```
      "customer_number": "50170719442",
```

15

```
      "ledger_transaction_id": ""
```

16

```
    },
```

17

```
    "event": "bill_payment.succeeded",
```

18

```
    "business_id": "60c820d70d4499475d05adb2"
```

19

```
  },
```

20

```
  "api_version": "v1"
```

21

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