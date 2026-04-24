---
url: https://docs.xendit.co/apidocs/get-payment-detail
title: "Get Payment Detail"
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

# Get Payment Detail

- Updated on Apr 1, 2026
- Published on Aug 8, 2025

 [Prev](/apidocs/create-payment "Create Payment")  [Next](/apidocs/payment-status-callback-webhook "Payment Status Callback (Webhook)") 

Get

/bill-payments/v1/payment/{id}

This endpoint retrieves detailed information about a specific payment,
including its current status and fulfillment results if available.

Security

HTTP

Type Basic

Path parameters

id

stringRequired

Payment transaction ID from post payment response

Exampletrx-98765

Responses

200

404

Show example

Payment details retrieved successfully

application/json

plnPrepaidSuccess

plnPrepaidSuccess

PLN Prepaid Payment - Success

Code snippet

```
{
  "data": {
    "business_id": "5f27a14a9bf05c73dd040bc8",
    "type": "payment",
    "id": "trx-98765",
    "properties": {
      "reference_id": "tx-pln-001",
      "product_id": "PLN_PREPAID_50K",
      "customer_number": "12345678910",
      "admin_amount": 3200,
      "base_amount": 50000,
      "total_amount": 53200,
      "currency": "IDR",
      "status": "SUCCEEDED",
      "fulfilled_at": "2024-01-23T08:15:30Z",
      "failure_code": null,
      "failure_reason": null,
      "customer_details": [
        {
          "key": "Nama Pelanggan",
          "value": "John Doe"
        },
        {
          "key": "Nomor Pelanggan",
          "value": "12345678910"
        }
      ],
      "product_details": [
        {
          "key": "Tarif/Daya",
          "value": "R2/000003500"
        }
      ],
      "bill_details": [
        {
          "key": "Admin",
          "value": "3200"
        }
      ],
      "payment_details": [
        {
          "key": "Token",
          "value": "1234-5678-9012-3456-7890"
        },
        {
          "key": "Serial Number",
          "value": "PLN987654321"
        }
      ]
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

Was this article helpful?

Yes  No

Previous article

Create Payment

Next article

Payment Status Callback (Webhook)

- Try It
- Code samples

Authentication

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
   "fulfilled_at": "2026-04-23T07:19:49.250Z",
```