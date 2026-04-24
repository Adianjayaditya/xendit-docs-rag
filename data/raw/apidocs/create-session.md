---
url: https://docs.xendit.co/apidocs/create-session
title: "Create a session"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payments](/apidocs/introduction)
  - Session

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

# Create a session

- Updated on Apr 8, 2026
- Published on Dec 4, 2024

 [Prev](/apidocs/payment-token-webhook-notification "Payment token webhook notification")  [Next](/apidocs/get-session "Get the status of a session") 

Post

/sessions

Initiate the process of collecting payments from your customer.
We recommend creating a new Session from your server and redirect the customer to the Session Hosted Checkout page.
Once payment has succeeded, Session will contain a reference Payment ID or the Payment Token ID.
You get the outcome asynchronously in a Session webhook.

Security

HTTP

Type basic

Header parameters

for-user-id

string

The XenPlatform subaccount user id that will perform this transaction.

with-split-rule

string

The XenPlatform split rule id that will be applied to this transaction.

Body parameters

Show example

application/json

PaymentLink\_OneTimePaymentExample
PaymentLink\_PayandSaveExample
PaymentLink\_SavePaymentMethodExample
PaymentLink\_ManualCaptureExample
XenditComponents\_OneTimePaymentExample
XenditComponents\_PayandSaveExample
XenditComponents\_SavePaymentMethodExample
XenditComponents\_ManualCaptureExample
PaymentLink\_SubscriptionExample
XenditComponents\_SubscriptionExample

PaymentLink\_OneTimePaymentExample

Code snippet

```
{
  "reference_id": "order_12345_PAY",
  "session_type": "PAY",
  "mode": "PAYMENT_LINK",
  "amount": 10000,
  "currency": "PHP",
  "country": "PH",
  "customer": {
    "reference_id": "cust_Lorem_Ipsum",
    "type": "INDIVIDUAL",
    "email": "test@yourdomain.com",
    "mobile_number": "+6212345678",
    "individual_detail": {
      "given_names": "Lorem",
      "surname": "Ipsum"
    }
  },
  "items": [
    {
      "reference_id": "item_001",
      "name": "Clothes",
      "description": "Red clothes",
      "type": "PHYSICAL_PRODUCT",
      "category": "CLOTHES",
      "net_unit_amount": 5000,
      "quantity": 1,
      "currency": "PHP",
      "url": "https://example.com/item"
    },
    {
      "reference_id": "item_002",
      "name": "Pants",
      "description": "Black pants",
      "type": "PHYSICAL_PRODUCT",
      "category": "CLOTHES",
      "net_unit_amount": 5000,
      "quantity": 1,
      "currency": "PHP",
      "url": "https://example.com/item"
    }
  ],
  "capture_method": "AUTOMATIC",
  "locale": "en",
  "description": "Sample one-time payment using Payment Session",
  "success_return_url": "https://yourcompany.com/success/example_item=my_item",
  "cancel_return_url": "https://yourcompany.com/cancel/example_item=my_item"
}
```

JSON

Copy

PaymentLink\_PayandSaveExample

Code snippet

```
{
  "reference_id": "order_123456_SAVE",
  "customer": {
    "reference_id": "cust_Lorem_Ipsum",
    "type": "INDIVIDUAL",
    "email": "test@yourdomain.com",
    "mobile_number": "+6212345678",
    "individual_detail": {
      "given_names": "Lorem",
      "surname": "Ipsum"
    }
  },
  "items": [
    {
      "reference_id": "item_001",
      "name": "Clothes",
      "description": "Red clothes",
      "type": "PHYSICAL_PRODUCT",
      "category": "CLOTHES",
      "net_unit_amount": 5000,
      "quantity": 1,
      "currency": "PHP",
      "url": "https://example.com/item"
    },
    {
      "reference_id": "item_002",
      "name": "Pants",
      "description": "Black pants",
      "type": "PHYSICAL_PRODUCT",
      "category": "CLOTHES",
      "net_unit_amount": 5000,
      "quantity": 1,
      "currency": "PHP",
      "url": "https://example.com/item"
    }
  ],
  "session_type": "PAY",
  "currency": "PHP",
  "amount": 10000,
  "mode": "PAYMENT_LINK",
  "allow_save_payment_method": "OPTIONAL",
  "country": "PH",
  "locale": "en",
  "description": "Sample of pay and save flow using Payment Session",
  "success_return_url": "https://yourcompany.com/success/example_item=my_item",
  "cancel_return_url": "https://yourcompany.com/cancel/example_item=my_item"
}
```

JSON

Copy

PaymentLink\_SavePaymentMethodExample

