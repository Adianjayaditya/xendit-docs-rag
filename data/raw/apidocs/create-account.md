---
url: https://docs.xendit.co/apidocs/create-account
title: "Create account"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [xenPlatform](/apidocs/accounts-misc-introduction)
  - xenPlatform

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

# Create account

- Updated on Jan 8, 2026
- Published on Dec 6, 2024

 [Prev](/apidocs/accounts-misc-introduction "Introduction")  [Next](/apidocs/list-accounts "List accounts") 

Post

/v2/accounts

Create Account API allows you to create Accounts for your Partners on your Platform. Once an Account is created, you can accept and route payments through the Transfers API or Platform Fee API.
Read more about account types [here](https://docs.xendit.co/docs/sub-accounts).

Remember to store the returned account ID value to make transactions for that Account in the future.

> **Notes**:
>
> - For the `/v2/accounts` endpoint, we allow a maximum of 5 write requests per second.
> - The `OWNED` type is currently restricted for accounts in Indonesia.
>
> Please contact help@xendit.co if you need the above features.

**Version**

This version of the API is asynchronous to improve performance and scalability. We have also added API permissions in this version. If you are using an existing API key, please edit your permissions in your Settings page.

It is mandatory to wait for the `account.created` callback before attempting to create transactions. Set a Callback URL in your Dashboard to receive Account Updated Callbacks and know when payments can be processed for your Accounts.

> Use API key permission Account Write to perform this request

**Account Suspension Callbacks**

The Account Suspension webhook can be used to let your system know when Xendit has suspected, suspended or cleared the Accounts linked to your Platform. Our teams and systems automatically and regularly review Account behaviour to help Platforms mitigate potential fraud.

These events may occur if we have reason to believe that the Account has engaged in fraudulent activity. When these events occur, only the transactions occurring on that specific Account will be affected. This approach allows your Platform to continue accepting payments for your other Accounts normally.

Security

HTTP

Type basic

Body parameters

Show example

application/json

Owned Type

Owned Type

Code snippet

```
{
  "email": "angie@pinkpanther.com",
  "type": "OWNED",
  "public_profile": {
    "business_name": "Owned Business Account"
  }
}
```

JSON

Copy

Collapse all

object

email

string (email) Required

A valid email address associated with the object

Max length255

Exampletest@example.co

type

string

The type of account created

Valid values[
"MANAGED",
"OWNED"
]

public\_profile

object (public\_profile) Required

business\_name

string

Public name of the account.

description

string

Additional description visible publicly.

Responses

200

400

Show example

application/json

Owned Sub-account

Owned Sub-account

Code snippet

```
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
}
```

JSON

Copy

Collapse all

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

Validation errors for creating accounts

application/json

OneOf

400ApiValidationError

object (400ApiValidationError)

error\_code

string

ExampleAPI\_VALIDATION\_ERROR

error\_message

string

ExampleInputs are failing validation. The errors field contains details about which fields are violating validation.

400InvalidConfigurationError

object (400InvalidConfigurationError)

error\_code

string

ExampleINVALID\_CONFIGURATION

error\_message

string

ExampleThe `configurations` parameter combination is invalid. Please follow the requirement of each parameter written in Request section.

400TypeConfigConflictError

object (400TypeConfigConflictError)

error\_code

string

ExampleTYPE\_AND\_CONFIGURATION\_CONFLICT

error\_message

string

ExamplePlease provide either one of the `type` field or the `configurations` field

Was this article helpful?

Yes  No

Previous article

Introduction

Next article

List accounts

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

Body

application/json

application/json

Owned Type

Owned Type

 Reset to default

 

7

1

```
{
```

2

```
  "email": "angie@pinkpanther.com",
```

3

```
  "type": "OWNED",
```

4

```
  "public_profile": {
```

5

```
    "business_name": "Owned Business Account"
```

6

```
  }
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

200400

 

```
 "created": "2026-04-23T07:09:10.805Z",
```