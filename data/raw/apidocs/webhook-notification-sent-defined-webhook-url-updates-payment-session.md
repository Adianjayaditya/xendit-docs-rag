---
url: https://docs.xendit.co/apidocs/webhook-notification-sent-defined-webhook-url-updates-payment-session
title: "Webhook notification that will be sent to your defined webhook url for updates to payment session status."
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payments](/apidocs/introduction)
  - [Session](/apidocs/create-session)

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

post

 [Create a session](/apidocs/create-session)

get

 [Get the status of a session](/apidocs/get-session)

post

 [Cancel a session](/apidocs/cancel-session)

post

 [Webhook notification that will be sent to your defined webhook url for updates to payment session status.](/apidocs/webhook-notification-sent-defined-webhook-url-updates-payment-session)

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

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Webhook notification that will be sent to your defined webhook url for updates to payment session status.

- Updated on Apr 8, 2026
- Published on Mar 31, 2026

 [Prev](/apidocs/cancel-session "Cancel a session")  [Next](/apidocs/refund-payment-request "Refund a payment request") 

Post

/your\_payment\_session\_webhook\_url

Webhook notification that will be sent to your defined webhook url for updates to payment session status.

Security

HTTP

Type basic

Body parameters

Show example

application/json

PaymentSession\_CompletedExample
PaymentSession\_ExpiredExample
PaymentSession\_SubscriptionCompletedExample

PaymentSession\_CompletedExample

Code snippet

```
{
  "event": "payment_session.completed",
  "business_id": "661f87c614802d6c402cd82d",
  "created": "2026-12-31T23:59:59Z",
  "data": {
    "payment_session_id": "ps-661f87c614802d6c402cd82d",
    "created": "2026-12-30T23:59:59Z",
    "updated": "2026-12-31T23:59:59Z",
    "reference_id": "order_12345_PAY",
    "customer_id": "cust-e2878b4c-d57e-4a2c-922d-c0313c2800a3",
    "session_type": "PAY",
    "allow_save_payment_method": "OPTIONAL",
    "currency": "PHP",
    "amount": 10000,
    "country": "PH",
    "mode": "PAYMENT_LINK",
    "expires_at": "2027-12-31T23:59:59Z",
    "locale": "en",
    "description": "Insurance Plan Registration",
    "success_return_url": "https://yourcompany.com/success/example_item=my_item",
    "cancel_return_url": "https://yourcompany.com/cancel/example_item=my_item",
    "status": "COMPLETED",
    "payment_link_url": "https://xen.to/kGxPCi60",
    "payment_token_id": "pt-661f87c614802d6c402cd82d",
    "payment_request_id": "pr-661f87c614802d6c402cd82d",
    "payment_id": "py-661f87c614802d6c402cd82d",
    "business_id": "661f87c614802d6c402cd82d"
  }
}
```

JSON

Copy

PaymentSession\_ExpiredExample

Code snippet

```
{
  "event": "payment_session.expired",
  "business_id": "661f87c614802d6c402cd82d",
  "created": "2021-12-31T23:59:59Z",
  "data": {
    "payment_session_id": "ps-661f87c614802d6c402cd82d",
    "created": "2021-12-31T23:59:59Z",
    "updated": "2021-12-31T23:59:59Z",
    "reference_id": "order_12345_PAY",
    "customer_id": "cust-e2878b4c-d57e-4a2c-922d-c0313c2800a3",
    "session_type": "PAY",
    "currency": "PHP",
    "amount": 10000,
    "country": "PH",
    "mode": "PAYMENT_LINK",
    "expires_at": "2021-12-31T23:59:59Z",
    "locale": "en",
    "description": "Insurance Plan Registration",
    "success_return_url": "https://yourcompany.com/success/example_item=my_item",
    "cancel_return_url": "https://yourcompany.com/cancel/example_item=my_item",
    "status": "EXPIRED",
    "payment_link_url": "https://xen.to/kGxPCi60"
  }
}
```

JSON

Copy

PaymentSession\_SubscriptionCompletedExample

Code snippet