Code snippet

```
{
  "reference_id": "order_123456_SAVE",
  "customer": {
    "reference_id": "cust_Lorem_Ipsum",
    "type": "INDIVIDUAL",
    "email": "test@yourdomain.com",
    "mobile_number": "+6212345678",
    "individual_detail": {
      "given_names": "Lorem",
      "surname": "Ipsum"
    }
  },
  "session_type": "SAVE",
  "currency": "IDR",
  "amount": 0,
  "mode": "PAYMENT_LINK",
  "country": "ID",
  "locale": "en",
  "description": "Insurance Plan Registration",
  "success_return_url": "https://yourcompany.com/success/example_item=my_item",
  "cancel_return_url": "https://yourcompany.com/cancel/example_item=my_item"
}
```

JSON

Copy

PaymentLink\_ManualCaptureExample

Code snippet

```
{
  "reference_id": "order_12345_PAY",
  "session_type": "PAY",
  "mode": "PAYMENT_LINK",
  "amount": 10000,
  "currency": "PHP",
  "country": "PH",
  "customer": {
    "reference_id": "cust_Lorem_Ipsum",
    "type": "INDIVIDUAL",
    "email": "test@yourdomain.com",
    "mobile_number": "+6212345678",
    "individual_detail": {
      "given_names": "Lorem",
      "surname": "Ipsum"
    }
  },
  "capture_method": "MANUAL",
  "locale": "en",
  "description": "Sample of authorization and manual capture flow using Payment Session",
  "success_return_url": "https://yourcompany.com/success/example_item=my_item",
  "cancel_return_url": "https://yourcompany.com/cancel/example_item=my_item"
}
```

JSON

Copy

XenditComponents\_OneTimePaymentExample

Code snippet

```
{
  "reference_id": "order_12345_PAY",
  "session_type": "PAY",
  "mode": "COMPONENTS",
  "amount": 10000,
  "currency": "PHP",
  "country": "PH",
  "locale": "en",
  "customer": {
    "reference_id": "cust_Lorem_Ipsum",
    "type": "INDIVIDUAL",
    "email": "test@yourdomain.com",
    "mobile_number": "+6212345678",
    "individual_detail": {
      "given_names": "Lorem",
      "surname": "Ipsum"
    }
  },
  "items": [
    {
      "reference_id": "item_001",
      "name": "Clothes",
      "description": "Red clothes",
      "type": "PHYSICAL_PRODUCT",
      "category": "CLOTHES",
      "net_unit_amount": 5000,
      "quantity": 1,
      "currency": "PHP",
      "url": "https://example.com/item"
    },
    {
      "reference_id": "item_002",
      "name": "Pants",
      "description": "Black pants",
      "type": "PHYSICAL_PRODUCT",
      "category": "CLOTHES",
      "net_unit_amount": 5000,
      "quantity": 1,
      "currency": "PHP",
      "url": "https://example.com/item"
    }
  ],
  "description": "Sample one-time payment using Xendit Components",
  "components_configuration": {
    "origins": [
      "https://yourcompany.com"
    ]
  }
}
```

JSON

Copy

XenditComponents\_PayandSaveExample

Code snippet

```
{
  "reference_id": "order_123456_SAVE",
  "customer": {
    "reference_id": "cust_Lorem_Ipsum",
    "type": "INDIVIDUAL",
    "email": "test@yourdomain.com",
    "mobile_number": "+6212345678",
    "individual_detail": {
      "given_names": "Lorem",
      "surname": "Ipsum"
    }
  },
  "items": [
    {
      "reference_id": "item_001",
      "name": "Clothes",
      "description": "Red clothes",
      "type": "PHYSICAL_PRODUCT",
      "category": "CLOTHES",
      "net_unit_amount": 5000,
      "quantity": 1,
      "currency": "PHP",
      "url": "https://example.com/item"
    },
    {
      "reference_id": "item_002",
      "name": "Pants",
      "description": "Black pants",
      "type": "PHYSICAL_PRODUCT",
      "category": "CLOTHES",
      "net_unit_amount": 5000,
      "quantity": 1,
      "currency": "PHP",
      "url": "https://example.com/item"
    }
  ],
  "session_type": "PAY",
  "currency": "PHP",
  "amount": 10000,
  "mode": "COMPONENTS",
  "allow_save_payment_method": "OPTIONAL",
  "country": "PH",
  "locale": "en",
  "description": "Sample of pay and save flow using Payment Session",
  "components_configuration": {
    "origins": [
      "https://yourcompany.com"
    ]
  }
}
```

JSON

Copy

XenditComponents\_SavePaymentMethodExample

