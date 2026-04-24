---
url: https://docs.xendit.co/apidocs/capture-payment
title: "Capture a payment"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payments](/apidocs/introduction)
  - [Payment](/apidocs/get-payment)

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

get

 [Get the status of a payment](/apidocs/get-payment)

post

 [Cancel a payment](/apidocs/cancel-payment)

post

 [Capture a payment](/apidocs/capture-payment)

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

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Capture a payment

- Updated on Apr 8, 2026
- Published on Jan 9, 2025

 [Prev](/apidocs/cancel-payment "Cancel a payment")  [Next](/apidocs/create-payment-token "Create a new payment token") 

Post

/v3/payments/{payment\_id}/capture

Capture authorized payment. Completes payment collection.

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

payment\_id

stringRequired

Min length39

Max length39

Examplepy-cc3938dc-c2a5-43c4-89d7-7570793348c2

Body parameters

application/json

object

capture\_amount

number

The payment amount captured for this payment. Maximum capture amount can only be equal or lesser than the authorized amount value.

Minimum0.0

Example10000.0

Responses

200

400

403

404

500

503

Show example

Capture Payment Status

application/json

capturePaymentCards

capturePaymentCards

Code snippet

```
{
  "payment_id": "py-1402feb0-bb79-47ae-9d1e-e69394d3949c",
  "business_id": "5f27a14a9bf05c73dd040bc8",
  "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
  "payment_request_id": "pr-1102feb0-bb79-47ae-9d1e-e69394d3949c",
  "payment_token_id": "pt-cc3938dc-c2a5-43c4-89d7-7570793348c2",
  "customer_id": "cust-b98d6f63-d240-44ec-9bd5-aa42954c4f48",
  "type": "PAY",
  "country": "ID",
  "currency": "IDR",
  "request_amount": 1999.01,
  "capture_method": "AUTOMATIC",
  "channel_code": "CARDS",
  "channel_properties": {
    "mid_label": "CTV_TEST",
    "card_details": {
      "type": "CREDIT",
      "issuer": "BRI",
      "country": "ID",
      "network": "VISA",
      "fingerprint": "61f632879e9e27001a8165b9",
      "masked_card_number": "2222XXXXXXXX8888",
      "expiry_year": "2027",
      "expiry_month": "12",
      "cardholder_first_name": "John",
      "cardholder_last_name": "Doe",
      "cardholder_email": "john.doe@example.com",
      "cardholder_phone_number": "+6212345678904"
    },
    "skip_three_ds": false,
    "card_on_file_type": "CUSTOMER_UNSCHEDULED",
    "failure_return_url": "https://xendit.co/failure",
    "success_return_url": "https://xendit.co/success",
    "billing_information": {
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com",
      "phone_number": "+6212345678904",
      "city": "Singapore",
      "country": "SG",
      "postal_code": "644228",
      "street_line1": "Merlion Bay Sands Suites",
      "street_line2": "21-37",
      "province_state": "Singapore"
    },
    "statement_descriptor": "Goods & Services",
    "recurring_configuration": {
      "recurring_expiry": "2025-12-31",
      "recurring_frequency": 30
    }
  },
  "captures": [
    {
      "capture_timestamp": "2029-12-31T23:59:59Z",
      "capture_id": "cap-1502feb0-bb79-47ae-9d1e-e69394d3949c",
      "capture_amount": 1999.01
    }
  ],
  "status": "SUCCEEDED",
  "payment_details": {
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
      "address_verification_result": "M",
      "retrieval_reference_number": "akjsdiuh132127y9sacsdjn",
      "network_response_code": "00",
      "network_response_code_descriptor": "testing",
      "network_transaction_id": "dahskjdhiquh341",
      "acquirer_merchant_id": "alskdnuoqh341",
      "reconciliation_id": "oiajsdo1823938yrh2"
    }
  },
  "metadata": {
    "invoice_id": "INV-2025-001",
    "customer_type": "business"
  },
  "created": "2029-12-31T23:59:59Z",
  "updated": "2029-12-31T23:59:59Z"
}
```

JSON