```
{
  "event": "payment_session.completed",
  "business_id": "661f87c614802d6c402cd82d",
  "created": "2026-12-31T23:59:59Z",
  "data": {
    "payment_session_id": "ps-661f87c614802d6c402cd82d",
    "created": "2026-12-30T23:59:59Z",
    "updated": "2026-12-31T23:59:59Z",
    "reference_id": "subscription_12345",
    "customer_id": "cust-e2878b4c-d57e-4a2c-922d-c0313c2800a3",
    "session_type": "SUBSCRIPTION",
    "currency": "PHP",
    "amount": 50000,
    "country": "PH",
    "mode": "PAYMENT_LINK",
    "expires_at": "2027-12-31T23:59:59Z",
    "locale": "en",
    "description": "Monthly subscription plan",
    "success_return_url": "https://yourcompany.com/success/example_item=my_item",
    "cancel_return_url": "https://yourcompany.com/cancel/example_item=my_item",
    "status": "COMPLETED",
    "payment_link_url": "https://xen.to/kGxPCi60",
    "payment_token_id": "pt-661f87c614802d6c402cd82d",
    "payment_request_id": "pr-661f87c614802d6c402cd82d",
    "payment_id": "py-661f87c614802d6c402cd82d",
    "business_id": "661f87c614802d6c402cd82d"
  }
}
```

JSON

Copy

Collapse all

object

Payment session status webhook

event

string

Webhook event names for payment session status updates.
Applies to all session types including SUBSCRIPTION.

Valid values[
"payment\_session.completed",
"payment\_session.expired"
]

business\_id

string

Business ID of the merchant

Example661f87c614802d6c402cd82d

created

string (date-time)

Timestamp of webhook delivery attempt in ISO 8601 date-time format.

Example2021-12-31T23:59:59Z

data

object (Payment\_Session\_SessionWebhookSchema)

customer\_id

string

A unique identifier automatically generated by Xendit to represent an end customer. This ID can be used as a consistent reference across multiple transactions or payment activities for the same user. You can create a customer object in advance through the Create Customer API here: <https://xendit-docs.document360.io/apidocs/create-customer-request>

Min length41

Max length41

Examplecust-b98d6f63-d240-44ec-9bd5-aa42954c4f48

reference\_id

string

Your reference to uniquely identify the Payment Session. This is commonly used to identify your order or transaction.

Min length1

Max length64

payment\_session\_id

string

A unique identifier for the Payment Session

Min length27

Max length27

Exampleps-661f87c614802d6c402cd82d

payment\_request\_id

string | null

Xendit Payment Request ID used to reference the payment made during this Session.

Examplepr-0800fe40-bb79-47ae-9d1e-e69394d3949c

session\_type

string

The use case for Payment Session.
SAVE: save the payment details from a customer for future payments.
PAY: collects a one-time payment from a customer.
SUBSCRIPTION: register a subscription payment for your customer using Xendit Subscription product, see here <https://docs.xendit.co/docs/subscriptions-overview>.
AUTHORIZATION: authorize a card payment for a future capture.

Valid values[
"SAVE",
"PAY",
"SUBSCRIPTION",
"AUTHORIZATION"
]

mode

string

The frontend integration mode for Payment Session.
PAYMENT\_LINK: redirect the customer to the Xendit Hosted Checkout page.
COMPONENTS: collect the payment details directly from the customer on your own page using Xendit Components.
CARDS\_SESSION\_JS: collect payment details from customer with cards-session Javascript library.
Only supported PAYMENT\_LINK and CARDS\_SESSION\_JS as mode for now.

Valid values[
"PAYMENT\_LINK",
"COMPONENTS",
"CARDS\_SESSION\_JS"
]

status

string

The status of the Payment Session.

Valid values[
"ACTIVE",
"COMPLETED",
"EXPIRED",
"CANCELED"
]

updated

string (date-time)

Example2021-12-31T23:59:59Z

created

string (date-time)

Example2021-12-31T23:59:59Z

expires\_at

string (date-time)

ISO 8601 date-time format.
By default the Session will expire 30 minutes after creation.
We recommend you to keep Sessions short-lived and create a new Session again only when the customer is ready to make payment.

Example2021-12-31T23:59:59Z

locale

string

ISO 639-1 two-letter language code for Hosted Checkout page.

Default"en"

Exampleen

description

string

A custom description for the Session. This text will be displayed on the Xendit Hosted Checkout page.

Min length1

Max length1000

ExamplePayment for your order #123

items

Array of object (Payment\_Session\_XenditStandardItem) | null

Array of objects describing the item/s attached to the session.

object

reference\_id

string Required

Merchant provided identifier for the item

Min length1

Max length255

type

Type of item

Valid values[
"DIGITAL\_PRODUCT",
"PHYSICAL\_PRODUCT",
"DIGITAL\_SERVICE",
"PHYSICAL\_SERVICE",
"FEE"
]

name

string Required

Name of item

Min length1