Code snippet

```
{
  "reference_id": "registration_123456_SAVE",
  "session_type": "SAVE",
  "mode": "COMPONENTS",
  "amount": 0,
  "currency": "PHP",
  "country": "PH",
  "customer": {
    "reference_id": "cust_Lorem_Ipsum",
    "type": "INDIVIDUAL",
    "email": "test@yourdomain.com",
    "mobile_number": "+6212345678",
    "individual_detail": {
      "given_names": "Lorem",
      "surname": "Ipsum"
    }
  },
  "locale": "en",
  "description": "Insurance Plan Registration",
  "components_configuration": {
    "origins": [
      "https://yourcompany.com"
    ]
  }
}
```

JSON

Copy

XenditComponents\_ManualCaptureExample

Code snippet

```
{
  "reference_id": "order_12345_PAY",
  "session_type": "PAY",
  "mode": "COMPONENTS",
  "amount": 10000,
  "currency": "PHP",
  "country": "PH",
  "locale": "en",
  "customer": {
    "reference_id": "cust_Lorem_Ipsum",
    "type": "INDIVIDUAL",
    "email": "test@yourdomain.com",
    "mobile_number": "+6212345678",
    "individual_detail": {
      "given_names": "Lorem",
      "surname": "Ipsum"
    }
  },
  "capture_method": "MANUAL",
  "description": "Sample of authorization and manual capture flow using Xendit Components",
  "components_configuration": {
    "origins": [
      "https://yourcompany.com"
    ]
  }
}
```

JSON

Copy

PaymentLink\_SubscriptionExample

Code snippet

```
{
  "reference_id": "subscription_12345",
  "session_type": "SUBSCRIPTION",
  "mode": "PAYMENT_LINK",
  "amount": 50000,
  "currency": "PHP",
  "country": "PH",
  "customer": {
    "reference_id": "cust_Lorem_Ipsum",
    "type": "INDIVIDUAL",
    "email": "test@yourdomain.com",
    "mobile_number": "+6212345678",
    "individual_detail": {
      "given_names": "Lorem",
      "surname": "Ipsum"
    }
  },
  "locale": "en",
  "description": "Monthly subscription plan",
  "subscription": {
    "schedule": {
      "interval": "MONTH",
      "interval_count": 1,
      "total_recurrence": 12,
      "anchor_date": "2026-05-01",
      "retry_interval": "DAY",
      "retry_interval_count": 1,
      "total_retry": 3,
      "failed_attempt_notifications": [
        1,
        2,
        3
      ]
    },
    "failed_cycle_action": "RESUME"
  },
  "success_return_url": "https://yourcompany.com/success/example_item=my_item",
  "cancel_return_url": "https://yourcompany.com/cancel/example_item=my_item"
}
```

JSON

Copy

XenditComponents\_SubscriptionExample

Code snippet

```
{
  "reference_id": "subscription_12345",
  "session_type": "SUBSCRIPTION",
  "mode": "COMPONENTS",
  "amount": 50000,
  "currency": "PHP",
  "country": "PH",
  "customer": {
    "reference_id": "cust_Lorem_Ipsum",
    "type": "INDIVIDUAL",
    "email": "test@yourdomain.com",
    "mobile_number": "+6212345678",
    "individual_detail": {
      "given_names": "Lorem",
      "surname": "Ipsum"
    }
  },
  "locale": "en",
  "description": "Monthly subscription plan",
  "subscription": {
    "schedule": {
      "interval": "MONTH",
      "interval_count": 1,
      "total_recurrence": 12,
      "anchor_date": "2026-05-01",
      "retry_interval": "DAY",
      "retry_interval_count": 1,
      "total_retry": 3,
      "failed_attempt_notifications": [
        1,
        2,
        3
      ]
    },
    "failed_cycle_action": "RESUME"
  },
  "components_configuration": {
    "origins": [
      "https://yourcompany.com"
    ]
  }
}
```

JSON

Copy

Collapse all

object

reference\_id

string Required

Your reference to uniquely identify the Payment Session. This is commonly used to identify your order or transaction.

Min length1

Max length64

customer\_id

string

A unique identifier automatically generated by Xendit to represent an end customer. This ID can be used as a consistent reference across multiple transactions or payment activities for the same user. You can create a customer object in advance through the Create Customer API here: <https://xendit-docs.document360.io/apidocs/create-customer-request>

Min length41

Max length41

Examplecust-b98d6f63-d240-44ec-9bd5-aa42954c4f48

customer

object (Payment\_Session\_CustomerDetails)

type

string Required

Type of customer

Valid values[
"INDIVIDUAL"
]

reference\_id

