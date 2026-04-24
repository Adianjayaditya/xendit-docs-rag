---
url: https://docs.xendit.co/apidocs/get-payout-channels
title: "Get Payment Channels"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payouts](/apidocs/payouts-introduction)
  - [Payout](/apidocs/create-payout)

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

post

 [Create a Payout](/apidocs/create-payout)

post

 [Payout Webhook](/apidocs/payout-webhook-notification)

get

 [Get payout by ID](/apidocs/get-payout)

get

 [Get all payouts by reference id](/apidocs/get-all-payouts)

get

 [Cancel payout](/apidocs/cancel-payout)

get

 [Get Payment Channels](/apidocs/get-payout-channels)

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

# Get Payment Channels

- Updated on Jul 31, 2025
- Published on Nov 29, 2024

 [Prev](/apidocs/cancel-payout "Cancel payout")  [Next](/apidocs/create-cross-border-payout "Create a Cross-Border Payout") 

Get

/payouts\_channels

This API endpoint will provide you the current list of banks and E-Wallets we support for payouts

Security

HTTP

Type basic

Query parameters

currency

string

currency

string

Valid values[
"BANK",
"EWALLET",
"OTC"
]

currency

string

ExampleID\_BCA

Responses

200

401

404

500

Show example

'Returns array of Payout Channel objects sorted by alphabetical order by channel\_code with HTTP status code 200.
Return empty array when not found.

If query parameters are defined, returns a filtered list of Payout Channel objects matching the query parameter.

application/json

getPaymentChannelsResponseExample

getPaymentChannelsResponseExample

Code snippet

```
[
  {
    "channel_code": "ID_BSI",
    "channel_category": "BANK",
    "currency": "IDR",
    "channel_name": "Bank Syariah Indonesia",
    "amount_limits": {
      "minimum": 10000,
      "maximum": 1999999999999,
      "minimum_increment": 1
    }
  },
  {
    "channel_code": "PH_AUB",
    "channel_category": "BANK",
    "currency": "PHP",
    "channel_name": "Asia United Bank",
    "amount_limits": {
      "minimum": 1,
      "maximum": 100000000,
      "minimum_increment": 1
    }
  }
]
```

JSON

Copy

Array of object

object

channel\_name

string

Name of payout channel

channel\_category

string

Valid values[
"BANK",
"EWALLET",
"OTC"
]

channel\_code

string

Channel code of destination bank, E-Wallet or OTC channel.
List of supported channels can be found [here](https://docs.xendit.co/xendisburse/channel-codes)

ExampleID\_BCA

currency

string

ISO 4217 Currency Code.

amount\_limits

object

Object containing amount limitations imposed by the channel.

minimum

number

Minimum amount that can be paid out to this channel

maximum

number

Maximum amount that can be paid out to this channel

minimum\_increment

number

Smallest amount increment allowed by the channel

Unauthorized

application/json

OneOf

401InvalidAPIKeyError

object (401InvalidAPIKeyError)

error\_code

string

ExampleINVALID\_API\_KEY

error\_message

string

ExampleAPI key format is invalid

Not Found

application/json

OneOf

404DataNotFoundError

object (404DataNotFoundError)

error\_code

string

ExampleDATA\_NOT\_FOUND

error\_message

string

ExampleCould not find payout with the corresponding ID. Please try again with a valid Id

Internal Server Error

application/json

OneOf

500ServerError

object (500ServerError)

error\_code

string

ExampleSERVER\_ERROR

error\_message

string

ExampleError connecting to our server. Retry safely using Idempotency-key header when available

Was this article helpful?

Yes  No

Previous article

Cancel payout

Next article

Create a Cross-Border Payout

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

currency

currency 

- 

-  BANK  EWALLET  OTC

currency

 Try it & see response

Response

Available responses

application/json

application/json

200401404500

 

```
  "channel_category": "BANK",
```