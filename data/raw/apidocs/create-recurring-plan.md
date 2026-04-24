---
url: https://docs.xendit.co/apidocs/create-recurring-plan
title: "Create Subscription Plan"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payments](/apidocs/introduction)
  - Subscriptions

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

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Create Subscription Plan

- Updated on Apr 8, 2026
- Published on Dec 4, 2024

 [Prev](/apidocs/refund-webhook-notification "Refund webhook notification")  [Next](/apidocs/get-subscription-plan-2 "Get Subscription Plan") 

Post

/recurring/plans

Creates a new subscription plan for managing subscription payments.

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

Body parameters

JSON object containing recurring plan details.

application/json

Collapse all

object

reference\_id

string Required

Merchant-provided identifier for the recurring plan.

Min length1

Examplemy-plan-01

customer\_id

string Required

Xendit-generated customer ID.

currency

string Required

ISO 4217 currency code (e.g., IDR, PHP).

ExampleIDR

amount

number Required

Amount to be charged in each recurring cycle.

Minimum0.0

schedule

object (Xendit\_Subscriptions\_API\_RecurringScheduleCreate) Required

interval

string Required

Frequency of the recurring cycles.

Valid values[
"DAY",
"WEEK",
"MONTH",
"YEAR"
]

interval\_count

integer Required

Number of intervals between consecutive cycles.

Minimum1.0

Maximum365.0

total\_recurrence

integer | null

Total number of cycles (optional; runs indefinitely if null).

Minimum1.0

Maximum32000.0

anchor\_date

string (date-time) Required

Start date for the recurring schedule (ISO 8601 format), max allowed day of the month is 28. Supports time offset and UTC zero.

Example2020-11-20T16:23:52Z

retry\_interval

string | null

Interval between retry attempts for failed payments.

Valid values[
"DAY",
null
]

retry\_interval\_count

integer | null

Number of retry intervals between consecutive retries.

Minimum1.0

Maximum365.0

total\_retry

integer | null

Maximum number of retries for failed cycles.

Minimum1.0

Maximum10.0

failed\_attempt\_notifications

Array of integer

Notifications triggered at specific retry attempts.

Example[
1,
3,
5
]

integer

Minimum1.0

Maximum10.0

payment\_tokens

Array of object Required

Min items0

Max items5

object

payment\_token\_id

string Required

ID for payment token.

Examplept-f8429206-f3ea-49f0-abb4-eaa89064056e

rank

integer Required

Order in which payment tokens will be attempted (1 to 5).

Minimum1.0

Maximum5.0

immediate\_payment

boolean

Payment taken upon recurring plan creation. Failing the payment will inactivate the plan.

Defaultfalse

failed\_cycle\_action

string

Determines if the plan should be terminated when a cycle fails. RESUME continues, STOP inactivates the plan.

Valid values[
"RESUME",
"STOP"
]

Default"RESUME"

notification\_channels

Array of string

Channels to notify end user.

string

Valid values[
"WHATSAPP",
"EMAIL"
]

locale

string

ISO 639-1 two-letter codes for language of notifications to be sent to end user

Default"en"

payment\_link\_for\_failed\_attempt

boolean

Whether a payment link is generated for failed cycle attempts.

Defaultfalse

metadata

object | null

Additional JSON properties. Max 20 keys, with key names up to 40 characters and values up to 80 characters.

Example{
"customKey": "customValue"
}

property\*

string additionalProperties

description

string | null

Custom description of the recurring plan.

Max length1000

ExampleMy newspaper subscription 01

items

Array of object (Xendit\_Subscriptions\_API\_BasketItem) | null

Details of items included in the recurring plan.

object

type

string Required

Type of item.

Valid values[
"DIGITAL\_PRODUCT",
"PHYSICAL\_PRODUCT",
"DIGITAL\_SERVICE",
"PHYSICAL\_SERVICE",
"FEES"
]

reference\_id

string Required

Min length1

Max length255

Examplemy-plan-01

name

string Required

Name of the item.

Min length1

Max length255

ExampleGranny Smith Apple

net\_unit\_amount

number Required

Net amount charged per unit. Negative values for discounts.

quantity

integer Required

Number of units of the item.

url

string | null

URL of the item, must be HTTPS or HTTP.

Pattern^https?:\/\/.+

category

string Required

Merchant category for the item.

Max length255

ExampleFood

subcategory

string | null

Subcategory for the item.

Max length255

ExampleFruits

description

string | null

Description of the item.

Max length255

ExampleGreen apple that is a little sour.

metadata

object | null

Additional JSON properties. Max 20 keys, with key names up to 40 characters and values up to 80 characters.