Max length255

net\_unit\_amount

number Required

Net amount to be charged per unit

quantity

integer Required

Number of units of this item in the basket

Minimum1.0

url

string

URL of the item. Must be HTTPS or HTTP

image\_url

string

URL of the image of the item. Must be HTTPS or HTTP

category

string Required

Category for item

Max length255

subcategory

string

Sub-category for item

Max length255

description

string

Description of item

Max length255

metadata

object (Payment\_Session\_MerchantMetadata) | null

Key-value entries for your custom data/information.
You can specify up to 50 keys, with key names up to 40 characters and values up to 500 characters.
This is commonly used for your internal reference or reconciliation purposes. Xendit will not use this data for any processing.

Example{
"my\_custom\_id": "merchant-123",
"my\_custom\_order\_id": "order-123"
}

success\_return\_url

string

Specify the URL to redirect the customer after the session is completed or expired,
or if the customer decide to stop the payment process.
Must be HTTPS.
For example: "https://yourcompany.com/example\_item=my\_example\_item"

Examplehttps://yourcompany.com/example\_item

cancel\_return\_url

string

Specify the URL to redirect the customer after the session is completed or expired,
or if the customer decide to stop the payment process.
Must be HTTPS.
For example: "https://yourcompany.com/example\_item=my\_example\_item"

Examplehttps://yourcompany.com/example\_item

payment\_link\_url

string | null

The URL for Xendit Hosted Checkout page. Redirect your customer to this URL to complete the payment.

Examplehttps://checkout.xendit.co/sessions/ps-661f87c614802d6c402cd82d0 or https://xen.to/kGxPCi60. For test mode, https://checkout-staging.xendit.co/sessions/ps-661f87c614802d6c402cd82d0 or https://dev.xen.to/kGxPCi76

payment\_token\_id

string | null

Xendit Payment Token ID used to reference the saved payment details from the customer.

Exampleptkn-cc3938dc-c2a5-43c4-89d7-7570793348c2

payment\_id

string | null

Xendit Payment ID used to reference the captured payment details from the customer.

Examplepy-ac1fcd3e-21c5-4c70-bb06-fa3c34e19e0c

business\_id

string

Business ID of the merchant

components\_sdk\_key

string | null

key will be used for sessions flows with mode COMPONENT

Examplef5RBHw4S3SeZV8KGlBxjy8tyN2Vg4klA5Bww7

components\_configuration

object (Payment\_Session\_ComponentsConfiguration) | null

origins

Array of string

Origins will be used for sessions flows with mode COMPONENT to validate CORS

Example[
"https://yourcompany.com"
]

string

Responses

200

OK

Was this article helpful?

Yes  No

Previous article

Cancel a session

Next article

Refund a payment request

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

PaymentSession\_CompletedExample

PaymentSession\_CompletedExample

PaymentSession\_ExpiredExample

PaymentSession\_SubscriptionCompletedExample

 Reset to default

 

29

1

```
{
```

2

```
  "event": "payment_session.completed",
```

3

```
  "business_id": "661f87c614802d6c402cd82d",
```

4

```
  "created": "2026-12-31T23:59:59Z",
```

5

```
  "data": {
```

6

```
    "payment_session_id": "ps-661f87c614802d6c402cd82d",
```

7

```
    "created": "2026-12-30T23:59:59Z",
```

8

```
    "updated": "2026-12-31T23:59:59Z",
```

9

```
    "reference_id": "order_12345_PAY",
```

10

```
    "customer_id": "cust-e2878b4c-d57e-4a2c-922d-c0313c2800a3",
```

11

```
    "session_type": "PAY",
```

12

```
    "allow_save_payment_method": "OPTIONAL",
```

13

```
    "currency": "PHP",
```

14

```
    "amount": 10000,
```

15

```
    "country": "PH",
```

16

```
    "mode": "PAYMENT_LINK",
```

17

```
    "expires_at": "2027-12-31T23:59:59Z",
```

18

```
    "locale": "en",
```

19

```
    "description": "Insurance Plan Registration",
```

20

```
    "success_return_url": "https://yourcompany.com/success/example_item=my_item",
```

21

```
    "cancel_return_url": "https://yourcompany.com/cancel/example_item=my_item",
```

22

```
    "status": "COMPLETED",
```

23

```
    "payment_link_url": "https://xen.to/kGxPCi60",
```

24

```
    "payment_token_id": "pt-661f87c614802d6c402cd82d",
```

 Try it & see response

Response

Available responses

200

 

```
null
```