string Required

Merchant provided identifier for the customer. Must be unique. Alphanumeric no special characters allowed

Min length1

Max length255

email

string (email)

E-mail address of customer. Maximum length 50 characters

Min length4

Max length50

mobile\_number

string

Mobile number of customer in E.164 format +(country code)(subscriber number)

Min length1

Max length50

individual\_detail

object (Payment\_Session\_XenditStandardIndividualDetail) Required

given\_names

string Required

Primary or first name/s of customer. Alphanumeric. No special characters is allowed.

Min length1

Max length50

surname

string

Last or family name of customer. Alphanumeric. No special characters is allowed.

Min length1

Max length50

nationality

string

Country code for customer nationality. ISO 3166-1 alpha-2 Country Code

Min length2

Max length2

place\_of\_birth

string

City or other relevant location for the customer birth place. Alphanumeric. No special characters is allowed.

Min length1

Max length60

date\_of\_birth

string

Date of birth of the customer. Format: YYYY-MM-DD

Min length10

Max length10

gender

Gender of customer

Valid values[
"MALE",
"FEMALE",
"OTHER"
]

session\_type

string Required

The use case for Payment Session.
SAVE: save the payment details from a customer for future payments.
PAY: collects a one-time payment from a customer.
SUBSCRIPTION: register a subscription payment for your customer using Xendit Subscription product, see here <https://docs.xendit.co/docs/subscriptions-overview>.

Valid values[
"SAVE",
"PAY",
"SUBSCRIPTION"
]

allow\_save\_payment\_method

string

The option to save the payment details from a customer for the PAY session\_type.
Saved payment details can be used for future payments.
DISABLED: does not save the payment details.
OPTIONAL: allows the customer to opt-in to save the payment details.
FORCED: always save the payment details.

Valid values[
"DISABLED",
"OPTIONAL",
"FORCED"
]

currency

string Required

ISO 4217 three-letter currency code for the payment.

Valid values[
"IDR",
"PHP",
"VND",
"THB",
"SGD",
"MYR",
"USD"
]

ExampleIDR

amount

number Required

The payment amount to be collected from the customer.
For SAVE session\_type, the amount must be 0.

Minimum0.0

Example10000.0

mode

string Required

The frontend integration mode for Payment Session.
PAYMENT\_LINK: redirect the customer to the Xendit Hosted Checkout page.
COMPONENTS: collect payment details from customer with Xendit Component SDK.

Valid values[
"PAYMENT\_LINK",
"COMPONENTS"
]

capture\_method

string

The method to capture the payment.
AUTOMATIC: capture the payment automatically.
MANUAL: capture the payment manually using Payment Capture API

Valid values[
"AUTOMATIC",
"MANUAL"
]

country

string Required

ISO 3166-1 alpha-2 two-letter country code for the country of transaction.

Valid values[
"ID",
"PH",
"VN",
"TH",
"SG",
"MY"
]

ExampleID

channel\_properties

object (Payment\_Session\_ChannelProperties)

Optional channel specific properties to be sent to specific payment channel provider.

allowed\_payment\_channels

Array of string

Specify the list of payment channels for your customer to select from the Xendit Hosted Checkout page.
By default all payment channels will be available if you leave this field empty.

Example[
"CARDS",
"BRI\_DIRECT\_DEBIT",
"DANA"
]

string

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

metadata

object (Payment\_Session\_MerchantMetadata) | null

Key-value entries for your custom data/information.
You can specify up to 50 keys, with key names up to 40 characters and values up to 500 characters.
This is commonly used for your internal reference or reconciliation purposes. Xendit will not use this data for any processing.

Example{
"my\_custom\_id": "merchant-123",
"my\_custom\_order\_id": "order-123"
}

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

notification\_channels

Array of string

The list of notification channels to be used for the session.

string

Valid values[
"EMAIL"
]

subscription

object (Payment\_Session\_SubscriptionPublic) | null

Subscription object for the session.

schedule

object (Payment\_Session\_SubscriptionSchedule) Required

The schedule for the subscription.

interval

string Required

The interval for the subscription.

Valid values[
"DAY",
"WEEK",
"MONTH"
]

interval\_count

integer Required

The number of intervals between each subscription payment.

Minimum1.0

total\_recurrence

integer

The total number of payments to be made for the subscription.

Minimum1.0

anchor\_date

string (date-time) Required

The date to start the subscription from. Max allowed day of the month is 28. Supports time offset and UTC zero

retry\_interval

string

The interval to wait before retrying a failed payment.

Valid values[
"DAY",
"WEEK",
"MONTH"
]

retry\_interval\_count

integer