property\*

string additionalProperties

Responses

202

400

401

403

404

409

500

503

Successfully created a recurring plan. A webhook will follow to confirm plan activation.

application/json

Collapse all

object

reference\_id

string

Merchant-provided identifier for the recurring plan.

Min length1

Examplemy-plan-01

customer\_id

string

Xendit-generated customer ID.

currency

string

ISO 4217 currency code (e.g., IDR, PHP).

ExampleIDR

amount

number

Amount to be charged in each recurring cycle.

Minimum0.0

schedule

object (Xendit\_Subscriptions\_API\_RecurringScheduleCreate)

interval

string

Frequency of the recurring cycles.

Valid values[
"DAY",
"WEEK",
"MONTH",
"YEAR"
]

interval\_count

integer

Number of intervals between consecutive cycles.

Minimum1.0

Maximum365.0

total\_recurrence

integer | null

Total number of cycles (optional; runs indefinitely if null).

Minimum1.0

Maximum32000.0

anchor\_date

string (date-time)

Start date for the recurring schedule (ISO 8601 format), max allowed day of the month is 28. Supports time offset and UTC zero.

Example2020-11-20T16:23:52Z

retry\_interval

string | null

Interval between retry attempts for failed payments.

Valid values[
"DAY",
null
]

retry\_interval\_count

integer | null

Number of retry intervals between consecutive retries.

Minimum1.0

Maximum365.0

total\_retry

integer | null

Maximum number of retries for failed cycles.

Minimum1.0

Maximum10.0

failed\_attempt\_notifications

Array of integer

Notifications triggered at specific retry attempts.

Example[
1,
3,
5
]

integer

Minimum1.0

Maximum10.0

payment\_tokens

Array of object

Min items0

Max items5

object

payment\_token\_id

string

ID for payment token.

Examplept-f8429206-f3ea-49f0-abb4-eaa89064056e

rank

integer

Order in which payment tokens will be attempted (1 to 5).

Minimum1.0

Maximum5.0

immediate\_payment

boolean

Payment taken upon recurring plan creation. Failing the payment will inactivate the plan.

Defaultfalse

failed\_cycle\_action

string

Determines if the plan should be terminated when a cycle fails. RESUME continues, STOP inactivates the plan.

Valid values[
"RESUME",
"STOP"
]

Default"RESUME"

notification\_channels

Array of string

Channels to notify end user.

string

Valid values[
"WHATSAPP",
"EMAIL"
]

locale

string

ISO 639-1 two-letter codes for language of notifications to be sent to end user

Default"en"

payment\_link\_for\_failed\_attempt

boolean

Whether a payment link is generated for failed cycle attempts.

Defaultfalse

metadata

object | null

Additional JSON properties. Max 20 keys, with key names up to 40 characters and values up to 80 characters.

Example{
"customKey": "customValue"
}

property\*

string additionalProperties

description

string | null

Custom description of the recurring plan.

Max length1000

ExampleMy newspaper subscription 01

items

Array of object (Xendit\_Subscriptions\_API\_BasketItem) | null

Details of items included in the recurring plan.

object

type

string

Type of item.

Valid values[
"DIGITAL\_PRODUCT",
"PHYSICAL\_PRODUCT",
"DIGITAL\_SERVICE",
"PHYSICAL\_SERVICE",
"FEES"
]

reference\_id

string

Min length1

Max length255

Examplemy-plan-01

name

string

Name of the item.

Min length1

Max length255

ExampleGranny Smith Apple

net\_unit\_amount

number

Net amount charged per unit. Negative values for discounts.

quantity

integer

Number of units of the item.

url

string | null

URL of the item, must be HTTPS or HTTP.

Pattern^https?:\/\/.+

category

string

Merchant category for the item.

Max length255

ExampleFood

subcategory

string | null

Subcategory for the item.

Max length255

ExampleFruits

description

string | null

Description of the item.

Max length255

ExampleGreen apple that is a little sour.

metadata

object | null

Additional JSON properties. Max 20 keys, with key names up to 40 characters and values up to 80 characters.

property\*

string additionalProperties

id

string

Xendit-generated recurring plan ID.

Examplerepl\_4e66b458-00b7-4ddd-9859-cce153dda097

status

string

Status of the recurring plan.

Valid values[
"ACTIVE",
"INACTIVE",
"PENDING",
"REQUIRES\_ACTION"
]

failure\_code

string | null

Failure code for failed plan creation

ExampleUNPROCESSABLE\_ENTITY\_ERROR

country

string | null

Country code for the plan

ExampleID

recurring\_cycle\_count

integer

Number of cycles generated for this plan.

actions

Array of object

