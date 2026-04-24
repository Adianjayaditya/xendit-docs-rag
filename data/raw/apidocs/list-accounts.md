---
url: https://docs.xendit.co/apidocs/list-accounts
title: "List accounts"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [xenPlatform](/apidocs/accounts-misc-introduction)
  - [xenPlatform](/apidocs/create-account)

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

post

 [Create account](/apidocs/create-account)

get

 [List accounts](/apidocs/list-accounts)

get

 [Get account](/apidocs/get-account)

pat

 [Update account](/apidocs/update-account)

post

 [Create split rule](/apidocs/create-split-rule)

post

 [Create account holder](/apidocs/create-account-holder)

get

 [Get account holder](/apidocs/get-account-holder)

pat

 [Update account holder](/apidocs/update-account-holder)

get

 [Get transfer by reference](/apidocs/get-transfer-by-reference)

post

 [Create transfers](/apidocs/create-transfers)

post

 [Owned account status webhook notification](/apidocs/owned-account-status-webhook-notification)

post

 [Managed account status webhook notification](/apidocs/managed-account-status-webhook-notification)

post

 [Account suspension webhook notification](/apidocs/account-suspension-webhook-notification)

post

 [Account holder KYC status notification webhook](/apidocs/account-holder-kyc-status-notification-webhook)

post

 [Account holder capabilities notification webhook](/apidocs/account-holder-capabilities-notification-webhook)

post

 [Split payment status notification webhook](/apidocs/split-payment-status-notification-webhook)

Webhook Settings

Others

Download API reference

[Introduction](/apidocs/others-introduction)

Customers

Bill Payments

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# List accounts

- Updated on Jan 8, 2026
- Published on Dec 6, 2024

 [Prev](/apidocs/create-account "Create account")  [Next](/apidocs/get-account "Get account") 

Get

/v2/accounts

Use this endpoint to retrieve information about your sub accounts. You can filter by email, creation date, type, name, or status. The results are paginated and ordered by creation date

> Use API key permission Accounts Read to perform this request

> This endpoint is backward compatible with Accounts created using the /accounts endpoint

Security

HTTP

Type basic

Query parameters

email

array of string

The email addresses of the accounts that will be filtered. If not specified, all account emails will be returned.

Item Max length255

Item Exampletest@example.co

status

array of string

The statuses of the accounts that will be filtered. If not specified, all account status will be returned.

Valid Item values[
"INVITED",
"REGISTERED",
"AWAITING\_DOCS",
"PENDING\_VERIFICATION",
"LIVE",
"SUSPENDED"
]

public\_profile.business\_name

string

The public profile or business name of the accounts that will be filtered. If not specified, all account business name will be returned. This is the business name specified during account creation

type

string

The type of accounts that will be filtered. If not specified, all account types will be returned.

Valid values[
"MANAGED",
"OWNED"
]

created[gte]

string

Start time of accounts by created date. If not specified will list all dates.

created[lte]

string (date-time)

End time of accounts by created date. If not specified will list all dates.

updated[gte]

string (date-time)

Start time of accounts by updated date. If not specified will list all dates.

updated[lte]

string (date-time)

End time of accounts by updated date. If not specified will list all dates.

limit

number

A limit on the number of transactions to be returned for each request.

Minimum1.0

Maximum50.0

Default10.0

before\_id

string

ID of the immediately following item.

after\_id

string

ID of the immediately previous item. Use this with links on the response for pagination.

Responses

200

400

404

Show example

application/json

Get Owned Account Response

Get Owned Account Response

Code snippet

```
{
  "data": [
    {
      "id": "5cafeb170a2b18519b1b8761",
      "created": "2021-01-01T10:00:00Z",
      "updated": "2021-01-01T10:00:00Z",
      "type": "OWNED",
      "email": "angie@pinkpanther.com",
      "public_profile": {
        "business_name": "Angie's lemonade stand"
      },
      "status": "LIVE"
    },
    {
      "id": "3cafeb170a2b18519b1b8762",
      "created": "2023-03-22T09:15:00Z",
      "updated": "2023-03-22T09:30:00Z",
      "type": "MANAGED",
      "email": "carol@cooldrinks.com",
      "public_profile": {
        "business_name": "Carol's Cool Drinks"
      },
      "status": "LIVE"
    }
  ],
  "has_more": true,
  "links": [
    {
      "href": "/v2/accounts?after_id=623ace8270bbddf93816b3g1",
      "rel": "next",
      "method": "GET"
    }
  ]
}
```

JSON

Copy

Collapse all

object

data

Array of object (ListAccountResponseSchema)

object

id

string

ID of your Account, use this in the for-user-id header to create transactions on behalf of your Account

created

string (date-time)

Timestamp of when the object was created

updated

string (date-time)

Timestamp of when the object was updated

type

string

The type of account created

Valid values[
"MANAGED",
"OWNED"
]

email

string (email)

A valid email address associated with the object

Max length255

Exampletest@example.co

public\_profile

object (public\_profile)

business\_name

string

Public name of the account.

description

string

Additional description visible publicly.

country

string

The country (based on ISO 3166-1 Alpha-2) of incorporation for a business, or the country of residence for an individual.

Valid values[
"ID",
"PH",
"VN",
"MY",
"TH"
]

status

string

Status of the Account you are creating.

Valid values[
"INVITED",
"REGISTERED",
"AWAITING\_DOCS",
"PENDING\_VERIFICATION",
"LIVE",
"SUSPENDED"
]

has\_more

boolean

Indicates whether there are more items to be queried with `after_id` of the last item from the current result.
Use the `links` to follow to the next result.

links

Array of object

The links to the next page based on HATEOAS if there is next result.
The HATEOAS format are:
`href`: URI of target, this will be to the next link.
`rel`: The relationship between source and target. The value will be `next`.
`method`: The HTTP method, the value will be `GET`.

object

href

string

rel

string

method

string

Bad Request

application/json

object

Inputs are failing validation. The errors field contains details about which fields are violating validation.

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR",
"INVALID\_CONFIGURATION",
"INVALID\_JSON\_FORMAT",
"TYPE\_AND\_CONFIGURATION\_CONFLICT",
"INVALID\_SOURCE\_OR\_DESTINATION\_ERROR",
"INSUFFICIENT\_BALANCE",
"INVALID\_FEE\_AMOUNT",
"DUPLICATE\_ERROR",
"INVALID\_AMOUNT",
"INSUFFICIENT\_ACCOUNT\_HOLDER\_DATA",
"MISMATCH\_PAYLOAD\_FOR\_REFERENCE",
"INVALID\_URL\_FORMAT"
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

Not Found

application/json

object

The object being referenced does not exist

error\_code

string

Valid values[
"DESTINATION\_ACCOUNT\_NOT\_FOUND",
"DATA\_NOT\_FOUND",
"CALLBACK\_AUTHENTICATION\_TOKEN\_NOT\_FOUND\_ERROR"
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

Create account

Next article

Get account

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

email

status 

- 

-  INVITED  REGISTERED  AWAITING\_DOCS  PENDING\_VERIFICATION  LIVE  SUSPENDED

public\_profile.business\_name

type 

- 

-  MANAGED  OWNED

created[gte]

created[lte]

updated[gte]

updated[lte]

limit

before\_id

after\_id

 Try it & see response

Response

Available responses

application/json

application/json

200400404

 

```
   "created": "2026-04-23T07:10:22.977Z",
```