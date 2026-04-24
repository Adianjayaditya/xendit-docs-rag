---
url: https://docs.xendit.co/apidocs/list-transactions
title: "List Transactions"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Balance & Transactions](/apidocs/introduction-1)
  - [Transaction](/apidocs/get-transaction)

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

get

 [Get Transaction by ID](/apidocs/get-transaction)

get

 [List Transactions](/apidocs/list-transactions)

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

# List Transactions

- Updated on Nov 26, 2025
- Published on Jul 24, 2025

 [Prev](/apidocs/get-transaction "Get Transaction by ID")  [Next](/apidocs/accounts-misc-introduction "Introduction") 

Get

/transactions

Request this endpoint to get all transactions or select specific filter and search parameters. You can filter by date, type, or status. And you can search by reference, product id, or account identifier. The returned result will be paginated and ordered by the created date.

Use API key permission `Transaction Read` to perform this request

Sample curl Request:

Code snippet

```
curl https://api.xendit.co/transactions?types=PAYMENT&statuses=SUCCESS&channel_categories=EWALLET&channel_categories=RETAIL_OUTLET&limit=2 -X GET \
-u xnd_development_O46JfOtygef9kMNsK+ZPGT+ZZ9b3ooF4w3Dn+R1k+2fT/7GlCAN3jg==:
```

Plain text

Copy

Security

HTTP

Type basic

API Key authentication using HTTPS Basic Auth.
Use your API key as the username. The password field can be left empty.
Note: In the API documentation "Try it" section, password is required, you may include any value.

Header parameters

for-user-id

string

The sub-account user-id that you want to make this transaction for.

This header is only used if you have access to xenPlatform. See xenPlatform for more information

Query parameters

types

string

The type of the transaction

Valid values[
"ADJUSTMENT\_ADD",
"ADJUSTMENT\_DEDUCT",
"BNPL\_PARTNER\_SETTLEMENT\_CREDIT",
"BNPL\_PARTNER\_SETTLEMENT\_DEBIT",
"CASHBACK\_FEE",
"CASHBACK\_VAT",
"CHARGEBACK",
"CONVERSION",
"DISBURSEMENT",
"FOREX\_DEDUCTION",
"FOREX\_DEPOSIT",
"IN\_PERSON\_PAYMENT",
"LOAN\_REPAYMENT",
"OTHER",
"PAYMENT",
"REFUND",
"REMITTANCE",
"REMITTANCE\_COLLECTION\_PAYMENT",
"REMITTANCE\_PAYOUT",
"RESERVES\_HOLD",
"RESERVES\_RELEASE",
"TOPUP",
"TRANSFER\_IN",
"TRANSFER\_OUT",
"WITHDRAWAL"
]

statuses

string

The status of the transaction

Valid values[
"PENDING",
"SUCCESS",
"FAILED",
"VOIDED",
"REVERSED"
]

channel\_categories

string

The channel of the transactions that will be filtered. If not specified, all transaction channel will be returned.

Valid values[
"BANK",
"CARDS",
"CARDLESS\_CREDIT",
"CASH",
"DIRECT\_DEBIT",
"EWALLET",
"PAYLATER",
"QR\_CODE",
"RETAIL\_OUTLET",
"VIRTUAL\_ACCOUNT",
"XENPLATFORM",
"OTHER"
]

reference\_id

string

Reference that will be searched. Search by reference is case sensitive and requires exact match. Contact support to enable partial match functionality for your account.

Min length1

Max length255

product\_id

string

Product\_id that will be searched. Product\_id search is an exact match and case sensitive.

account\_identifier

string | null

Account identifier that will be searched. Account identifier search is exact match case sensitive.

currency

string

Currency filter for transaction-related endpoints and reports. The following currencies are commonly supported:

- IDR, PHP, USD, VND, THB, MYR, SGD, EUR, GBP, HKD, AUD
  However, any applicable ISO 4217 currency code may be used depending on your account and transaction type. This parameter is optional; if omitted, all currencies will be included.

