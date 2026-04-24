---
url: https://docs.xendit.co/apidocs/get-product-list
title: "Get Product List"
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
  - Products

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

# Get Product List

- Updated on Apr 1, 2026
- Published on Aug 8, 2025

 [Prev](/apidocs/update-customer "Update Customer")  [Next](/apidocs/get-product-by-id "Get Product by ID") 

Get

/bill-payments/v1/product

Gets a list of available products with optional filtering capabilities

Security

HTTP

Type Basic

Query parameters

id

string

Filter by specific product ID

ExamplePLN\_PREPAID\_50K

biller

string

Filter by biller name

ExamplePLN

category

string

Filter by product category

Valid values[
"ELECTRICITY"
]

ExampleELECTRICITY

country

string

Filter by country code (e.g. ID)

ExampleID

availability\_status

string

Filter by product availability status

Valid values[
"AVAILABLE",
"TEMPORARILY\_UNAVAILABLE",
"DISCONTINUED"
]

ExampleAVAILABLE

requires\_inquiry

boolean

Filter products that require inquiry step

Exampletrue

limit

integer

Number of records to be fetched per page

Default50

Example50

cursor

string

Cursor value for paginating the result

Exampledummy-cursor-value-001==

Responses

200

400

401

500

Show example

Successful response

application/json

plnPrepaid

plnPrepaid

PLN Prepaid 50K Example

Code snippet

```
{
  "limit": 50,
  "cursor": "dummy-cursor-value-001==",
  "data": [
    {
      "type": "product",
      "id": "PLN_PREPAID_50K",
      "properties": {
        "product_name": "PLN Prepaid 50K",
        "category": "ELECTRICITY",
        "biller": "PLN",
        "country": "ID",
        "currency": "IDR",
        "requires_inquiry": false,
        "availability_status": "AVAILABLE",
        "admin_amount": 3200,
        "base_amount": 50000,
        "total_amount": 53200,
        "revenue_share_amount": 1000,
        "locale": {
          "en": "PLN Prepaid 50.000",
          "id": "PLN Prabayar 50.000"
        }
      }
    }
  ]
}
```

JSON

Copy

Collapse all

object

data

Array of object (BillPaymentProduct)

Array of product objects

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

next\_cursor

string

Cursor value for next page. Empty if the last page reached

limit

integer

Number of records per page

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

API key in use does not have necessary permissions to perform the request. Please assign proper permissions for the key.

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

Internal Server Error

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

Update Customer

Next article

Get Product by ID

- Try It
- Code samples

Authentication

Request

URL

id

biller

category 

- 

-  ELECTRICITY

country

availability\_status 

- 

-  AVAILABLE  TEMPORARILY\_UNAVAILABLE  DISCONTINUED

requires\_inquiry

limit

cursor

 Try it & see response

Response

Available responses

application/json

application/json

200400401500

 

```
    "availability_status": "AVAILABLE",
```