---
url: https://docs.xendit.co/apidocs/get-payment-token
title: "Get the status of a payment token"
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

# Get the status of a payment token

- Updated on Apr 8, 2026
- Published on Jan 9, 2025

 [Prev](/apidocs/create-payment-token "Create a new payment token")  [Next](/apidocs/cancel-payment-token "Cancel and deactivate a payment token") 

Get

/v3/payment\_tokens/{payment\_token\_id}

Retrieve the status of your payment token.

Security

HTTP

Type basic

Header parameters

api-version

string

Valid values[
"2024-11-11"
]

Path parameters

payment\_token\_id

stringRequired

Min length39

Max length39

Examplept-56ef1da0-6c92-490a-9ea8-803eaf404ce1

Responses

200

400

404

500

Show example

Fetch Payment Token Status

application/json

Get\_Payment\_Token\_Ewallet
Get\_Payment\_Token\_Cards

Get\_Payment\_Token\_Ewallet

Code snippet

```
{
  "payment_token_id": "pt-90392f42-d98a-49ef-a7f3-abcezas123",
  "business_id": "5f27a14a9bf05c73dd040bc8",
  "reference_id": "tokenize_ovo_user789",
  "customer_id": "cust-b98d6f63-d240-44ec-9bd5-aa42954c4f48",
  "country": "ID",
  "currency": "IDR",
  "channel_code": "OVO",
  "channel_properties": {
    "failure_return_url": "https://xendit.co/failure",
    "success_return_url": "https://xendit.co/success"
  },
  "status": "ACTIVE",
  "token_details": {
    "account_name": "John Doe",
    "account_balance": "1000001",
    "account_point_balance": "50000"
  },
  "description": "Save OVO account for future payments",
  "metadata": {
    "customer_id": "CUST789",
    "wallet_usage": "recurring"
  },
  "created": "2021-12-31T23:59:59Z",
  "updated": "2021-12-31T23:59:59Z"
}
```

JSON

Copy

Get\_Payment\_Token\_Cards

Code snippet

```
{
  "payment_token_id": "pt-1402feb0-bb79-47ae-9d1e-e69394d3949c",
  "business_id": "5f27a14a9bf05c73dd040bc8",
  "reference_id": "tokenize_card_user456",
  "customer_id": "cust-b98d6f63-d240-44ec-9bd5-aa42954c4f48",
  "country": "ID",
  "currency": "IDR",
  "channel_code": "CARDS",
  "channel_properties": {
    "card_details": {
      "type": "CREDIT",
      "issuer": "PT BANK MANDIRI",
      "country": "ID",
      "network": "VISA",
      "fingerprint": "61f632879e9e27001a8165b9",
      "masked_card_number": "5200****1005",
      "expiry_year": "2028",
      "expiry_month": "09",
      "cardholder_first_name": "Jane",
      "cardholder_last_name": "Doe",
      "cardholder_email": "jane.doe@example.com",
      "cardholder_phone_number": "+6212345678903"
    },
    "skip_three_ds": false,
    "failure_return_url": "https://xendit.co/failure",
    "success_return_url": "https://xendit.co/success"
  },
  "status": "ACTIVE",
  "token_details": {
    "authentication_data": {
      "flow": "FULL_AUTH",
      "a_res": {
        "eci": "05",
        "message_version": "02",
        "authentication_value": "AUTHVAR",
        "ds_trans_id": "sample_trans_id"
      }
    },
    "authorization_data": {
      "authorization_code": "A1B2C3",
      "cvn_verification_result": "M",
      "address_verification_result": "M"
    }
  },
  "description": "Save card for future payments",
  "metadata": {
    "customer_id": "CUST456",
    "card_usage": "subscription"
  },
  "created": "2021-12-31T23:59:59Z",
  "updated": "2021-12-31T23:59:59Z"
}
```

JSON

Copy

Collapse all

object

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

Bad request

application/json

OneOf

Payments\_API\_Http400ApiValidationError

object (Payments\_API\_Http400ApiValidationError)

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR"
]

message

string

Fields or values in the payment request does not comply with our API specification. Check the specific error message for debugging.

Not found

application/json

OneOf

Payments\_API\_Http404DataNotFound

object (Payments\_API\_Http404DataNotFound)

error\_code

string

Valid values[
"DATA\_NOT\_FOUND"
]

message

string

ID specified in request cannot be found.

Internal server error

application/json

OneOf

Payments\_API\_Http500ServerError

object (Payments\_API\_Http500ServerError)

error\_code

string

Valid values[
"SERVER\_ERROR"
]

message

string

An unexpected error occured, our team has been notified and will troubleshoot the issue

Was this article helpful?

Yes  No

Previous article

Create a new payment token

Next article

Cancel and deactivate a payment token

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

payment\_token\_id \*

api-version 

2024-11-11 

-  2024-11-11

 Try it & see response

Response

Available responses

application/json

application/json

200400404500

 

```
 "payment_token_id": "pt-cc3938dc-c2a5-43c4-89d7-7570793348c2",
```