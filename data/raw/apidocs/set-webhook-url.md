---
url: https://docs.xendit.co/apidocs/set-webhook-url
title: "Set webhook URL"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [xenPlatform](/apidocs/accounts-misc-introduction)
  - Webhook Settings

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

Webhook Settings

post

 [Set webhook URL](/apidocs/set-webhook-url)

Others

Download API reference

[Introduction](/apidocs/others-introduction)

Customers

Bill Payments

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Set webhook URL

- Updated on Jan 8, 2026
- Published on Dec 6, 2024

 [Prev](/apidocs/split-payment-status-notification-webhook "Split payment status notification webhook")  [Next](/apidocs/others-introduction "Introduction") 

Post

/callback\_urls/{type}

> ℹ️ Info
>
> This API can only be used to set Webhook URLs for our [Legacy Payment and Payout APIs](https://archive.developers.xendit.co/api-reference/#payments-api).
> For the latest APIs, as a Master Account, you can set up your sub-accounts to send webhooks for their activities to your configured URLs. Otherwise you may
> set the webhook URLs from each sub-account's Settings page in their Dashboards.

The following can be used in the `type` path parameter:

Money-In

- `invoice`: Xendit notifies your system when Invoice has been paid or expired.
- `fva_status`: Xendit notifies your system when Virtual Account has been created or updated successfully. Support: Indonesia only 🇲🇨
- `fva_paid`: Xendit notifies your system when Virtual Account has been paid successfully. Support: Indonesia only 🇲🇨
- `ro_fpc_paid`: Xendit notifies your system when Retail Outlet payment code (Alfamart/Indomaret) in Indonesia has been paid successfully. Support: Indonesia only 🇲🇨
- `regional_ro_paid`: Xendit notifies your system when Over-the-Counter payment code (7 Eleven, Cebuana, ECPay) in Philippines has been paid successfully. Support: Philippines only 🇵🇭
- `ewallet`: New eWallet type to receive charge and other eWallet events across eWallets channels from /ewallets/charges API.
- `payment_method`: Xendit notifies your system when payment method is expiring and/or has expired. Payment Method is a mandatory step to abstract Debit Card/Bank Account for Direct Debit transactions.
- `payment_method_v2`: Xendit notifies your system when payment method V2 is expiring and/or has activated or expired. Learn more about Payment Method V2 here.
- `direct_debit`: A Direct Debit payment event will be sent to your system for any successful transactions. Use direct\_debit type to receive Direct Debit payment event via webhook.
- `qr_code`: Xendit notifies your system when QR payment has been made or QR refund has been completed. This field is only supported for qr\_codes API version 2022-07-31.
- `recurring`: Xendit notifies your system when Subscription plan has been activated/inactivated, cycle created/succeeded/retrying/failed, or force attempt failed.
- `payment_succeeded`: Xendit notifies your system when a payment has been successfully confirmed or received from the partner channel (Only for payments initiated via new Payments API). Support: All businesses
- `payment_awaiting_capture`: Xendit notifies your system when a payment request with capture\_method set to MANUAL has been intialized and a call to the Payment Capture API needed to complete the payment. Support: All businesses
- `payment_pending`: Xendit notifies your system when a payment is being processed by the partner channel awaiting for the terminal status of it (Only for payments initiated via new Payments API). Support: All businesses
- `payment_failed`: Xendit notifies your system when a pending payment has failed (Only for payments initiated via new Payments API). Support: All businesses
- `capture_succeeded`: Xendit notifies your system when a manual capture via the Payment Capture API has succeeded. Support: All businesses
- `capture_failed`: Xendit notifies your system when a manual capture via the Payment Capture API has Failed. Support: All businesses
- `payment_request_completed`: Xendit notifies your system when a Direct Debit or E-Wallet payment request has succeeded or failed. Please Note that this is for the Payment Request API only. Make sure that other payment callbacks for Direct Debit or E-wallet are not set to prevent duplication. Support: Thailand 🇹🇭 and Malaysia 🇲🇾 only

Money-Out

- `disbursement`: Xendit notifies your system when disbursement has been executed successfully by Xendit, either with COMPLETED or FAILED status. Support: Indonesia only 🇲🇨
- `ph_disbursement`: Xendit notifies your system when disbursement has been executed successfully by Xendit, either with COMPLETED or FAILED status. Support: Philippines only 🇵🇭
- `batch_disbursement`: Xendit notifies your system when Batch Disbursement has been executed successfully by Xendit. Support: Indonesia only 🇲🇨
- `payout`: Xendit notifies your system upon failed and successful payouts. Learn more about Payouts V2 webhooks here.
  Others
- `report`: Xendit notifies your system to send the report to the specified URLs. Support: All businesses

Security

HTTP

Type basic

Header parameters

for-user-id

string

Example5cafeb170a2b18519b1b8761

Path parameters

type

stringRequired

The type of Webhook URL you want to set

Valid values[
"invoice",
"fva\_status",
"fva\_paid",
"ro\_fpc\_paid",
"regional\_ro\_paid",
"ewallet",
"payment\_method",
"payment\_method\_v2",
"direct\_debit",
"qr\_code",
"recurring",
"disbursement",
"ph\_disbursement",
"batch\_disbursement",
"report",
"payment\_succeeded",
"payment\_awaiting\_capture",
"payment\_pending",
"payment\_failed",
"capture\_succeeded",
"capture\_failed",
"payment\_request\_completed"
]

Body parameters

Show example

application/json

Code snippet

```
{
  "url": "https://www.xendit.co/webhook_catcher"
}
```

JSON

Copy

object

url

string Required

The URL of your server that you want to receive our Webhooks

Min length1

Responses

200

400

404

Show example

application/json

Code snippet

```
{
  "status": "SUCCESSFUL",
  "user_id": "5e6b30d967627b957de8c123",
  "url": "https://www.xendit.co/webhook_catcher",
  "environment": "TEST",
  "callback_token": "66a6680348e1c33ed2b9053a8eb9291b9e2230ff4f4d3057c9f4ac26405d2123"
}
```

JSON

Copy

object

status

string

The status of setting the Webhook URL

Valid values[
"SUCCESSFUL"
]

user\_id

string

The user\_id on which the Webhook URL has been set

url

string

The Webhook URL that has been set

environment

string

The environment on which the Webhook URL has been set

Valid values[
"TEST",
"LIVE"
]

callback\_token

string

The unique Webhook token that is attached to each sub-account. Use this to validate that a Webhook is sent from Xendit's servers.

Show example

Validation error

application/json

INVALID\_URL\_FORMAT

INVALID\_URL\_FORMAT

Code snippet

```
{
  "error_code": "INVALID_URL_FORMAT",
  "message": "You have provided an invalid URL format",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

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

Show example

Validation error

application/json

CALLBACK\_AUTHENTICATION\_TOKEN\_NOT\_FOUND\_ERROR

CALLBACK\_AUTHENTICATION\_TOKEN\_NOT\_FOUND\_ERROR

Code snippet

```
{
  "error_code": "CALLBACK_AUTHENTICATION_TOKEN_NOT_FOUND_ERROR",
  "message": "No webhook verification token found for this business, please contact help@xendit.co to resolve this issue",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

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

Split payment status notification webhook

Next article

Introduction

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

type \*

- 

-  invoice  fva\_status  fva\_paid  ro\_fpc\_paid  regional\_ro\_paid  ewallet  payment\_method  payment\_method\_v2  direct\_debit  qr\_code  recurring  disbursement  ph\_disbursement  batch\_disbursement  report  payment\_succeeded  payment\_awaiting\_capture  payment\_pending  payment\_failed  capture\_succeeded  capture\_failed  payment\_request\_completed

for-user-id

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
  "url": "https://www.xendit.co/webhook_catcher"
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

200400404

 

```
 "callback_token": "string"
```