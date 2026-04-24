---
url: https://docs.xendit.co/apidocs/create-payment
title: "Create Payment"
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
  - Payments

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

# Create Payment

- Updated on Apr 1, 2026
- Published on Aug 8, 2025

 [Prev](/apidocs/create-inquiry "Create Inquiry")  [Next](/apidocs/get-payment-detail "Get Payment Detail") 

Post

/bill-payments/v1/payment

This endpoint allows users to submit a payment for a specific product.
It can be used for various types of payments, including utility bills,
prepaid services, and other products that may or may not require a prior inquiry.

Security

HTTP

Type Basic

Header parameters

Idempotency-Key

stringRequired

Unique key to prevent duplicate payments. Must be unique for each payment request.

Exampleunique-idempotency-key-123

Body parameters

Show example

application/json

plnPrepaid
plnPostpaid

plnPrepaid

PLN Prepaid Payment

Code snippet

```
{
  "product_id": "PLN_PREPAID_50K",
  "customer_number": "12345678910",
  "inquiry_id": "inq-98765",
  "reference_id": "tx-pln-001",
  "total_amount": 53200,
  "additional_properties": {}
}
```

JSON

Copy

plnPostpaid

PLN Postpaid Payment

Code snippet

```
{
  "product_id": "PLN_POSTPAID",
  "customer_number": "22345678910",
  "inquiry_id": "inq-98766",
  "reference_id": "tx-pln-postpaid-001",
  "total_amount": 159500
}
```

JSON

Copy

Collapse all

object

product\_id

string Required

Product identifier

customer\_number

string Required

Customer's account/service number

inquiry\_id

string

Inquiry ID from POST /inquiry (optional)

reference\_id

string Required

Partner's unique transaction reference

total\_amount

number Required

Total payment amount including admin fee

additional\_properties

object

Additional parameters required for specific products

Responses

200

400

402

404

409

502

503

504

Show example

Payment accepted for processing

application/json

plnPrepaidPending

plnPrepaidPending

PLN Prepaid Payment - Pending

Code snippet

```
{
  "data": {
    "business_id": "5f27a14a9bf05c73dd040bc8",
    "type": "payment",
    "id": "trx-98765",
    "properties": {
      "product_id": "PLN_PREPAID_50K",
      "customer_number": "12345678910",
      "reference_id": "tx-pln-001",
      "admin_amount": 3200,
      "base_amount": 50000,
      "total_amount": 53200,
      "currency": "IDR",
      "status": "PENDING",
      "fulfilled_at": null,
      "failure_code": null,
      "failure_reason": null,
      "customer_details": [],
      "product_details": [],
      "bill_details": [],
      "payment_details": []
    }
  }
}
```

JSON

Copy

Collapse all

object

data

object

business\_id

string

Xendit's Business ID

type

string

Type of response, always "payment"

Valid values[
"payment"
]

id

string

Unique payment transaction ID

properties

object

reference\_id

string

Partner's transaction reference

product\_id

string

Product identifier

customer\_number

string

Customer's account/service number

admin\_amount

number

Administrative fee amount

base\_amount

number

Base product amount

total\_amount

number

Total amount including admin fee

currency

string

Currency of the product

status

string

Payment status

Valid values[
"PENDING",
"SUCCEEDED",
"FAILED"
]

fulfilled\_at

string (date-time) | null

ISO8601 timestamp when payment completed (null when pending)

failure\_code

string | null

Error code in case of FAILED status

failure\_reason

string | null

Error message in case of FAILED status

customer\_details

Array of object (BillPaymentDetailKeyValue)

Array of customer information key-value pairs

object

key

string

Name of the detail field

value

string

Value of the detail field

product\_details

Array of object (BillPaymentDetailKeyValue)

Array of product information key-value pairs

object

key

string

Name of the detail field

value

string

Value of the detail field

bill\_details

Array of object (BillPaymentDetailKeyValue)

Array of billing information key-value pairs

object

key

string

Name of the detail field

value

string

Value of the detail field

payment\_details

Array of object (BillPaymentDetailKeyValue)

Array of payment information key-value pairs

object

key

string

Name of the detail field

value

string

Value of the detail field

Inputs are failing validation. The errors field contains details about which fields are violating validation.

application/json

object

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR",
"FEATURE\_NOT\_AVAILABLE"
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

Payment Required - Insufficient balance

application/json

object

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR",
"FEATURE\_NOT\_AVAILABLE"
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

The provided `id` does not exist. Please review the `id` and try again

application/json

object

error\_code

string

Valid values[
"RATE\_LIMIT\_EXCEEDED"
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

Conflict

application/json

object

error\_code

string

Valid values[
"DUPLICATE\_ERROR",
"IDEMPOTENCY\_ERROR"
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

Bad Gateway - Biller error

application/json

object

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR",
"FEATURE\_NOT\_AVAILABLE"
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

Service Unavailable - Biller maintenance

application/json

object

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR",
"FEATURE\_NOT\_AVAILABLE"
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

Gateway Timeout - Biller timeout

application/json

object

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR",
"FEATURE\_NOT\_AVAILABLE"
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

Create Inquiry

Next article

Get Payment Detail

- Try It
- Code samples

Authentication

Request

URL

Idempotency-Key \*

Body

application/json

application/json

plnPrepaid

plnPrepaid

plnPostpaid

 Reset to default

 

8

1

```
{
```

2

```
  "product_id": "PLN_PREPAID_50K",
```

3

```
  "customer_number": "12345678910",
```

4

```
  "inquiry_id": "inq-98765",
```

5

```
  "reference_id": "tx-pln-001",
```

6

```
  "total_amount": 53200,
```

7

```
  "additional_properties": {}
```

8

```
}
```

 Try it & see response

Response

Available responses

application/json

application/json

200400402404409502503504

 

```
   "fulfilled_at": "2026-04-23T07:16:14.202Z",
```