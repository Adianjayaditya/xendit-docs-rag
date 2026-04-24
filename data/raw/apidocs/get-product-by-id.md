---
url: https://docs.xendit.co/apidocs/get-product-by-id
title: "Get Product by ID"
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
  - [Products](/apidocs/get-product-list)

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

get

 [Get Product List](/apidocs/get-product-list)

get

 [Get Product by ID](/apidocs/get-product-by-id)

Inquiry

Payments

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Get Product by ID

- Updated on Apr 1, 2026
- Published on Aug 8, 2025

 [Prev](/apidocs/get-product-list "Get Product List")  [Next](/apidocs/create-inquiry "Create Inquiry") 

Get

/bill-payments/v1/product/{id}

Gets a specific product by its ID

Security

HTTP

Type Basic

Path parameters

id

stringRequired

Product ID

ExamplePLN\_PREPAID\_50K

Responses

200

404

Successful response

application/json

Collapse all

object

type

string

Type of object, always "product"

Valid values[
"product"
]

id

string

Unique product identifier

properties

object

product\_name

string

Display name of the product

category

string

Product category

Valid values[
"ELECTRICITY"
]

biller

string

Name of the biller/provider

country

string

Country code in ISO 3166-1 alpha-2 format

currency

string

Currency code in ISO 4217 format

requires\_inquiry

boolean

Whether product requires inquiry before purchase

availability\_status

string

Product availability status

Valid values[
"AVAILABLE",
"TEMPORARILY\_UNAVAILABLE",
"DISCONTINUED"
]

admin\_amount

number

Administrative fee amount

base\_amount

number

Base product amount (0 for postpaid products)

total\_amount

number

Total amount including admin fee

revenue\_share\_amount

number

Merchant revenue share amount

locale

object

Localized product names

en

string

Product name in English

id

string

Product name in Indonesian

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

Get Product List

Next article

Create Inquiry

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
  "availability_status": "AVAILABLE",
```