Copy

Collapse all

object

Payment object

payment\_id

string

Xendit unique Payment ID generated as reference for a payment.

Examplepy-1402feb0-bb79-47ae-9d1e-e69394d3949c

business\_id

string

Xendit-generated identifier for the business that owns the transaction

Example5f27a14a9bf05c73dd040bc8

reference\_id

string

A Reference ID from merchants to identify their request.

Min length1

Max length255

payment\_request\_id

string

Xendit unique Payment Request ID generated as reference after creation of payment request.

Examplepr-1102feb0-bb79-47ae-9d1e-e69394d3949c

payment\_token\_id

string

Xendit unique Payment Token ID generated as reference for reusable payment details of the end user.

Examplept-cc3938dc-c2a5-43c4-89d7-7570793348c2

customer\_id

string

Xendit unique Capture ID generated as reference for the end user

Max length41

Examplecust-b98d6f63-d240-44ec-9bd5-aa42954c4f48

type

string

The payment collection intent type for the payment request.

PAY: Create a payment request that is able to receive one payment.

PAY\_AND\_SAVE: Create a payment request that is able to receive one payment. If the payment is successful, a reusable payment token will be returned for subsequent payment requests.

REUSABLE\_PAYMENT\_CODE: Create a payment request that is able to receive multiple payments. This is only used for repeat use payment method like a static QR, a predefined OTC payment code or a predefined Virtual Account number.

Valid values[
"PAY",
"PAY\_AND\_SAVE",
"REUSABLE\_PAYMENT\_CODE"
]

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

request\_amount

number

The intended payment amount to be collected from the end user.

Minimum0.0

Example10000.0

capture\_method

string

AUTOMATIC: payment capture will be processed immediately after payment request is created.
MANUAL: payment capture requires merchant's trigger via payment capture endpoint before being processed

Valid values[
"AUTOMATIC",
"MANUAL"
]

Default"AUTOMATIC"

ExampleAUTOMATIC

channel\_code

string

Channel code used to select the payment method provider.

captures

Array of object (Payments\_API\_Capture)

object

Capture object contains information about the capture that was performed

capture\_timestamp

string (date-time)

ISO 8601 date-time format.

Example2021-12-31T23:59:59Z

capture\_id

string

Xendit unique Capture ID generated as reference for a single capture.

Examplecap-1502feb0-bb79-47ae-9d1e-e69394d3949c

capture\_amount

number

The payment amount captured for this payment. Maximum capture amount can only be equal or lesser than the authorized amount value.

Minimum0.0

Example10000.0

status

string

Status of the payment.

Valid values[
"AUTHORIZED",
"CANCELED",
"SUCCEEDED",
"FAILED",
"EXPIRED",
"PENDING"
]

ExampleSUCCEEDED

payment\_details

object (Payments\_API\_PaymentDetails)

Payment information provided by the payment method provider. Fields returned are dependent on what is made available by the provider.

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

issuer\_name

string

Name of the payment method provider used by the end user.

payer\_account\_number

string

Account number of the end user making the payment from the payment method provider's records.

payer\_name

string

Name of the end user making the payment from the payment method provider's records.

receipt\_id

string

Receipt reference number communicated to the end user by their payment method provider for this specific payment. This a commonly used reference number for the end users to raise tickets.

remark

string

Remarks about this specific payment from the payment method provider's records.

network

string

Payment network which the payment was processed over.

fund\_source

string

Information about what was used by the end user to complete the payment. e.g. balance, installment, credit.

failure\_code

string

Failure codes for payments.