The number of intervals to wait before retrying a failed payment.

Minimum1.0

total\_retry

integer

The total number of retries to be made for a failed payment.

Minimum1.0

failed\_attempt\_notifications

Array of integer

The list of failed attempt numbers to send notifications for.

integer

Minimum1.0

payment\_link\_for\_failed\_attempt

boolean

Whether to create a payment link for failed attempts.

failed\_cycle\_action

string

Whether to resume or stop the subscription after a failed payment.

Valid values[
"RESUME",
"STOP"
]

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

Responses

201

4XX

5XX

Show example

Session Created

application/json

createSessionResponseExample

createSessionResponseExample

Code snippet

```
{
  "payment_session_id": "ps-661f87c614802d6c402cd82d",
  "created": "2021-12-31T23:59:59Z",
  "updated": "2021-12-31T23:59:59Z",
  "reference_id": "Alice",
  "customer_id": "cust-e2878b4c-d57e-4a2c-922d-c0313c2800a3",
  "session_type": "SAVE",
  "currency": "IDR",
  "amount": 0,
  "country": "ID",
  "mode": "PAYMENT_LINK",
  "channel_properties": {},
  "allowed_payment_channels": [
    "OVO",
    "DANA"
  ],
  "expires_at": "2021-12-31T23:59:59Z",
  "locale": "en",
  "description": "Insurance Plan Registration",
  "success_return_url": "https://yourcompany.com/success/example_item=my_item",
  "cancel_return_url": "https://yourcompany.com/cancel/example_item=my_item",
  "items": null,
  "metadata": null,
  "status": "ACTIVE",
  "payment_link_url": "https://xen.to/kGxPCi60",
  "payment_token_id": null,
  "payment_request_id": null,
  "business_id": "661f87c614802d6c402cd82d"
}
```

JSON

Copy

Collapse all

object

payment\_session\_id

string

A unique identifier for the Payment Session

Min length27

Max length27

Exampleps-661f87c614802d6c402cd82d

created

string (date-time)

Example2021-12-31T23:59:59Z

updated

string (date-time)

Example2021-12-31T23:59:59Z

reference\_id

string

Your reference to uniquely identify the Payment Session. This is commonly used to identify your order or transaction.

Min length1

Max length64

customer\_id

string

A unique identifier automatically generated by Xendit to represent an end customer. This ID can be used as a consistent reference across multiple transactions or payment activities for the same user. You can create a customer object in advance through the Create Customer API here: <https://xendit-docs.document360.io/apidocs/create-customer-request>

Min length41

Max length41

Examplecust-b98d6f63-d240-44ec-9bd5-aa42954c4f48

session\_type

string

The use case for Payment Session.
SAVE: save the payment details from a customer for future payments.
PAY: collects a one-time payment from a customer.
SUBSCRIPTION: register a subscription payment for your customer using Xendit Subscription product, see here <https://docs.xendit.co/docs/subscriptions-overview>.

Valid values[
"SAVE",
"PAY",
"SUBSCRIPTION"
]

allow\_save\_payment\_method

string

The option to save the payment details from a customer for the PAY session\_type.
Saved payment details can be used for future payments.
DISABLED: does not save the payment details.
OPTIONAL: allows the customer to opt-in to save the payment details.
FORCED: always save the payment details.

Valid values[
"DISABLED",
"OPTIONAL",
"FORCED"
]

currency

string

ISO 4217 three-letter currency code for the payment.

Valid values[
"IDR",
"PHP",
"VND",
"THB",
"SGD",
"MYR",
"USD"
]

ExampleIDR

amount

number

The payment amount to be collected from the customer.
For SAVE session\_type, the amount must be 0.

Minimum0.0

Example10000.0

country

string

ISO 3166-1 alpha-2 two-letter country code for the country of transaction.

Valid values[
"ID",
"PH",
"VN",
"TH",
"SG",
"MY"
]

ExampleID

mode

string

The frontend integration mode for Payment Session.
PAYMENT\_LINK: redirect the customer to the Xendit Hosted Checkout page.
COMPONENTS: collect payment details from customer with Xendit Component SDK.

Valid values[
"PAYMENT\_LINK",
"COMPONENTS"
]

capture\_method

string

The method to capture the payment.
AUTOMATIC: capture the payment automatically.
MANUAL: capture the payment manually using Payment Capture API

Valid values[
"AUTOMATIC",
"MANUAL"
]

channel\_properties

object (Payment\_Session\_ChannelProperties)

Optional channel specific properties to be sent to specific payment channel provider.

allowed\_payment\_channels

Array of string

