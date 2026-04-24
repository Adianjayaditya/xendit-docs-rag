---
url: https://docs.xendit.co/apidocs/payment-token-webhook-notification
title: "Payment token webhook notification"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payments](/apidocs/introduction)
  - [Payment Token](/apidocs/create-payment-token)

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

post

 [Create a new payment token](/apidocs/create-payment-token)

get

 [Get the status of a payment token](/apidocs/get-payment-token)

post

 [Cancel and deactivate a payment token](/apidocs/cancel-payment-token)

post

 [Payment token webhook notification](/apidocs/payment-token-webhook-notification)

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

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Payment token webhook notification

- Updated on Apr 8, 2026
- Published on Jan 22, 2025

 [Prev](/apidocs/cancel-payment-token "Cancel and deactivate a payment token")  [Next](/apidocs/create-session "Create a session") 

Post

/your\_payment\_token\_webhook\_url

Webhook notification that will be sent to your defined webhook url for updates to payment token status.

Header parameters

x-callback-token

string

Your Xendit unique webhook token to verify the origin of the webhook. It is highly recommended for your integration to verify this value.

Body parameters

Payment Token status callback

Show example

application/json

Code snippet

```
{
  "tokenActivation": {
    "value": {
      "event": "payment_token.activation",
      "business_id": "6094fa76c2fd53701b8e079c",
      "created": "2021-12-02T14:52:21.566Z",
      "data": {
        "payment_token_id": "pt-1402feb0-bb79-47ae-9d1e-e69394d3949c",
        "business_id": "5f27a14a9bf05c73dd040bc8",
        "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
        "customer_id": "cust-b98d6f63-d240-44ec-9bd5-aa42954c4f48",
        "country": "ID",
        "currency": "IDR",
        "channel_code": "OVO",
        "channel_properties": {
          "failure_return_url": "https://xendit.co/failure",
          "success_return_url": "https://xendit.co/success"
        },
        "actions": [
          {
            "type": "REDIRECT_CUSTOMER",
            "descriptor": "WEB_URL",
            "value": "https://xendit.co/"
          }
        ],
        "status": "ACTIVE",
        "token_details": {
          "account_name": "John Doe",
          "account_balance": "1000001",
          "account_point_balance": "50000"
        },
        "metadata": {
          "invoice_id": "INV-2025-001",
          "customer_type": "business"
        },
        "created": "2029-12-31T23:59:59Z",
        "updated": "2029-12-31T23:59:59Z"
      }
    }
  },
  "tokenFailure": {
    "value": {
      "event": "payment_token.failure",
      "business_id": "6094fa76c2fd53701b8e079c",
      "created": "2021-12-02T14:52:21.566Z",
      "data": {
        "payment_token_id": "pt-1402feb0-bb79-47ae-9d1e-e69394d3949c",
        "business_id": "5f27a14a9bf05c73dd040bc8",
        "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
        "customer_id": "cust-b98d6f63-d240-44ec-9bd5-aa42954c4f48",
        "country": "ID",
        "currency": "IDR",
        "channel_code": "OVO",
        "channel_properties": {
          "failure_return_url": "https://xendit.co/failure",
          "success_return_url": "https://xendit.co/success"
        },
        "actions": [
          {
            "type": "REDIRECT_CUSTOMER",
            "descriptor": "WEB_URL",
            "value": "https://xendit.co/"
          }
        ],
        "status": "FAILED",
        "metadata": {
          "invoice_id": "INV-2025-001",
          "customer_type": "business"
        },
        "created": "2029-12-31T23:59:59Z",
        "updated": "2029-12-31T23:59:59Z"
      }
    }
  },
  "tokenExpiry": {
    "value": {
      "event": "payment_token.expiry",
      "business_id": "6094fa76c2fd53701b8e079c",
      "created": "2021-12-02T14:52:21.566Z",
      "data": {
        "payment_token_id": "pt-1402feb0-bb79-47ae-9d1e-e69394d3949c",
        "business_id": "5f27a14a9bf05c73dd040bc8",
        "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
        "customer_id": "cust-b98d6f63-d240-44ec-9bd5-aa42954c4f48",
        "country": "ID",
        "currency": "IDR",
        "channel_code": "OVO",
        "channel_properties": {
          "failure_return_url": "https://xendit.co/failure",
          "success_return_url": "https://xendit.co/success"
        },
        "actions": [
          {
            "type": "REDIRECT_CUSTOMER",
            "descriptor": "WEB_URL",
            "value": "https://xendit.co/"
          }
        ],
        "status": "EXPIRED",
        "token_details": {
          "account_name": "John Doe",
          "account_balance": "1000001",
          "account_point_balance": "50000"
        },
        "metadata": {
          "invoice_id": "INV-2025-001",
          "customer_type": "business"
        },
        "created": "2029-12-31T23:59:59Z",
        "updated": "2029-12-31T23:59:59Z"
      }
    }
  }
}
```