Array of objects containing URLs for end users to complete the recurring plan.

object

action

string

Describes the purpose of the action. `AUTH` triggers payment account linking.

url\_type

string

Type of URL, optimized for desktop or web interface.

Valid values[
"WEB"
]

url

string (uri)

Generated URL to perform the action.

method

string

HTTP method for calling the URL.

Valid values[
"GET",
"POST"
]

created

string (date-time)

ISO 8601 date time format

Example2017-07-21T17:32:28Z

updated

string (date-time)

ISO 8601 date time format

Example2017-07-21T17:32:28Z

Show example

Validation errors occurred.

application/json

API\_VALIDATION\_ERROR
INVALID\_PAYMENT\_TOKEN\_ID

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

INVALID\_PAYMENT\_TOKEN\_ID

Payment token ID is not in eligible status for plan creation.

Code snippet

```
{
  "error_code": "INVALID_PAYMENT_TOKEN_ID",
  "message": "The payment_token_id provided has a mismatched currency or it is not \"ACTIVE\" because it has expired/ been unlinked/ linking has not been completed. Please retry with a valid payment_token_id."
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

Invalid API key or unauthorized access.

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

Request forbidden error.

application/json

object

Example{
"error\_code": "REQUEST\_FORBIDDEN\_ERROR",
"message": "The request is forbidden."
}

error\_code

string

message

string

Show example

Resource not found.

application/json

CUSTOMER\_NOT\_FOUND

CUSTOMER\_NOT\_FOUND

Customer not found.

Code snippet

```
{
  "error_code": "CUSTOMER_NOT_FOUND_ERROR",
  "message": "customer_id is invalid or not found. Please try again with a valid customer_id."
}
```

JSON

Copy

object

error\_code

string

message

string

Idempotency error.

application/json

object

Example{
"error\_code": "IDEMPOTENCY\_ERROR",
"message": "Idempotency key has been used before."
}

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

Payment server error.

application/json

object

Example{
"error\_code": "CHANNEL\_UNAVAILABLE",
"message": "The payment channel is currently unavailable. Please try again later."
}

error\_code

string

message

string

Callbacks

Post

/{merchant defined callback url}

Body parameters

Recurring plan webhook

application/json

Collapse all

object

Recurring plan webhook to indentify status transition of plan

event

string

Webhook event names for recurring plan status updates.

Valid values[
"recurring.plan.activated",
"recurring.plan.inactivated"
]

business\_id

string

Business ID of Xendit

Example62440e322008e87fb29c1fd0

created

string (date-time)

Timestamp of webhook delivery attempt in ISO 8601 date-time format.

Example2021-12-31T23:59:59Z

data

object

reference\_id

string Required

Merchant-provided identifier for the recurring plan.

Min length1

Examplemy-plan-01

customer\_id

string Required

Xendit-generated customer ID.

currency

string Required

ISO 4217 currency code (e.g., IDR, PHP).

ExampleIDR

amount

number Required

Amount to be charged in each recurring cycle.

Minimum0.0

schedule

object (Xendit\_Subscriptions\_API\_RecurringScheduleCreate) Required

interval

string Required

Frequency of the recurring cycles.

Valid values[
"DAY",
"WEEK",
"MONTH",
"YEAR"
]

interval\_count

integer Required

Number of intervals between consecutive cycles.

Minimum1.0

Maximum365.0

total\_recurrence

integer | null

Total number of cycles (optional; runs indefinitely if null).

Minimum1.0

Maximum32000.0

anchor\_date

string (date-time) Required

Start date for the recurring schedule (ISO 8601 format), max allowed day of the month is 28. Supports time offset and UTC zero.

Example2020-11-20T16:23:52Z

retry\_interval

string | null

Interval between retry attempts for failed payments.

Valid values[
"DAY",
null
]

retry\_interval\_count

integer | null

Number of retry intervals between consecutive retries.

Minimum1.0

Maximum365.0

total\_retry

integer | null

Maximum number of retries for failed cycles.

Minimum1.0

Maximum10.0

failed\_attempt\_notifications

Array of integer

Notifications triggered at specific retry attempts.

Example[
1,
3,
5
]

integer

Minimum1.0

Maximum10.0

payment\_tokens

Array of object Required

Min items0

Max items5

object

payment\_token\_id

string Required

ID for payment token.

Examplept-f8429206-f3ea-49f0-abb4-eaa89064056e

rank

integer Required

Order in which payment tokens will be attempted (1 to 5).

Minimum1.0

Maximum5.0

immediate\_payment

boolean

Payment taken upon recurring plan creation. Failing the payment will inactivate the plan.

Defaultfalse

failed\_cycle\_action

string

Determines if the plan should be terminated when a cycle fails. RESUME continues, STOP inactivates the plan.

Valid values[
"RESUME",
"STOP"
]

Default"RESUME"

notification\_channels

Array of string

Channels to notify end user.

string

Valid values[
"WHATSAPP",
"EMAIL"
]

locale

string

ISO 639-1 two-letter codes for language of notifications to be sent to end user

Default"en"

payment\_link\_for\_failed\_attempt

boolean

Whether a payment link is generated for failed cycle attempts.

Defaultfalse

metadata

object | null

Additional JSON properties. Max 20 keys, with key names up to 40 characters and values up to 80 characters.

Example{
"customKey": "customValue"
}

property\*

string additionalProperties

description

string | null

Custom description of the recurring plan.

Max length1000

ExampleMy newspaper subscription 01

items

Array of object (Xendit\_Subscriptions\_API\_BasketItem) | null

Details of items included in the recurring plan.

object

type

string Required

Type of item.

Valid values[
"DIGITAL\_PRODUCT",
"PHYSICAL\_PRODUCT",
"DIGITAL\_SERVICE",
"PHYSICAL\_SERVICE",
"FEES"
]

reference\_id

string Required

Min length1

Max length255

Examplemy-plan-01

name

string Required

Name of the item.

Min length1

Max length255

ExampleGranny Smith Apple

net\_unit\_amount

number Required

Net amount charged per unit. Negative values for discounts.

quantity

integer Required

Number of units of the item.

url

string | null

URL of the item, must be HTTPS or HTTP.

Pattern^https?:\/\/.+

category

string Required

Merchant category for the item.

Max length255

ExampleFood

subcategory

string | null

Subcategory for the item.

Max length255

ExampleFruits

description

string | null

Description of the item.

Max length255

ExampleGreen apple that is a little sour.

metadata

object | null

Additional JSON properties. Max 20 keys, with key names up to 40 characters and values up to 80 characters.

property\*

string additionalProperties

id

string

Xendit-generated recurring plan ID.

Examplerepl\_4e66b458-00b7-4ddd-9859-cce153dda097

status

string

Status of the recurring plan.

Valid values[
"ACTIVE",
"INACTIVE",
"PENDING",
"REQUIRES\_ACTION"
]

failure\_code

string | null

Failure code for failed plan creation

ExampleUNPROCESSABLE\_ENTITY\_ERROR

country

string | null

Country code for the plan

ExampleID

recurring\_cycle\_count

integer

Number of cycles generated for this plan.

actions

Array of object

Array of objects containing URLs for end users to complete the recurring plan.

object

action

string Required

Describes the purpose of the action. `AUTH` triggers payment account linking.

url\_type

string

Type of URL, optimized for desktop or web interface.

Valid values[
"WEB"
]

url

string (uri)

Generated URL to perform the action.

method

string

HTTP method for calling the URL.

Valid values[
"GET",
"POST"
]

created

string (date-time)

ISO 8601 date time format

Example2017-07-21T17:32:28Z

updated

string (date-time)

ISO 8601 date time format

Example2017-07-21T17:32:28Z

Responses

200

OK

Was this article helpful?

Yes  No

Previous article

Refund webhook notification

Next article

Get Subscription Plan

- Try It
- Code samples

Request

URL

api-version 

2026-01-01 

-  2026-01-01

for-user-id

with-split-rule

Body

application/json

application/json

 

53

1

```
{
```

2

```
 "reference_id": "my-plan-01",
```

3

```
 "customer_id": "string",
```

4

```
 "currency": "IDR",
```

5

```
 "amount": 1,
```

6

```
 "schedule": {
```

7

```
  "interval": "DAY",
```

8

```
  "interval_count": 1,
```

9

```
  "total_recurrence": 1,
```

10

```
  "anchor_date": "2020-11-20T16:23:52Z",
```

11

```
  "retry_interval": "DAY",
```

12

```
  "retry_interval_count": 1,
```

13

```
  "total_retry": 1,
```

14

```
  "failed_attempt_notifications": [
```

15

```
   1,
```

16

```
   3,
```

17

```
   5
```

18

```
  ]
```

19

```
 },
```

20

```
 "payment_tokens": [
```

21

```
  {
```

22

```
   "payment_token_id": "pt-f8429206-f3ea-49f0-abb4-eaa89064056e",
```

23

```
   "rank": 1
```

24

```
  }
```

 Try it & see response

Response

Available responses

application/json

application/json

202400401403404409500503

 

```
   "payment_token_id": "pt-f8429206-f3ea-49f0-abb4-eaa89064056e",
```