Valid values[
"IDR",
"PHP",
"USD",
"VND",
"THB",
"MYR",
"SGD",
"EUR",
"GBP",
"HKD",
"AUD"
]

amount

number

Transaction amount to search. This will be exact match.

Example9989.0

created[gte]

string

Start time of transaction by created date. If not specified, will list all dates.

created[lte]

string

End time of transaction by created date. If not specified, will list all dates.

updated[gte]

string

Start time of transaction by updated date. If not specified, will list all dates.

updated[lte]

string

End time of transaction by updated date. If not specified, will list all dates.

limit

number

A limit on the number of transactions to be returned for each request.

Default10.0

after\_id

string

Id of the immediately previous item. Use this with `links` on the response for pagination.

before\_id

string

ID of the immediately following item.

Responses

200

400

Show example

Successful operation

application/json

Code snippet

```
{
  "has_more": false,
  "data": [
    {
      "id": "txn_3365895e-3cc1-490a-b48c-2757ce8ab0e5",
      "product_id": "cmanl0vtp000101u9lqbvn7im",
      "type": "CONVERSION",
      "status": "SUCCESS",
      "channel_category": "OTHER",
      "channel_code": "DEFAULT",
      "reference_id": "cmanl0vtp000101u9lqbvn7im",
      "account_identifier": null,
      "currency": "SGD",
      "amount": 6.55,
      "net_amount": 6.55,
      "net_amount_currency": "SGD",
      "cashflow": "MONEY_IN",
      "settlement_status": "SETTLED",
      "estimated_settlement_time": "2025-05-14T06:51:08.999Z",
      "business_id": "675bdaf542c2f448122e71d5",
      "created": "2025-05-14T06:51:08.998Z",
      "updated": "2025-05-14T06:52:34.196Z",
      "fee": {
        "xendit_fee": 0,
        "value_added_tax": 0,
        "xendit_withholding_tax": 0,
        "third_party_withholding_tax": 0,
        "status": "NOT_APPLICABLE"
      }
    },
    {
      "id": "txn_c3d31125-1a06-4563-b7aa-b574beb7e2f9",
      "product_id": "cm99a3by9000x01qu51tf1t85",
      "type": "CONVERSION",
      "status": "FAILED",
      "channel_category": "OTHER",
      "channel_code": "DEFAULT",
      "reference_id": "cm99a3by9000x01qu51tf1t85",
      "account_identifier": null,
      "currency": "SGD",
      "amount": 6.8,
      "net_amount": 5.1,
      "net_amount_currency": "USD",
      "cashflow": "MONEY_IN",
      "settlement_status": "PENDING",
      "estimated_settlement_time": "2025-04-09T01:56:38.519Z",
      "business_id": "675bdaf542c2f448122e71d5",
      "created": "2025-04-09T01:56:38.517Z",
      "updated": "2025-04-09T01:58:05.027Z",
      "fee": {
        "xendit_fee": 0,
        "value_added_tax": 0,
        "xendit_withholding_tax": 0,
        "third_party_withholding_tax": 0,
        "status": "NOT_APPLICABLE"
      }
    },
    {
      "id": "txn_8c36b107-a52e-478a-8dde-59bfa7212bc6",
      "product_id": "d2845324-50d1-41bc-8583-0b888456ebfe",
      "type": "PAYMENT",
      "status": "SUCCESS",
      "channel_category": "EWALLET",
      "channel_code": "MY_SHOPEEPAY",
      "reference_id": "mylitt-aa7650f9b1364433-a7e7c4809b379e4e-1742983783200",
      "account_identifier": null,
      "currency": "MYR",
      "amount": 2.22,
      "net_amount": 2.2,
      "net_amount_currency": "MYR",
      "cashflow": "MONEY_IN",
      "settlement_status": "SETTLED",
      "estimated_settlement_time": "2025-03-28T10:09:54.915Z",
      "business_id": "668643d45f3fffd3c0d3b1ef",
      "created": "2025-03-26T10:09:55.171Z",
      "updated": "2025-03-28T10:10:53.276Z",
      "fee": {
        "xendit_fee": 0.02,
        "value_added_tax": 0,
        "xendit_withholding_tax": 0,
        "third_party_withholding_tax": 0,
        "status": "NOT_APPLICABLE"
      }
    },
    {
      "id": "txn_pay_1234567890abcdef",
      "product_id": "py-123e4567-e89b-12d3-a456-426614174000",
      "type": "PAYMENT",
      "status": "SUCCESS",
      "channel_category": "EWALLET",
      "channel_code": "ID_SHOPEEPAY",
      "reference_id": "payref-123456",
      "account_identifier": null,
      "currency": "IDR",
      "amount": 100000,
      "net_amount": 99000,
      "net_amount_currency": "IDR",
      "cashflow": "MONEY_IN",
      "settlement_status": "SETTLED",
      "estimated_settlement_time": "2025-06-01T10:00:00Z",
      "business_id": "1234567890abcdef",
      "created": "2025-06-01T09:59:00Z",
      "updated": "2025-06-01T10:01:00Z",
      "fee": {
        "xendit_fee": 1000,
        "value_added_tax": 0,
        "xendit_withholding_tax": 0,
        "third_party_withholding_tax": 0,
        "status": "COMPLETED"
      },
      "product_data": {
        "capture_id": "cap-123e4567-e89b-12d3-a456-426614174002",
        "payment_request_id": "pr-123e4567-e89b-12d3-a456-426614174003"
      }
    }
  ],
  "links": []
}
```

