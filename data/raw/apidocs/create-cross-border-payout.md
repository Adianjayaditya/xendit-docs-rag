---
url: https://docs.xendit.co/apidocs/create-cross-border-payout
title: "Create a Cross-Border Payout"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payouts](/apidocs/payouts-introduction)
  - Cross-Border Payout

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

post

 [Create a Cross-Border Payout](/apidocs/create-cross-border-payout)

post

 [Cross-Border Payout Webhook](/apidocs/cross-border-payout-webhook-notification)

get

 [Get cross-border payout by Id](/apidocs/get-cross-border-payout)

get

 [Cancel cross-border payout](/apidocs/cancel-cross-border-payout)

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

# Create a Cross-Border Payout

- Updated on Jul 31, 2025
- Published on Feb 11, 2025

 [Prev](/apidocs/get-payout-channels "Get Payment Channels")  [Next](/apidocs/cross-border-payout-webhook-notification "Cross-Border Payout Webhook") 

Post

/remittance\_payouts

Our Create Cross-Border Payout API allows you to send third party payouts from your Xendit Account on behalf of a sender to your designated recipient.

Security

HTTP

Type basic

Header parameters

Idempotency-key

stringRequired

A unique key to prevent processing duplicate requests. Can be your reference\_id or any GUID.

Min length1

Max length100

Body parameters

Show example

application/json

createPayoutExample

createPayoutExample

Code snippet

```
{
  "reference_id": "myref-1482928194",
  "destination_currency": "IDR",
  "destination_amount": 1000000,
  "sender_customer_id": "cust-1752fefb-358c-4043-a690-58036157d851",
  "recipient_customer_id": "cust-b8476133-ec15-4f06-9dfb-562d8dca3f43",
  "origin_currency": "EUR",
  "origin_amount": 60,
  "source_of_fund": "OTHER",
  "purpose_code": "OTHER",
  "relationship": "CUSTOMER",
  "description": "This is a sample Cross-border Payout transaction"
}
```

JSON

Copy

Collapse all

object

reference\_id

string Required

A reference to uniquely identify the Payout.

Min length1

Max length255

Examplemyref-1482928194

destination\_currency

string Required

ISO 4217 Currency Code.

destination\_amount

number Required

Amount to be sent to the destination account.

- For `IDR` currency, number should be integer
- For `PHP` currency, number can be up to 2 decimal places
- For `VND` currency, number should be integer
- For `MYR` currency, number can be up to 2 decimal places
- For `THB` currency, number can be up to 2 decimal places

Minimum0.0

Example10000.0

sender\_customer\_id

string Required

The Id of the sender customer (as returned by the Create Customer endpoint)

The following fields are required in the sender customer object: `customer_type` and `addresses`

- For INDIVIDUAL `customer_type`, the following parameters are also required: `given_names`, `nationality`, and `date_of_birth` in `customer_type`.`individual_detail` object
- For BUSINESS `customer_type`, then the following parameters are also required: `business_name` in `customer_type`.`business_detail` object.
- For `addresses` object, the following fields are also required: `addresses`.`country`, `addresses`.`city`, `addresses`.`street_line1`