Specify the list of payment channels for your customer to select from the Xendit Hosted Checkout page.
By default all payment channels will be available if you leave this field empty.

Example[
"CARDS",
"BRI\_DIRECT\_DEBIT",
"DANA"
]

string

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

metadata

object (Payment\_Session\_MerchantMetadata) | null

Key-value entries for your custom data/information.
You can specify up to 50 keys, with key names up to 40 characters and values up to 500 characters.
This is commonly used for your internal reference or reconciliation purposes. Xendit will not use this data for any processing.

Example{
"my\_custom\_id": "merchant-123",
"my\_custom\_order\_id": "order-123"
}

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

string

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

string

Name of item

Min length1

Max length255

net\_unit\_amount

number

Net amount to be charged per unit

quantity

integer

Number of units of this item in the basket

Minimum1.0

url

string

URL of the item. Must be HTTPS or HTTP

image\_url

string

URL of the image of the item. Must be HTTPS or HTTP

category

string

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

status

string

The status of the Payment Session.

Valid values[
"ACTIVE",
"COMPLETED",
"EXPIRED",
"CANCELED"
]

notification\_channels

Array of string

The list of notification channels to be used for the session.

string

Valid values[
"EMAIL"
]

subscription

object (Payment\_Session\_SubscriptionPublic) | null

Subscription object for the session.

schedule

object (Payment\_Session\_SubscriptionSchedule)

The schedule for the subscription.

interval

string

The interval for the subscription.

Valid values[
"DAY",
"WEEK",
"MONTH"
]

interval\_count

integer

The number of intervals between each subscription payment.

Minimum1.0

total\_recurrence

integer

The total number of payments to be made for the subscription.

Minimum1.0

anchor\_date

string (date-time)

The date to start the subscription from. Max allowed day of the month is 28. Supports time offset and UTC zero

retry\_interval

string

The interval to wait before retrying a failed payment.

Valid values[
"DAY",
"WEEK",
"MONTH"
]

retry\_interval\_count

integer

The number of intervals to wait before retrying a failed payment.

Minimum1.0

total\_retry

integer

The total number of retries to be made for a failed payment.

Minimum1.0

failed\_attempt\_notifications

Array of integer

The list of failed attempt numbers to send notifications for.

integer

Minimum1.0

payment\_link\_for\_failed\_attempt

boolean

Whether to create a payment link for failed attempts.

failed\_cycle\_action

string

Whether to resume or stop the subscription after a failed payment.

Valid values[
"RESUME",
"STOP"
]

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

payment\_request\_id

string | null

Xendit Payment Request ID used to reference the payment made during this Session.

Examplepr-0800fe40-bb79-47ae-9d1e-e69394d3949c

business\_id

string

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

Show example

Error response for POST /sessions. Possible HTTP status codes: 400, 401, 404, 409.

application/json

apiValidationError
invalidAmount
invalidPaymentChannel
invalidPrimaryPaymentChannel
invalidMetadata
invalidItemMetadata
invalidCustomerId
invalidUrl
missingCustomer
disallowedCaptureMethod
invalidExpiryDate
itemsNotSupported
sessionTypeNotSupported
modeNotSupported
invalidApiKey
dataNotFound
duplicateError

apiValidationError

400 - Missing required field

Code snippet

```
{
  "error_code": "API_VALIDATION_ERROR",
  "message": "request/body must have required property 'session_type'",
  "errors": [
    {
      "message": "must have required property 'session_type'",
      "path": "/body/session_type"
    }
  ]
}
```

JSON

Copy

invalidAmount

400 - Amount must be greater than zero

Code snippet

```
{
  "error_code": "INVALID_AMOUNT",
  "message": "Amount must be greater than zero"
}
```

JSON

Copy

invalidPaymentChannel

400 - Payment channel not available

Code snippet

```
{
  "error_code": "INVALID_PAYMENT_CHANNEL",
  "message": "Channel(s) INVALID_CHANNEL are not available. Please ensure that you have activated the necessary channels"
}
```

JSON

Copy

invalidPrimaryPaymentChannel

400 - Primary channel not in allowed channels

Code snippet

```
{
  "error_code": "INVALID_PRIMARY_PAYMENT_CHANNEL",
  "message": "Primary channel BPI_DIRECT_DEBIT is not included in the requested channels"
}
```

JSON

Copy

invalidMetadata

400 - Metadata value exceeds limit

Code snippet

```
{
  "error_code": "INVALID_METADATA",
  "message": "Metadata value must have at most 80 characters"
}
```

JSON

Copy

invalidItemMetadata

400 - Item metadata value exceeds limit

Code snippet