JSON

Copy

Collapse all

object

Payment Token status callback for binding

event

string

Webhook event names for payment token status updates.

Valid values[
"payment\_token.activation",
"payment\_token.failure",
"payment\_token.expiry"
]

business\_id

string

Xendit-generated identifier for the business that owns the transaction

Example5f27a14a9bf05c73dd040bc8

created

string (date-time)

Timestamp of webhook delivery attempt in ISO 8601 date-time format.

Example2021-12-31T23:59:59Z

data

object (Payments\_API\_PaymentTokenSchema)

Payment Token object

payment\_token\_id

string

Xendit unique Payment Token ID generated as reference for reusable payment details of the end user.

Examplept-cc3938dc-c2a5-43c4-89d7-7570793348c2

channel\_code

string

Channel code used to select the payment method provider.

country

string

ISO 3166-1 alpha-2 two-letter country code for the country of transaction.

Valid values[
"ID",
"PH",
"VN",
"TH",
"SG",
"MY",
"HK",
"MX"
]

ExampleID

business\_id

string

Xendit-generated identifier for the business that owns the transaction

Example5f27a14a9bf05c73dd040bc8

customer\_id

string

Xendit unique Capture ID generated as reference for the end user

Max length41

Examplecust-b98d6f63-d240-44ec-9bd5-aa42954c4f48

reference\_id

string

A Reference ID from merchants to identify their request.

Min length1

Max length255

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
"USD",
"HKD",
"AUD",
"GBP",
"EUR",
"JPY",
"MXN"
]

ExampleIDR

channel\_properties

object (Payments\_API\_ChannelProperties)

Data required to initiate transaction with payment method provider. Refer to the Channel Data Finder widget in the channel\_code field above for the full list of required properties for each channel.

actions

Array of object (Payments\_API\_Actions)

object

Actions object contains possible next steps merchants can take to proceed with payment collection from end user

type

The type of action that merchant system will need to handle to complete payment.

Valid values[
"PRESENT\_TO\_CUSTOMER",
"REDIRECT\_CUSTOMER",
"API\_POST\_REQUEST"
]

descriptor

The type of action that merchant system will need to handle to complete payment.

Valid values[
"CAPTURE\_PAYMENT",
"PAYMENT\_CODE",
"QR\_STRING",
"VIRTUAL\_ACCOUNT\_NUMBER",
"WEB\_URL",
"DEEPLINK\_URL",
"VALIDATE\_OTP",
"RESEND\_OTP"
]

value

string

The specific value that will be used by merchant to complete the action

status

string

Status of the payment token.

Valid values[
"REQUIRES\_ACTION",
"PENDING",
"ACTIVE",
"FAILED",
"EXPIRED",
"CANCELED"
]

ExampleACTIVE

token\_details

object (Payments\_API\_TokenDetails)

Account information provided by the payment method provider. Fields returned are dependent on what is made available by the provider.

authorization\_data

object (Payments\_API\_AuthorizationData)

Specific to cards transaction only. Details about the card authorization processing.

authorization\_code

string

Authorization approval code from the scheme. 6 alphanumeric characters.

cvn\_verification\_result

string

Whether CVN input matches with the issuer's data.

Valid values[
"M",
"N"
]

address\_verification\_result

string

Whether the end user's address input matches with the issuer's data.

Valid values[
"M",
"N"
]

retrieval\_reference\_number

string

Receipt reference number communicated to the end user by their card issuer for this specific payment. This a commonly used reference number for the end users to raise tickets.

network\_response\_code

string

