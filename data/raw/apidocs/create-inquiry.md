---
url: https://docs.xendit.co/apidocs/create-inquiry
title: "Create Inquiry"
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
  - Inquiry

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

post

 [Create Inquiry](/apidocs/create-inquiry)

Payments

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Create Inquiry

- Updated on Apr 1, 2026
- Published on Aug 8, 2025

 [Prev](/apidocs/get-product-by-id "Get Product by ID")  [Next](/apidocs/create-payment "Create Payment") 

Post

/bill-payments/v1/inquiry

Facilitates pre-payment verification for products requiring upfront bill checks,
such as PLN electricity services. The response includes comprehensive
bill information and the total amount due.

Security

HTTP

Type Basic

Body parameters

Show example

application/json

plnPrepaid
plnPostpaid

plnPrepaid

PLN Prepaid Inquiry

Code snippet

```
{
  "product_id": "PLN_PREPAID_50K",
  "customer_number": "12345678910"
}
```

JSON

Copy

plnPostpaid

PLN Postpaid Inquiry

Code snippet

```
{
  "product_id": "PLN_POSTPAID",
  "customer_number": "22345678910"
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

additional\_properties

object

Additional parameters required for specific products

Responses

200

400

404

409

502

503

504

Show example

Successful inquiry response

application/json

plnPrepaid

plnPrepaid

PLN Prepaid Inquiry Response

Code snippet

```
{
  "data": {
    "business_id": "5f27a14a9bf05c73dd040bc8",
    "type": "inquiry",
    "id": "inq-98765",
    "properties": {
      "product_id": "PLN_PREPAID_50K",
      "admin_amount": 3200,
      "base_amount": 50000,
      "total_amount": 53200,
      "revenue_share_amount": 500,
      "currency": "IDR",
      "customer_number": "12345678910",
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
        },
        {
          "key": "Denom",
          "value": "100.000"
        }
      ],
      "bill_details": [
        {
          "key": "Admin",
          "value": "3200"
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

Type of response, always "inquiry"

Valid values[
"inquiry"
]

id

string

Unique inquiry identifier

properties

object

product\_id

string

Product identifier

admin\_amount

number

Administrative fee amount

base\_amount

number

Base product amount

total\_amount

number

Total amount including admin fee

revenue\_share\_amount

number

Partner revenue share amount

currency

string

Currency of the product

customer\_number

string

Customer's account/service number

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

Get Product by ID

Next article

Create Payment

- Try It
- Code samples

Authentication

Request

URL

Body

application/json

application/json

plnPrepaid

plnPrepaid

plnPostpaid

 Reset to default

 

4

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
  "customer_number": "12345678910"
```

4

```
}
```

 Try it & see response

Response

Available responses

application/json

application/json

200400404409502503504

 

```
   "customer_number": "string",
```