JSON

Copy

Collapse all

object

has\_more

boolean

Indicates whether there are more items to be queried with after\_id of the last item from the current result.
When true, use the HATEOAS links for pagination.

data

Array of object (TransactionObject)

object

id

string

Unique ID generated by Xendit for the particular file

product\_id

string

The product\_id of transaction. Product id will have different prefix for each different product. You can use this id to match the transaction from this API to each product API.

type

string

The type of the transactions. Here are the descriptions:

- `ADJUSTMENT_ADD`: An adjustment transaction that adds to the balance.
- `ADJUSTMENT_DEDUCT`: An adjustment transaction that deducts from the balance.
- `BNPL_PARTNER_SETTLEMENT_CREDIT`: Buy Now Pay Later partner settlement credit transaction.
- `BNPL_PARTNER_SETTLEMENT_DEBIT`: Buy Now Pay Later partner settlement debit transaction.
- `CASHBACK_FEE`: Cashback fee transaction.
- `CASHBACK_VAT`: Cashback VAT transaction.
- `CHARGEBACK`: A chargeback transaction for disputed charges.
- `CONVERSION`: Balance conversion transactions between different currencies.
- `DISBURSEMENT`: The disbursement of money-out transaction.
- `FOREX_DEDUCTION`: Foreign exchange deduction transaction.
- `FOREX_DEPOSIT`: Foreign exchange deposit transaction.
- `IN_PERSON_PAYMENT`: In-person payment transaction.
- `LOAN_REPAYMENT`: Loan repayment transaction.
- `OTHER`: Other transaction types not covered by specific categories.
- `PAYMENT`: The payment that includes all variation of money-in transaction.
- `REFUND`: A refund transaction created to refund amount from money-in transaction.
- `REMITTANCE`: A remittance transaction.
- `REMITTANCE_COLLECTION_PAYMENT`: Remittance collection payment transaction.
- `REMITTANCE_PAYOUT`: The remittance pay-out transaction.
- `RESERVES_HOLD`: Transaction for holding reserves.
- `RESERVES_RELEASE`: Transaction for releasing held reserves.
- `TOPUP`: A top-up transaction for adding money to account balance.
- `TRANSFER_IN`: Transfer into the account from another Xendit account.
- `TRANSFER_OUT`: Transfer out of the account to another Xendit account.
- `WITHDRAWAL`: A withdrawal transaction for money-out operations.