Reference: [Customer Object](https://developers.xendit.co/api-reference/#create-customer)

recipient\_customer\_id

string Required

The Id of the recipient customer (as returned by the Create Customer endpoint)

The following fields are required in the sender customer object: `customer_type`, `addresses`, `identity_accounts`, and one of `phone_number` or `mobile_number`

- For INDIVIDUAL `customer_type`, the following parameters are also required: `given_names`, `nationality`, and `date_of_birth` in `customer_type`.`individual_detail` object
- For BUSINESS `customer_type`, then the following parameters are also required: `business_name` in `customer_type`.`business_detail` object.
- For `addresses` object, the following fields are also required: `addresses`.`country`, `addresses`.`city`, `addresses`.`street_line1`
- For `identity_accounts` object, the following fields are also required: `type`, `country`, `company` (with the channel code value), and `properties`

Reference: [Customer Object](https://developers.xendit.co/api-reference/#create-customer)

origin\_currency

string Required

ISO 4217 Currency Code.

origin\_amount

number Required

The original amount as sent by the sender.
This field will not be used for processing the payout, but is required for monitoring purposes.

Xendit will deduct your balance and process the payout in the destination amount and currency.

source\_of\_fund

string

Source of fund

- `INVESTMENT` - Bonds, fixed deposits, preference shares, business ownership/equity or property ownership
- `PERSONAL_SAVINGS` - Funds kept in an account in a bank or a similar organization
- `BUSINESS_REVENUE` - Income from a business or a company
- `LEGACY` - Inherited money from a will
- `BUSINESS_ARRANGEMENT` - Any understanding, procedure, course of dealing, or arrangement between a creditor and a seller
- `LOAN` - A sum of money that is borrowed
- `SALARY` - A fixed regular payment made by an employer
- `OTHER` - Other

Default: OTHER

Valid values[
"INVESTMENT",
"PERSONAL\_SAVINGS",
"BUSINESS\_REVENUE",
"LEGACY",
"BUSINESS\_ARRANGEMENT",
"LOAN",
"SALARY",
"OTHER"
]

purpose\_code

string

Purpose of the Cross-border Payout

- `SELF` - Transfer to own account
- `FAMILY` - Family Maintenance
- `EDUCATION` - Education-related student expenses
- `MEDICAL` - Medical Treatment
- `HOTEL` - Hotel Accomodation
- `TRAVEL` - Travel
- `UTILITIES` - Utility Bills
- `LOAN_REPAYMENT` - Repayment of Loans
- `TAX_PAYMENT` - Tax Payment
- `RESIDENCE_PURCHASE` - Purchase of Residential Property
- `RESIDENCE_RENT` - Payment of Property Rental
- `INSURANCE` - Insurance
- `MUTUAL_FUND` - Mutual Fund Investment
- `SHARES_INVESTMENT` - Investment in Shares
- `DONATIONS` - Donations
- `ADVERTISING` - Advertising & Public relations-related expenses
- `ROYALTY_FEES` - Royalty fees, trademark fees, patent fees, and copyright fees
- `BROKER_FEES` - Fees for brokers, front end fee, commitment fee, guarantee fee and custodian fee
- `ADVISORS` - Fees for advisors, technical assistance, and academic purpose, including remuneration for specialists
- `OFFICE` - Representative office expenses
- `CONSTRUCTION` - Construction costs / expenses
- `SHIPMENT` - Transportation fees for goods
- `EXPORT` - For payment of exported goods
- `DELIVERY` - Delivery fees for goods
- `TRADES` - General Goods Trades - Offline trade
- `SALARY` - Salary
- `REFUND` - Refund
- `OTHER` - Other

Default: OTHER

Valid values[
"SELF",
"FAMILY",
"EDUCATION",
"MEDICAL",
"HOTEL",
"TRAVEL",
"UTILITIES",
"LOAN\_REPAYMENT",
"TAX\_PAYMENT",
"RESIDENCE\_PURCHASE",
"RESIDENCE\_RENT",
"INSURANCE",
"MUTUAL\_FUND",
"SHARES\_INVESTMENT",
"DONATIONS",
"ADVERTISING",
"ROYALTY\_FEES",
"BROKER\_FEES",
"ADVISORS",
"OFFICE",
"CONSTRUCTION",
"SHIPMENT",
"EXPORT",
"DELIVERY",
"TRADES",
"SALARY",
"REFUND",
"OTHER"
]

relationship

string

Relationship between sender and recipient

Required for PH\_GCASH
Default: OTHER

Valid values[
"BRANCH\_REPRESENTATIVE\_OFFICE",
"BUSINESS\_PARTNER",
"CHILDREN",
"CREDITOR",
"CUSTOMER",
"DEBTOR",
"EMPLOYEE",
"EX\_SPOUSE",
"FRANCHISEE\_FRANCHISOR",
"GRANDPARENTS",
"HOLDING\_COMPANY",
"MAID",
"OWNSELF",
"PARENTS",
"RELATIVE",
"SIBLING",
"SPOUSE",
"SUBSIDIARY\_COMPANY",
"SUPPLIER",
"FRIEND",
"GOVERNMENT\_BODY",
"EDUCATION\_INSTITUTION",
"NON\_GOVERNMENT\_BODY",
"OTHER"
]

description

string Required

Description to send with the payout.
The recipient may see this e.g. in their bank statement (if supported) or in email receipts we send on your behalf.

Min length1

Max length100

metadata

object (Metadata) | null

Key-value entries for your custom data.
You can specify up to 50 keys, with key names up to 40 characters and values up to 500 characters.
This is for your convenience. Xendit will not use this data for any processing.

Example{
"my\_custom\_id": "merchant-123",
"my\_custom\_order\_id": "order-123"
}

Responses

200

400

403

404

409

500

Show example

Cross-Border Payout created

application/json

createCrossBorderPayoutResponseExample

createCrossBorderPayoutResponseExample

Code snippet

```
{
  "id": "rpo_288250b4-124b-4be5-93a1-1cd50dd4ad02",
  "business_id": "665990ef233a8b8054549367",
  "description": "This is a sample Cross-border Payout transaction",
  "destination_amount": 1000000,
  "destination_currency": "IDR",
  "metadata": {},
  "origin_amount": 60,
  "origin_currency": "EUR",
  "purpose_code": "OTHER",
  "recipient_customer_id": "cust-b8476133-ec15-4f06-9dfb-562d8dca3f43",
  "reference_id": "myref-1482928194",
  "relationship": "CUSTOMER",
  "sender_customer_id": "cust-1752fefb-358c-4043-a690-58036157d851",
  "source_of_fund": "OTHER",
  "status": "ACCEPTED",
  "created": "2024-12-13T07:51:10.832Z",
  "updated": "2024-12-13T07:51:10.832Z"
}
```

JSON

Copy

Collapse all

object

id

string

Xendit-generated unique payout link id in UUID format

Prefix: rpo\_

Min length40

Max length40

Examplerpo\_cde3dcb8-37d7-4ea1-a275-8f54af81feb0

created

string

Timestamp when the payout request was made (in ISO 8601 format)

Timezone UTC+0

updated

string

Timestamp when the payout request was updated (in ISO 8601 format)

Timezone UTC+0

business\_id

string

Your Xendit Business ID

Example5785e6334d7b410667d355c4

reference\_id

string

A reference to uniquely identify the Payout.

Min length1

Max length255

Examplemyref-1482928194

destination\_currency

string

ISO 4217 Currency Code.

destination\_amount

number

Amount to be sent to the destination account.

- For `IDR` currency, number should be integer
- For `PHP` currency, number can be up to 2 decimal places
- For `VND` currency, number should be integer
- For `MYR` currency, number can be up to 2 decimal places
- For `THB` currency, number can be up to 2 decimal places

Minimum0.0

Example10000.0

sender\_customer\_id

string

The Id of the sender customer (as returned by the Create Customer endpoint)

The following fields are required in the sender customer object: `customer_type` and `addresses`

- For INDIVIDUAL `customer_type`, the following parameters are also required: `given_names`, `nationality`, and `date_of_birth` in `customer_type`.`individual_detail` object
- For BUSINESS `customer_type`, then the following parameters are also required: `business_name` in `customer_type`.`business_detail` object.
- For `addresses` object, the following fields are also required: `addresses`.`country`, `addresses`.`city`, `addresses`.`street_line1`

Reference: [Customer Object](https://developers.xendit.co/api-reference/#create-customer)

recipient\_customer\_id

string

The Id of the recipient customer (as returned by the Create Customer endpoint)

The following fields are required in the sender customer object: `customer_type`, `addresses`, `identity_accounts`, and one of `phone_number` or `mobile_number`

- For INDIVIDUAL `customer_type`, the following parameters are also required: `given_names`, `nationality`, and `date_of_birth` in `customer_type`.`individual_detail` object
- For BUSINESS `customer_type`, then the following parameters are also required: `business_name` in `customer_type`.`business_detail` object.
- For `addresses` object, the following fields are also required: `addresses`.`country`, `addresses`.`city`, `addresses`.`street_line1`
- For `identity_accounts` object, the following fields are also required: `type`, `country`, `company` (with the channel code value), and `properties`

Reference: [Customer Object](https://developers.xendit.co/api-reference/#create-customer)

status

string

Status of the cross-border payout. Default is ACCEPTED.

- `ACCEPTED` - The payout request has been accepted and has not yet been sent on to a channel. A payout may remain in this status if the chosen channel is currently offline. Xendit will process this automatically when the channel comes back online
- `PENDING_COMPLIANCE_ASSESSMENT` - Request is considered medium or high risk, and is being reviewed by our compliance team. Our team will contact you via email for extra information for enhanced due diligence.
- `COMPLIANCE_REJECTED` - Request is rejected for compliance reasons.
- `REQUESTED` - The payout has been sent to the channel. Funds have been sent to the channel for processing.
- `READY` - For cash payout only. Cash is ready for pick-up.
- `LOCKED` - For cash payout only. Cash pick-up in progress.
- `EXPIRED` - For cash payout only. Cash payout has expired.
- `FAILED` - Payout failed. See possible reasons in Failed Reasons section.
- `SUCCEEDED` - Sender bank/channel has sent out the payout
- `CANCELLED` - Payout has been cancelled per your request
- `REFUNDED` - Only valid for SKN/RTGS and cash channel use case.

Valid values[
"ACCEPTED",
"PENDING\_COMPLIANCE\_ASSESSMENT",
"COMPLIANCE\_REJECTED",
"REQUESTED",
"READY",
"LOCKED",
"EXPIRED",
"FAILED",
"SUCCEEDED",
"CANCELLED",
"REFUNDED"
]

description

string

Description to send with the payout.
The recipient may see this e.g. in their bank statement (if supported) or in email receipts we send on your behalf.

Min length1

Max length100

source\_of\_fund

string

Source of fund

- `INVESTMENT` - Bonds, fixed deposits, preference shares, business ownership/equity or property ownership
- `PERSONAL_SAVINGS` - Funds kept in an account in a bank or a similar organization
- `BUSINESS_REVENUE` - Income from a business or a company
- `LEGACY` - Inherited money from a will
- `BUSINESS_ARRANGEMENT` - Any understanding, procedure, course of dealing, or arrangement between a creditor and a seller
- `LOAN` - A sum of money that is borrowed
- `SALARY` - A fixed regular payment made by an employer
- `OTHER` - Other

Default: OTHER

Valid values[
"INVESTMENT",
"PERSONAL\_SAVINGS",
"BUSINESS\_REVENUE",
"LEGACY",
"BUSINESS\_ARRANGEMENT",
"LOAN",
"SALARY",
"OTHER"
]

origin\_currency

string

ISO 4217 Currency Code.

origin\_amount

number

The original amount as sent by the sender.
This field will not be used for processing the payout, but is required for monitoring purposes.

Xendit will deduct your balance and process the payout in the destination amount and currency.

purpose\_code

string

Purpose of the Cross-border Payout

- `SELF` - Transfer to own account
- `FAMILY` - Family Maintenance
- `EDUCATION` - Education-related student expenses
- `MEDICAL` - Medical Treatment
- `HOTEL` - Hotel Accomodation
- `TRAVEL` - Travel
- `UTILITIES` - Utility Bills
- `LOAN_REPAYMENT` - Repayment of Loans
- `TAX_PAYMENT` - Tax Payment
- `RESIDENCE_PURCHASE` - Purchase of Residential Property
- `RESIDENCE_RENT` - Payment of Property Rental
- `INSURANCE` - Insurance
- `MUTUAL_FUND` - Mutual Fund Investment
- `SHARES_INVESTMENT` - Investment in Shares
- `DONATIONS` - Donations
- `ADVERTISING` - Advertising & Public relations-related expenses
- `ROYALTY_FEES` - Royalty fees, trademark fees, patent fees, and copyright fees
- `BROKER_FEES` - Fees for brokers, front end fee, commitment fee, guarantee fee and custodian fee
- `ADVISORS` - Fees for advisors, technical assistance, and academic purpose, including remuneration for specialists
- `OFFICE` - Representative office expenses
- `CONSTRUCTION` - Construction costs / expenses
- `SHIPMENT` - Transportation fees for goods
- `EXPORT` - For payment of exported goods
- `DELIVERY` - Delivery fees for goods
- `TRADES` - General Goods Trades - Offline trade
- `SALARY` - Salary
- `REFUND` - Refund
- `OTHER` - Other

Default: OTHER

Valid values[
"SELF",
"FAMILY",
"EDUCATION",
"MEDICAL",
"HOTEL",
"TRAVEL",
"UTILITIES",
"LOAN\_REPAYMENT",
"TAX\_PAYMENT",
"RESIDENCE\_PURCHASE",
"RESIDENCE\_RENT",
"INSURANCE",
"MUTUAL\_FUND",
"SHARES\_INVESTMENT",
"DONATIONS",
"ADVERTISING",
"ROYALTY\_FEES",
"BROKER\_FEES",
"ADVISORS",
"OFFICE",
"CONSTRUCTION",
"SHIPMENT",
"EXPORT",
"DELIVERY",
"TRADES",
"SALARY",
"REFUND",
"OTHER"
]

relationship

string

Relationship between sender and recipient

Required for PH\_GCASH
Default: OTHER

Valid values[
"BRANCH\_REPRESENTATIVE\_OFFICE",
"BUSINESS\_PARTNER",
"CHILDREN",
"CREDITOR",
"CUSTOMER",
"DEBTOR",
"EMPLOYEE",
"EX\_SPOUSE",
"FRANCHISEE\_FRANCHISOR",
"GRANDPARENTS",
"HOLDING\_COMPANY",
"MAID",
"OWNSELF",
"PARENTS",
"RELATIVE",
"SIBLING",
"SPOUSE",
"SUBSIDIARY\_COMPANY",
"SUPPLIER",
"FRIEND",
"GOVERNMENT\_BODY",
"EDUCATION\_INSTITUTION",
"NON\_GOVERNMENT\_BODY",
"OTHER"
]

failure\_code

string

If the Payout failed, we include a failure code for more details on the failure.

- `INSUFFICIENT_BALANCE` - Client has insufficient balance for the payout amount
- `INVALID_DESTINATION` - The recipient account does not exist/is invalid.
- `REJECTED_BY_CHANNEL` - Payout failed due to an error from the destination channel. This is usually because of network issues associated with the destination bank or issues crediting funds into the destination bank account.
- `TEMPORARY_TRANSFER_ERROR` - The channel networks are experiencing a temporary error.
- `TRANSFER_ERROR` - We’ve encountered a fatal error while processing this payout. Normally, this means that certain API fields in your request are invalid.
- `UNKNOWN_BANK_NETWORK_ERROR` - The bank has delivered an error they have not documented. By definition, this means the bank does not know the issue.
- `DESTINATION_MAXIMUM_LIMIT` - The recipient is unable to receive the funds due to the payout amount exceeding the recipient’s ability to receive.

Valid values[
"INSUFFICIENT\_BALANCE",
"INVALID\_DESTINATION",
"REJECTED\_BY\_CHANNEL",
"TEMPORARY\_TRANSFER\_ERROR",
"TRANSFER\_ERROR",
"UNKNOWN\_BANK\_NETWORK\_ERROR",
"DESTINATION\_MAXIMUM\_LIMIT"
]

metadata

object (Metadata) | null

Key-value entries for your custom data.
You can specify up to 50 keys, with key names up to 40 characters and values up to 500 characters.
This is for your convenience. Xendit will not use this data for any processing.

Example{
"my\_custom\_id": "merchant-123",
"my\_custom\_order\_id": "order-123"
}

Bad Request

application/json

OneOf

400APIValidationError

object (400APIValidationError)

error\_code

string

ExampleAPI\_VALIDATION\_ERROR

error\_message

string

ExampleInputs are failing validation. The errors field contains details about which fields are violating validation

400InvalidJSONFormatError

object (400InvalidJSONFormatError)

error\_code

string

ExampleINVALID\_JSON\_FORMAT

error\_message

string

ExampleThe request body is not a valid JSON format

400DestinationCurrencyNotSupportedError

object (400DestinationCurrencyNotSupportedError)

error\_code

string

ExampleDESTINATION\_CURRENCY\_NOT\_SUPPORTED

error\_message

string

ExampleDestination currency is not supported. Check that the currency is supported for your chosen channel before retrying

400AmountFormatError

object (400AmountFormatError)

error\_code

string

ExampleAMOUNT\_FORMAT\_ERROR

error\_message

string

ExampleIncorrect number of decimal places for given amount

400MinimumTransferLimitError

object (400MinimumTransferLimitError)

error\_code

string

ExampleMINIMUM\_TRANSFER\_LIMIT\_ERROR

error\_message

string

Example"amount” is under the minimum amount supported for the channel. See amount limitations at the URL below

400MaximumTransferLimitError

object (400MaximumTransferLimitError)

error\_code

string

ExampleMAXIMUM\_TRANSFER\_LIMIT\_ERROR

error\_message

string

Example“amount” is more than the maximum amount supported for the channel. See amount limitations at the URL below

400AmountIncrementError

object (400AmountIncrementError)

error\_code

string

ExampleAMOUNT\_INCREMENT\_NOT\_SUPPORTED

error\_message

string

Example“amount” needs to be a multiple of the minimum increment supported by the channel

400AccountBlacklistedError

object (400AccountBlacklistedError)

error\_code

string

ExampleACCOUNT\_BLACKLISTED\_ERROR

error\_message

string

ExampleThe provided recipient bank account is blacklisted

400PaymentChannelDetailError

object (400PaymentChannelDetailError)

error\_code

string

ExamplePAYMENT\_CHANNEL\_DETAIL\_ERROR

error\_message

string

ExampleThe provided recipient account type is invalid. Please use the valid values (BANK\_ACCOUNT or EWALLET)

400DuplicateError

object (400DuplicateError)

error\_code

string

ExampleDUPLICATE\_ERROR

error\_message

string

ExampleA payout with this idempotency key already exists. If you meant to execute a different request, please use another idempotency key

Forbidden

application/json

OneOf

403RequestForbiddenError

object (403RequestForbiddenError)

error\_code

string

ExampleREQUEST\_FORBIDDEN\_ERROR

error\_message

string

ExampleThe API key is forbidden to perform this request

Not Found

application/json

OneOf

404CustomerDataNotFoundError

object (404CustomerDataNotFoundError)

error\_code

string

ExampleCUSTOMER\_DATA\_NOT\_FOUND

error\_message

string

ExampleCould not find any customer object with given sender\_customer\_id or recipient\_customer\_id. Try again using a valid Customer Id

Conflict

application/json

OneOf

409IdempotencyError

object (409IdempotencyError)

error\_code

string

ExampleIDEMPOTENCY\_ERROR

error\_message

string

ExampleKeys for idempotent requests can only be used for the same endpoint they were first used for. Try using a key if you meant to execute a different request

409StillProcessingError

object (409StillProcessingError)

error\_code

string

ExampleSTILL\_PROCESSING\_ERROR

error\_message

string

ExampleSimilar request with similar idempotency key is still processing

Internal Server Error

application/json

OneOf

500ServerError

object (500ServerError)

error\_code

string

ExampleSERVER\_ERROR

error\_message

string

ExampleError connecting to our server. Retry safely using Idempotency-key header when available

Was this article helpful?

Yes  No

Previous article

Get Payment Channels

Next article

Cross-Border Payout Webhook

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

Idempotency-key \*

Body

application/json

application/json

createPayoutExample

createPayoutExample

 Reset to default

 

13

1

```
{
```

2

```
  "reference_id": "myref-1482928194",
```

3

```
  "destination_currency": "IDR",
```

4

```
  "destination_amount": 1000000,
```

5

```
  "sender_customer_id": "cust-1752fefb-358c-4043-a690-58036157d851",
```

6

```
  "recipient_customer_id": "cust-b8476133-ec15-4f06-9dfb-562d8dca3f43",
```

7

```
  "origin_currency": "EUR",
```

8

```
  "origin_amount": 60,
```

9

```
  "source_of_fund": "OTHER",
```

10

```
  "purpose_code": "OTHER",
```

11

```
  "relationship": "CUSTOMER",
```

12

```
  "description": "This is a sample Cross-border Payout transaction"
```

13

```
}
```

 Try it & see response

Response

Available responses

application/json

application/json

200400403404409500

 

```
 "id": "rpo_cde3dcb8-37d7-4ea1-a275-8f54af81feb0",
```