```
{
  "error_code": "INVALID_ITEM_METADATA",
  "message": "Metadata value must have at most 80 characters"
}
```

JSON

Copy

invalidCustomerId

400 - Customer ID format invalid

Code snippet

```
{
  "error_code": "INVALID_CUSTOMER_ID",
  "message": "Customer ID must start with \"cust-\""
}
```

JSON

Copy

invalidUrl

400 - Invalid URL format

Code snippet

```
{
  "error_code": "INVALID_URL",
  "message": "Please provide a valid HTTPS URL"
}
```

JSON

Copy

missingCustomer

400 - Customer required but not provided

Code snippet

```
{
  "error_code": "MISSING_CUSTOMER",
  "message": "Customer object or customer_id is required"
}
```

JSON

Copy

disallowedCaptureMethod

400 - Capture method not allowed for session type

Code snippet

```
{
  "error_code": "DISALLOWED_CAPTURE_METHOD",
  "message": "Capture method is not supported for session type SAVE"
}
```

JSON

Copy

invalidExpiryDate

400 - Expiry date is invalid

Code snippet

```
{
  "error_code": "INVALID_EXPIRY_DATE",
  "message": "expires_at must be at least 10 minutes in the future"
}
```

JSON

Copy

itemsNotSupported

400 - Items not allowed for session type

Code snippet

```
{
  "error_code": "ITEMS_NOT_SUPPORTED",
  "message": "Items are allowed for session type PAY only"
}
```

JSON

Copy

sessionTypeNotSupported

400 - Session type not supported

Code snippet

```
{
  "error_code": "SESSION_TYPE_NOT_SUPPORTED",
  "message": "session_type AUTHORIZATION is not supported for now"
}
```

JSON

Copy

modeNotSupported

400 - Mode not supported

Code snippet

```
{
  "error_code": "MODE_NOT_SUPPORTED",
  "message": "mode INVALID_MODE is not supported for now"
}
```

JSON

Copy

invalidApiKey

401 - Invalid API key

Code snippet

```
{
  "error_code": "INVALID_API_KEY",
  "message": "API key is not authorized for this API"
}
```

JSON

Copy

dataNotFound

404 - Customer ID does not exist

Code snippet

```
{
  "error_code": "DATA_NOT_FOUND",
  "message": "The customer ID provided in the request does not exist"
}
```

JSON

Copy

duplicateError

409 - Duplicate customer reference\_id

Code snippet

```
{
  "error_code": "DUPLICATE_ERROR",
  "message": "customer: The reference_id entered has been used before. Please enter a unique reference_id"
}
```

JSON

Copy

object

error\_code

string

400 error codes:

- `API_VALIDATION_ERROR` - Generic request validation failure such as missing required fields, invalid enum values, invalid field formats, or constraint violations (e.g. missing `session_type`, invalid `allow_save_payment_method` value, missing `cards_session_js` properties, invalid `components_configuration.origins`, missing `subscription.schedule` fields, `card_details` not allowed on `channel_properties.cards`, `recurring_configuration` required when `card_on_file_type` is RECURRING or MERCHANT\_UNSCHEDULED, `internal_metadata` not allowed).
- `INVALID_AMOUNT` - Amount validation failed. For PAY/SUBSCRIPTION session types, amount must be greater than zero. For SAVE session type, amount must be zero. Amount must also respect the decimal places allowed for the given currency.
- `INVALID_PAYMENT_CHANNEL` - One or more requested payment channels are not recognized, not activated for your account, not supported for the requested session configuration, or no channels are available for the given `capture_method`, `allow_save_payment_method`, or country/currency combination.
- `INVALID_PRIMARY_PAYMENT_CHANNEL` - A channel specified in `payment_link_configuration.primary_payment_channels` is not included in `allowed_payment_channels`.
- `INVALID_METADATA` - Session-level metadata validation failed. Metadata supports a maximum of 20 keys, each key up to 40 characters, each value must be a string of up to 80 characters.
- `INVALID_ITEM_METADATA` - Item-level metadata validation failed. Same constraints as session-level metadata.
- `INVALID_COUNTRY` - The provided `country` is not supported.
- `INVALID_CURRENCY` - The provided `currency` is not supported.`
- `INVALID_CUSTOMER_ID` - The provided `customer_id` does not start with the required `cust-` prefix.
- `INVALID_URL` - A URL field (e.g. `success_return_url`, `cancel_return_url`) is not a valid HTTPS URL.
- `MISSING_CUSTOMER` - A `customer` object or `customer_id` is required but was not provided. Required when `session_type` is SAVE, when `mode` is CARDS\_SESSION\_JS, or when `allow_save_payment_method` is FORCED or OPTIONAL.
- `DISALLOWED_CAPTURE_METHOD` - `capture_method` was provided for a session type that does not support it (e.g. SAVE or SUBSCRIPTION).
- `INVALID_EXPIRY_DATE` - The provided `expires_at` value is invalid. It must be at least 10 minutes in the future and must not exceed the maximum allowed expiry duration.
- `ITEMS_NOT_SUPPORTED` - `items` were provided for a session type other than PAY.
- `SESSION_TYPE_NOT_SUPPORTED` - The provided `session_type` is not supported (e.g. AUTHORIZATION).
- `MODE_NOT_SUPPORTED` - The provided `mode` is not supported.

401 error codes:

- `INVALID_API_KEY` - The API key provided is invalid or missing.

404 error codes:

- `DATA_NOT_FOUND` - The `customer_id` provided in the request does not exist.

409 error codes:

- `DUPLICATE_ERROR` - A customer with the same `reference_id` already exists for a different business.

Valid values[
"API\_VALIDATION\_ERROR",
"INVALID\_AMOUNT",
"INVALID\_PAYMENT\_CHANNEL",
"INVALID\_PRIMARY\_PAYMENT\_CHANNEL",
"INVALID\_METADATA",
"INVALID\_ITEM\_METADATA",
"INVALID\_CURRENCY",
"INVALID\_COUNTRY",
"INVALID\_CUSTOMER\_ID",
"INVALID\_URL",
"MISSING\_CUSTOMER",
"DISALLOWED\_CAPTURE\_METHOD",
"INVALID\_EXPIRY\_DATE",
"ITEMS\_NOT\_SUPPORTED",
"SESSION\_TYPE\_NOT\_SUPPORTED",
"MODE\_NOT\_SUPPORTED",
"INVALID\_API\_KEY",
"DATA\_NOT\_FOUND",
"DUPLICATE\_ERROR"
]

message

string

Human-readable description of the error.

errors

Array

OneOf

string

string

object

object

Show example

Internal Server Error

application/json

serverError

serverError

500 - Internal server error

Code snippet

```
{
  "error_code": "SERVER_ERROR",
  "message": "Something unexpected happened. We are investigating this issue. Please try again later."
}
```

JSON

Copy

object

error\_code

string

- `SERVER_ERROR` - Something unexpected happened. Please try again later.

Valid values[
"SERVER\_ERROR"
]

message

string

Human-readable description of the error.

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

Payment token webhook notification

Next article

Get the status of a session

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

for-user-id

with-split-rule

Body

application/json

application/json

PaymentLink\_OneTimePaymentExample

PaymentLink\_OneTimePaymentExample

PaymentLink\_PayandSaveExample

PaymentLink\_SavePaymentMethodExample

PaymentLink\_ManualCaptureExample

XenditComponents\_OneTimePaymentExample

XenditComponents\_PayandSaveExample

XenditComponents\_SavePaymentMethodExample

XenditComponents\_ManualCaptureExample

PaymentLink\_SubscriptionExample

XenditComponents\_SubscriptionExample

 Reset to default

 

47

```
  "success_return_url": "https://yourcompany.com/success/example_item=my_item",
```

1

```
{
```

2

```
  "reference_id": "order_12345_PAY",
```

3

```
  "session_type": "PAY",
```

4

```
  "mode": "PAYMENT_LINK",
```

5

```
  "amount": 10000,
```

6

```
  "currency": "PHP",
```

7

```
  "country": "PH",
```

8

```
  "customer": {
```

9

```
    "reference_id": "cust_Lorem_Ipsum",
```

10

```
    "type": "INDIVIDUAL",
```

11

```
    "email": "test@yourdomain.com",
```

12

```
    "mobile_number": "+6212345678",
```

13

```
    "individual_detail": {
```

14

```
      "given_names": "Lorem",
```

15

```
      "surname": "Ipsum"
```

16

```
    }
```

17

```
  },
```

18

```
  "items": [
```

19

```
    {
```

20

```
      "reference_id": "item_001",
```

21

```
      "name": "Clothes",
```

22

```
      "description": "Red clothes",
```

23

```
      "type": "PHYSICAL_PRODUCT",
```

24

```
      "category": "CLOTHES",
```

 Try it & see response

Response

Available responses

application/json

application/json

2014XX5XX

 

```
 "payment_link_url": "https://checkout.xendit.co/sessions/ps-661f87c614802d6c402cd82d0 or https://xen.to/kGxPCi60. For test mode, https://checkout-staging.xendit.co/sessions/ps-661f87c614802d6c402cd82d0 or https://dev.xen.to/kGxPCi76",
```