The response code returned by the scheme (Visa, Mastercard, JCB, China Unionpay or Amex).

network\_response\_code\_descriptor

string

Description of the response code.

network\_transaction\_id

string

Transaction ID received from the card scheme. Only available for merchants on switcher model.

acquirer\_merchant\_id

string

Acquirer's record of the MID that was used to process this transaction. Only available for merchants on switcher model.

reconciliation\_id

string

Acquirer's transaction record of the payment on their settlement statement. Only available for merchants on switcher model.

authentication\_data

object (Payments\_API\_AuthenticationData)

Specific to cards transaction only. Details about the card authentication.

flow

string

Indicates the flow that was used for the 3DS authentication.

Valid values[
"FULL\_AUTH",
"FRICTIONLESS"
]

a\_res

object

Details about the card authentication response from the 3DS server.

eci

string

Payment system-specific value provided by the ACS or DS to indicate the results of the attempt to authenticate the Cardholder.

message\_version

string

The 3DS protocol version which has been used to perform 3DS.

authentication\_value

string

The result value from the 3DS transaction received from the ACS. This value is no longer present on responses after 45 days have passed after the authentication. Note that Mastercard and Visa use a different underlying format.

ds\_trans\_id

string

Universally unique transaction identifier assigned by the DS to identify a single transaction.

account\_name

string

Name of the owner of the account bound to the token.

account\_balance

string

Balance of the account bound to the token.

account\_point\_balance

string

Point balance of the account bound to the token.

account\_number

string

Account number bound to the token.

failure\_code

string

Failure codes for payment tokens.

Valid values[
"ACCOUNT\_ALREADY\_LINKED",
"INVALID\_ACCOUNT\_DETAILS",
"AUTHENTICATION\_FAILED",
"CARD\_DECLINED",
"CAPTURE\_AMOUNT\_EXCEEDED ",
"INSUFFICIENT\_BALANCE",
"ISSUER\_UNAVAILABLE",
"CHANNEL\_UNAVAILABLE",
"INVALID\_MERCHANT\_SETTINGS"
]

ExampleAUTHENTICATION\_FAILED

description

string

A custom description for the Payment Request.

Min length1

Max length1000

ExamplePayment for your order #123

metadata

object (Payments\_API\_MerchantMetadata)

Key-value entries for your custom data.
You can specify up to 50 keys, with key names up to 40 characters and values up to 500 characters.
This is for your convenience. Xendit will not use this data for any processing.

Example{
"my\_custom\_id": "merchant-123",
"my\_custom\_order\_id": "order-123"
}

created

string (date-time)

ISO 8601 date-time format.

Example2021-12-31T23:59:59Z

updated

string (date-time)

ISO 8601 date-time format.

Example2021-12-31T23:59:59Z

Responses

200

OK

Was this article helpful?

Yes  No

Previous article

Cancel and deactivate a payment token

Next article

Create a session

- Try It
- Code samples

Request

URL

x-callback-token

Body

application/json

application/json

 

114

1

```
{
```

2

```
  "tokenActivation": {
```

3

```
    "value": {
```

4

```
      "event": "payment_token.activation",
```

5

```
      "business_id": "6094fa76c2fd53701b8e079c",
```

6

```
      "created": "2021-12-02T14:52:21.566Z",
```

7

```
      "data": {
```

8

```
        "payment_token_id": "pt-1402feb0-bb79-47ae-9d1e-e69394d3949c",
```

9

```
        "business_id": "5f27a14a9bf05c73dd040bc8",
```

10

```
        "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
```

11

```
        "customer_id": "cust-b98d6f63-d240-44ec-9bd5-aa42954c4f48",
```

12

```
        "country": "ID",
```

13

```
        "currency": "IDR",
```

14

```
        "channel_code": "OVO",
```

15

```
        "channel_properties": {
```

16

```
          "failure_return_url": "https://xendit.co/failure",
```

17

```
          "success_return_url": "https://xendit.co/success"
```

18

```
        },
```

19

```
        "actions": [
```

20

```
          {
```

21

```
            "type": "REDIRECT_CUSTOMER",
```

22

```
            "descriptor": "WEB_URL",
```

23

```
            "value": "https://xendit.co/"
```

24

```
          }
```

 Try it & see response

Response

Available responses

200

 

```
null
```