Valid values[
"ACCOUNT\_ACCESS\_BLOCKED",
"INVALID\_MERCHANT\_SETTINGS",
"INVALID\_ACCOUNT\_DETAILS",
"PAYMENT\_ATTEMPT\_COUNTS\_EXCEEDED",
"USER\_DEVICE\_UNREACHABLE",
"CHANNEL\_UNAVAILABLE",
"INSUFFICIENT\_BALANCE",
"ACCOUNT\_NOT\_ACTIVATED",
"INVALID\_TOKEN",
"SERVER\_ERROR",
"PARTNER\_TIMEOUT\_ERROR",
"TIMEOUT\_ERROR",
"USER\_DECLINED\_PAYMENT",
"USER\_DID\_NOT\_AUTHORIZE",
"PAYMENT\_REQUEST\_EXPIRED",
"FAILURE\_DETAILS\_UNAVAILABLE",
"EXPIRED\_OTP",
"INVALID\_OTP",
"PAYMENT\_AMOUNT\_LIMITS\_EXCEEDED",
"OTP\_ATTEMPT\_COUNTS\_EXCEEDED",
"CARD\_DECLINED",
"DECLINED\_BY\_ISSUER",
"ISSUER\_UNAVAILABLE",
"INVALID\_CVV",
"DECLINED\_BY\_PROCESSOR",
"CAPTURE\_AMOUNT\_EXCEEDED ",
"AUTHENTICATION\_FAILED",
"PROCESSOR\_ERROR",
"EXPIRED\_CARD",
"STOLEN\_CARD",
"INACTIVE\_OR\_UNAUTHORIZED\_CARD",
"INVALID\_MERCHANT\_CREDENTIALS",
"SUSPECTED\_FRAUDULENT"
]

ExampleCARD\_DECLINED

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

Payments\_API\_Http400InactivePaymentRequest

object (Payments\_API\_Http400InactivePaymentRequest)

error\_code

string

Valid values[
"INACTIVE\_PAYMENT\_REQUEST"
]

message

string

Payment request is already inactive.

Payments\_API\_Http400InvalidValueError

object (Payments\_API\_Http400InvalidValueError)

error\_code

string

Valid values[
"INVALID\_VALUE\_ERROR"
]

message

string

Values in the payment request is not within expected range or expected configurations. Check the specific error message for debugging.

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

Payments\_API\_Http400IneligibleTransactionStatus

object (Payments\_API\_Http400IneligibleTransactionStatus)

error\_code

string

Valid values[
"INELIGIBLE\_TRANSACTION\_STATUS"
]

message

string

Feature is not allowed for the payment request because of its current status. Check the specific error message for debugging.

Payments\_API\_Http400CaptureAmountExceeded

object (Payments\_API\_Http400CaptureAmountExceeded)

error\_code

string

Valid values[
"CAPTURE\_AMOUNT\_EXCEEDED"
]

message

string

Capture amount specified in capture request must be less than or equal to uncaptured authorization amount.

Payments\_API\_Http400TemporarilyUnavailable

object (Payments\_API\_Http400TemporarilyUnavailable)

error\_code

string

Valid values[
"TEMPORARILY\_UNAVAILABLE"
]

message

string

Requested feature is unavailable during this timing.

Forbidden

application/json

OneOf

Payments\_API\_Http403InvalidMerchantSettings

object (Payments\_API\_Http403InvalidMerchantSettings)

error\_code

string

Valid values[
"INVALID\_MERCHANT\_SETTINGS"
]

message

string

Merchant credentials met with an error with the provider. Please contact Xendit customer support to resolve this issue.

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

Service unavailable

application/json

OneOf

Payments\_API\_Http503ChannelUnavailable

object (Payments\_API\_Http503ChannelUnavailable)

error\_code

string

Valid values[
"CHANNEL\_UNAVAILABLE"
]

message

string

The channel requested is currently experiencing unexpected issues. The provider will be notified to resolve this issue.

Payments\_API\_Http503IssuerUnavailable

object (Payments\_API\_Http503IssuerUnavailable)

error\_code

string

Valid values[
"ISSUER\_UNAVAILABLE"
]

message

string

The end user's payment method provider is currently experiencing unexpected issues. The provider will be notified to resolve this issue.

Was this article helpful?

Yes  No

Previous article

Cancel a payment

Next article

Create a new payment token

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

payment\_id \*

api-version 

2024-11-11 

-  2024-11-11

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
 "capture_amount": 10000
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

200400403404500503

 

```
 "payment_request_id": "pr-1102feb0-bb79-47ae-9d1e-e69394d3949c",
```