---
url: https://docs.xendit.co/apidocs/simulate-cycle-payment
title: "Simulate cycle payment"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payments](/apidocs/introduction)
  - [Subscriptions](/apidocs/create-recurring-plan)

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

post

 [Create Subscription Plan](/apidocs/create-recurring-plan)

get

 [Get Subscription Plan](/apidocs/get-subscription-plan-2)

pat

 [Update Subscription Plan](/apidocs/update-subscription-plan-2)

post

 [Deactivate Subscription Plan](/apidocs/deactivate-subscription-plan-2)

get

 [Get List of Subscription Cycles](/apidocs/get-list-of-subscription-cycles-2)

get

 [Get Subscription Cycle](/apidocs/get-subscription-cycle-2)

pat

 [Update Subscription Cycle](/apidocs/update-subscription-cycle-2)

post

 [Cancel Subscription Cycle](/apidocs/cancel-subscription-cycle-2)

post

 [Force Attempt Subscription Cycle](/apidocs/force-attempt-subscription-cycle-2)

post

 [Simulate cycle payment](/apidocs/simulate-cycle-payment)

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

# Simulate cycle payment

- Updated on Apr 8, 2026
- Published on Apr 7, 2026

 [Prev](/apidocs/force-attempt-subscription-cycle-2 "Force Attempt Subscription Cycle")  [Next](/apidocs/payment-link "Payment Link") 

Post

/recurring/plans/{plan\_id}/cycles/{id}/simulate

Simulate cycle payment only for test mode

Header parameters

api-version

string

Valid values[
"2026-01-01"
]

for-user-id

string

The sub-account user-id to make this transaction for. This header is only used if you have access to xenPlatform. See xenPlatform for more information.

with-split-rule

string

The XenPlatform split rule ID that will be applied to this transaction. This header is only used if you have access to xenPlatform.

Path parameters

plan\_id

stringRequired

The ID of the recurring plan associated with the cycle.

id

stringRequired

The ID of the recurring cycle.

Body parameters

application/json

object

amount

number Required

Minimum0.0

Responses

200

400

401

403

404

500

Successfully simulate cycle payment

application/json

Collapse all

object

id

string

Xendit-generated recurring cycle ID.

Examplerecy\_4e66b458-00b7-4ddd-9859-cce153dda097

type

string

Indicates whether the cycle was charged as part of plan creation

Valid values[
"SCHEDULED",
"IMMEDIATE"
]

reference\_id

string

Inherited from Plan reference\_id

plan\_id

string

ID of the associated recurring plan.

Examplerepl\_4e66b458-00b7-4ddd-9859-cce153dda097

customer\_id

string

Xendit-generated customer ID.

cycle\_number

integer

The order of the current cycle within the plan

status

string

Status of the recurring cycle.

Valid values[
"SCHEDULED",
"PENDING",
"RETRYING",
"FAILED",
"SUCCEEDED",
"CANCELLED"
]

attempt\_details

Array of object

Details of any attempt actions made on the cycle.

object

attempt\_number

integer

Order of the attempt within the cycle. The current action belongs to this attempt.

action\_number

integer

Order of the action within an attempt. An attempt can have multiple actions.
In general, one action corresponds to one unique payment token within the same attempt.

type

string

The type of payment attempt made on the cycle.
INITIAL represents the first system generated attempt on the cycle.
RETRY represents all subsequent system generated attempt after first attempt failed.
FORCED represents explicit request made by the merchant to perform a payment attempt on the cycle.
PAYMENT\_LINK represents a payment link sent to the end user to solicit payment.

Valid values[
"INITIAL",
"RETRY",
"FORCED",
"PAYMENT\_LINK"
]

created

string (date-time)

The date time that the payment action was performed.

payment\_id

string | null

This field used to indicate the payment ID created from cycle

Examplepy-5cd39c23-89da-45f9-b316-f1e865b71b46

payment\_token\_id

string | null

The payment token ID used for this payment action.

Examplept-f8429206-f3ea-49f0-abb4-eaa89064056e

status

string

The status of the action

Valid values[
"SUCCEEDED",
"FAILED",
"PENDING"
]

failure\_code

string | null

If payment action encounters an error, the failure reason will be shown here.

next\_retry\_timestamp

string (date-time) | null

The date time that the next RETRY attempt should be created for this cycle.

payment\_session

object | null

Contains details of payment links sent to the end user.

session\_id

string

Payment session id created when the cycle attempt failed

Exampleps-661f87c614802d6c402cd82d

payment\_link\_url

string

This URL will lead the end user to a checkout page to complete the payment.

attempt\_count

integer

number of attempts made on the cycle so far

forced\_attempt\_count

integer

number of forced attempts made on the cycle so far

scheduled\_timestamp

string (date-time)

The scheduled date and time that the cycle will be executed. Always in UTC zero.

Example2020-11-20T16:23:52Z

currency

string

ISO 4217 currency code (e.g., IDR, PHP).

ExampleIDR

amount

number

Amount charged in the cycle.

Minimum0.0

metadata

object | null

created

string (date-time)

ISO 8601 date time format

Example2017-07-21T17:32:28Z

updated

string (date-time)

ISO 8601 date time format

Example2017-07-21T17:32:28Z

Show example

Validation errors occurred. Safe to retry.

application/json

API\_VALIDATION\_ERROR

API\_VALIDATION\_ERROR

Fields or values in the payload body does not comply with our API specification.

Code snippet

```
{
  "error_code": "API_VALIDATION_ERROR",
  "message": "Check the specific error message for debugging."
}
```

JSON

Copy

object

error\_code

string

Error code identifying the issue.

message

string

Description of the error.

Invalid API key or unauthorized access. Safe to retry.

application/json

object

Example{
"error\_code": "INVALID\_API\_KEY",
"message": "API key format is invalid."
}

error\_code

string

message

string

Show example

Ineligible request

application/json

INELIGIBLE\_CYCLE\_REQUEST

INELIGIBLE\_CYCLE\_REQUEST

Request cannot be processed.

Code snippet

```
{
  "error_code": "INELIGIBLE_CYCLE_REQUEST",
  "message": "Requested changes to cycle cannot be processed. Only cycles in \"SCHEDULED\" status can be simulated"
}
```

JSON

Copy

object

error\_code

string

message

string

Show example

Resource not found. Safe to retry.

application/json

DATA\_NOT\_FOUND

DATA\_NOT\_FOUND

Cycle not found.

Code snippet

```
{
  "error_code": "DATA_NOT_FOUND",
  "message": "Recurring cycle_id not found. Please check your query again."
}
```

JSON

Copy

object

error\_code

string

message

string

Server error.

application/json

object

Example{
"error\_code": "SERVER\_ERROR",
"message": "An unexpected error occurred. Our team has been notified and will troubleshoot the issue."
}

error\_code

string

message

string

Was this article helpful?

Yes  No

Previous article

Force Attempt Subscription Cycle

Next article

Payment Link

- Try It
- Code samples

Request

URL

plan\_id \*

id \*

api-version 

2026-01-01 

-  2026-01-01

for-user-id

with-split-rule

Body

application/json

application/json

 

3

1

```
{
```

2

```
 "amount": 1
```

3

```
}
```

 Try it & see response

Response

Available responses

application/json

application/json

200400401403404500

 

```
   "payment_token_id": "pt-f8429206-f3ea-49f0-abb4-eaa89064056e",
```