Valid values[
"ADJUSTMENT\_ADD",
"ADJUSTMENT\_DEDUCT",
"BNPL\_PARTNER\_SETTLEMENT\_CREDIT",
"BNPL\_PARTNER\_SETTLEMENT\_DEBIT",
"CASHBACK\_FEE",
"CASHBACK\_VAT",
"CHARGEBACK",
"CONVERSION",
"DISBURSEMENT",
"FOREX\_DEDUCTION",
"FOREX\_DEPOSIT",
"IN\_PERSON\_PAYMENT",
"LOAN\_REPAYMENT",
"OTHER",
"PAYMENT",
"REFUND",
"REMITTANCE",
"REMITTANCE\_COLLECTION\_PAYMENT",
"REMITTANCE\_PAYOUT",
"RESERVES\_HOLD",
"RESERVES\_RELEASE",
"TOPUP",
"TRANSFER\_IN",
"TRANSFER\_OUT",
"WITHDRAWAL"
]

channel\_code

string

The channel of the transaction that is used. See [channel codes](https://xendit-docs.document360.io/docs/available-payment-channels) for the list of available per channel categories.

reference\_id

string

A Reference ID from merchants to identify their request.

Min length1

Max length255

account\_identifier

string | null

Account identifier of transaction. The format will be different from each channel. For example, on `BANK` channel it will be account number and on `CARD` it will be masked card number.

currency

string

The currency to filter.

Valid values[
"IDR",
"PHP",
"USD",
"VND",
"THB",
"MYR",
"SGD",
"EUR",
"GBP",
"HKD",
"AUD"
]

Default"IDR"

amount

number

The amount of transaction. The number of decimal place will be different for each currency according to ISO 4217.

Example9989.0

net\_amount

number

The net amount of transaction after it deducted with fee/vat.

Example9989.0

net\_amount\_currency

string

The currency of the net amount after fees and taxes are applied.

Valid values[
"IDR",
"PHP",
"USD",
"VND",
"THB",
"MYR",
"SGD",
"EUR",
"GBP",
"HKD",
"AUD"
]

cashflow

string

Representing whether the transaction is money in or money out For transfer, the transfer out side it will shows up as money out and on transfer in side in will shows up as money-in.

Available values are `MONEY_IN` for money in and `MONEY_OUT` for money out.

status

string

The status of the transaction. Here's the description:

- `PENDING`: The transaction is still pending to be processed. This refers to money out-transaction when the amount is still on hold.
- `SUCCESS`: The transaction is successfully sent for money-out or already arrives on money-in.
- `FAILED`: The transaction failed to send/receive.
- `VOIDED`: The money-in transaction is voided by customer.
- `REVERSED`:The transaction is reversed by Xendit.

Valid values[
"PENDING",
"SUCCESS",
"FAILED",
"VOIDED",
"REVERSED"
]

channel\_category

string

The channel category of the transaction to identify the source of the transaction. Here's the description:

- `DISBURSEMENT` and `REMITTANCE_PAYOUT`: `BANK` and `CASH`
- `PAYMENT`: `CARDS`, `CARDLESS_CREDIT`, `DIRECT_DEBIT`, `EWALLET`, `PAYLATER`, `QR_CODE`, `RETAIL_OUTLET`, `VIRTUAL_ACCOUNT`
- `TRANSFER`: `XENPLATFORM`
- `CONVERSION`: `OTHER`

Valid values[
"BANK",
"CARDS",
"CARDLESS\_CREDIT",
"CASH",
"DIRECT\_DEBIT",
"EWALLET",
"PAYLATER",
"QR\_CODE",
"RETAIL\_OUTLET",
"VIRTUAL\_ACCOUNT",
"XENPLATFORM",
"OTHER"
]

business\_id

string

Unique ID generated by Xendit for the particular file

created

string

Transaction created timestamp on UTC+0

updated

string

Transaction updated timestamp on UTC+0

fee

object (FeeObject)

xendit\_fee

number

Amount of the Xendit fee for this transaction.

value\_added\_tax

number

Amount of the VAT for this transaction.

xendit\_withholding\_tax

number

Amount of the Xendit Withholding Tax for this transaction if applicable. See Tax Documentation for more information.

third\_party\_withholding\_tax

number

Amount of the 3rd Party Withholding Tax for this transaction if applicable.

status

string

Status of the fee processing. NOT\_APPLICABLE means no fees are applicable for this transaction.

Valid values[
"PENDING",
"COMPLETED",
"CANCELED",
"REVERSED",
"NOT\_APPLICABLE"
]

settlement\_status

string | null

Status of the settlement.

- `null`: Settlement status is not applicable or not yet determined
- `PENDING`: Transaction amount has not been settled to merchant's balance
- `EARLY_SETTLED`: Transaction has been settled early to merchant's balance
- `SETTLED`: Transaction has been settled to merchant's balance

Valid values[
"PENDING",
"EARLY\_SETTLED",
"SETTLED"
]

estimated\_settlement\_time

string

Estimated settlement time will only apply to money-in transactions.
For money-out transaction, value will be `NULL`
Estimated settlement time in which transaction amount will be settled to merchant's balance.

product\_data

object (ProductData) | null

Additional metadata for payment V3 transactions. This object contains product-specific identifiers and is only included when at least one field has a value. All fields are nullable and conditionally populated based on the transaction type and payment flow.

capture\_id

string | null

The capture ID for payment V3 transactions. Present for captured payments.

Examplecptr-123e4567-e89b-12d3-a456-426614174000

payment\_request\_id

string | null

The payment request ID for payment V3 transactions. Present for payments created via payment V3 payment requests.

Examplepr-123e4567-e89b-12d3-a456-426614174001

reusable\_payment\_link\_id

string | null

The reusable payment link ID. Present for payments made through reusable payment links.

Examplerpl-123e4567-e89b-12d3-a456-426614174002

payment\_link\_id

string | null

The invoice/payment link ID. Present for payments associated with payment links.

Exampleinv-123e4567-e89b-12d3-a456-426614174003

links

Array of object

HATEOAS links for pagination. Contains navigation links when more results are available.

object

href

string

URI for the next page of results.

rel

string

Link relationship type. Value will be 'next' for pagination.

method

string

HTTP method to use. Value will be 'GET'.

Inputs are failing validation. The errors field contains details about which fields are violating validation.

application/json

object

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR",
"FEATURE\_NOT\_AVAILABLE"
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

Get Transaction by ID

Next article

Introduction

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

types 

- 

-  ADJUSTMENT\_ADD  ADJUSTMENT\_DEDUCT  BNPL\_PARTNER\_SETTLEMENT\_CREDIT  BNPL\_PARTNER\_SETTLEMENT\_DEBIT  CASHBACK\_FEE  CASHBACK\_VAT  CHARGEBACK  CONVERSION  DISBURSEMENT  FOREX\_DEDUCTION  FOREX\_DEPOSIT  IN\_PERSON\_PAYMENT  LOAN\_REPAYMENT  OTHER  PAYMENT  REFUND  REMITTANCE  REMITTANCE\_COLLECTION\_PAYMENT  REMITTANCE\_PAYOUT  RESERVES\_HOLD  RESERVES\_RELEASE  TOPUP  TRANSFER\_IN  TRANSFER\_OUT  WITHDRAWAL

statuses 

- 

-  PENDING  SUCCESS  FAILED  VOIDED  REVERSED

channel\_categories 

- 

-  BANK  CARDS  CARDLESS\_CREDIT  CASH  DIRECT\_DEBIT  EWALLET  PAYLATER  QR\_CODE  RETAIL\_OUTLET  VIRTUAL\_ACCOUNT  XENPLATFORM  OTHER

reference\_id

product\_id

account\_identifier

currency 

- 

-  IDR  PHP  USD  VND  THB  MYR  SGD  EUR  GBP  HKD  AUD

amount

created[gte]

created[lte]

updated[gte]

updated[lte]

limit

after\_id

before\_id

for-user-id

 Try it & see response

Response

Available responses

application/json

application/json

200400

 

```
    "reusable_payment_link_id": "rpl-123e4567-e89b-12d3-a456-426614174002",
```