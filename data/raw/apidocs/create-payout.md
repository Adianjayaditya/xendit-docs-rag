---
url: https://docs.xendit.co/apidocs/create-payout
title: "Create a Payout"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payouts](/apidocs/payouts-introduction)
  - Payout

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

post

 [Create a Payout](/apidocs/create-payout)

post

 [Payout Webhook](/apidocs/payout-webhook-notification)

get

 [Get payout by ID](/apidocs/get-payout)

get

 [Get all payouts by reference id](/apidocs/get-all-payouts)

get

 [Cancel payout](/apidocs/cancel-payout)

get

 [Get Payment Channels](/apidocs/get-payout-channels)

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

# Create a Payout

- Updated on Jul 31, 2025
- Published on Nov 29, 2024

 [Prev](/apidocs/payouts-introduction "Introduction")  [Next](/apidocs/payout-webhook-notification "Payout Webhook") 

Post

/v2/payouts

Initiate a Payout

Security

HTTP

Type basic

Header parameters

Idempotency-key

stringRequired

A unique key to prevent processing duplicate requests. Can be your reference\_id or any GUID.

Min length1

Max length100

for-user-id

string

The XenPlatform subaccount user id that you want to make this transaction for.
This header is only used if you have access to xenPlatform. See [xenPlatform](https://developers.xendit.co/api-reference/#xenplatform) for more information.

Body parameters

Show example

application/json

createPayoutExample

createPayoutExample

Code snippet

```
{
  "reference_id": "myref-1482928194",
  "channel_code": "ID_BCA",
  "channel_properties": {
    "account_number": "000000000099",
    "account_holder_name": "Michael Chen"
  },
  "amount": 10000,
  "description": "July payout",
  "currency": "IDR"
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

channel\_code

string Required

Channel code of destination bank, E-Wallet or OTC channel.
List of supported channels can be found [here](https://docs.xendit.co/xendisburse/channel-codes)

ExampleID\_BCA

channel\_properties

object (ChannelProperties) Required

account\_holder\_name

string Required

Name of account holder as per the bank or E-Wallet's records. Needs to match the registered account name exactly.

Min length1

Max length100

account\_number

string Required

Account number of destination. Mobile numbers for E-Wallet accounts.
For E-Wallets, standard format should use prefix 0, e.g. 081234567890

Min length1

Max length100

account\_type

string

Account type of the destination for currencies and channels that supports proxy transfers (ie: Using mobile number as account number)
If you do not specify a value for this field, the default value is BANK\_ACCOUNT

Values:

For channel\_code == MY\_DUITNOW:
MOBILE\_NO
NATIONAL\_ID
PASSPORT
BUSINESS\_REGISTRATION
BANK\_ACCOUNT

For currency == THB:
MOBILE\_NO
NATIONAL\_ID
BANK\_ACCOUNT

amount

number Required

Amount to be sent to the destination account.

- For `IDR` currency, number should be integer
- For `PHP` currency, number can be up to 2 decimal places
- For `VND` currency, number should be integer
- For `MYR` currency, number can be up to 2 decimal places
- For `THB` currency, number can be up to 2 decimal places

Minimum0.0

Example10000.0

description

string

Description to send with the payout.
The recipient may see this e.g. in their bank statement (if supported) or in email receipts we send on your behalf.

Min length1

Max length100

currency

string Required

ISO 4217 Currency Code.

receipt\_notification

object (ReceiptNotification)

Object containing email addresses to receive payout details upon successful Payout.
Maximum of three email addresses each.

email\_to

Array of string

Direct email recipients

string

email\_cc

Array of string

CC-ed email recipients

string

email\_bcc

Array of string

BCC-ed email recipients

string

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

401

403

500

Show example

Payout created

application/json

createPayoutResponseExample

createPayoutResponseExample

Code snippet

```
{
  "id": "disb-571f3644d2b4edf0745e9703",
  "amount": 10000,
  "channel_code": "ID_BCA",
  "currency": "IDR",
  "status": "ACCEPTED",
  "description": "July payout",
  "reference_id": "myref-1482928194",
  "created": "2024-12-31T23:53:59Z",
  "updated": "2024-12-31T23:53:59Z",
  "estimated_arrival_time": "2024-12-31T23:59:59Z",
  "business_id": "6018306aa16ad90cb3c43ba7",
  "channel_properties": {
    "account_number": "000000000099",
    "account_holder_name": "Michael Chen"
  }
}
```

JSON

Copy

Collapse all

object

id

string

Xendit-generated unique identifier for each payout

Prefix: disb\_

Min length29

Max length29

Exampledisb-571f3644d2b4edf0745e9703

amount

number

Amount to be sent to the destination account.

- For `IDR` currency, number should be integer
- For `PHP` currency, number can be up to 2 decimal places
- For `VND` currency, number should be integer
- For `MYR` currency, number can be up to 2 decimal places
- For `THB` currency, number can be up to 2 decimal places

Minimum0.0

Example10000.0

channel\_code

string

Channel code of destination bank, E-Wallet or OTC channel.
List of supported channels can be found [here](https://docs.xendit.co/xendisburse/channel-codes)

ExampleID\_BCA

currency

string

ISO 4217 Currency Code.

reference\_id

string

A reference to uniquely identify the Payout.

Min length1

Max length255

Examplemyref-1482928194

status

string

Status of the payout.

The status in the response will always be ACCEPTED; meaning transfer is initiated but not yet completed by bank or E-Wallet.
The final status will be given in a callback.

- `ACCEPTED` - The payout request has been accepted and has not yet been sent on to a channel. A payout may remain in this status if the chosen channel is currently offline. Xendit will process this automatically when the channel comes back online
- `REQUESTED` - The payout has been sent to the channel. Funds have been sent to the channel for processing.
- `FAILED` - Payout failed. See possible reasons in Failed Reasons section.
- `SUCCEEDED` - Sender bank/channel has sent out the payout
- `CANCELLED` - Payout has been cancelled per your request
- `REVERSED` - Payout was rejected by the channel after the payout succeeded. Commonly due to invalid or dormant account.

Valid values[
"ACCEPTED",
"REQUESTED",
"FAILED",
"SUCCEEDED",
"CANCELLED",
"REVERSED"
]

created

string

Timestamp when the payout request was made (in ISO 8601 format)

Timezone UTC+0

updated

string

Timestamp when the payout request was updated (in ISO 8601 format)

Timezone UTC+0

estimated\_arrival\_time

string

Estimated time of arrival of funds in destination account (in ISO 8601 format)
For OTC payouts: Estimated time that funds will be available for pick-up

Timezone UTC+0

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

business\_id

string

Your Xendit Business ID

Example5785e6334d7b410667d355c4

channel\_properties

object (ChannelProperties)

account\_holder\_name

string

Name of account holder as per the bank or E-Wallet's records. Needs to match the registered account name exactly.

Min length1

Max length100

account\_number

string

Account number of destination. Mobile numbers for E-Wallet accounts.
For E-Wallets, standard format should use prefix 0, e.g. 081234567890

Min length1

Max length100

account\_type

string

Account type of the destination for currencies and channels that supports proxy transfers (ie: Using mobile number as account number)
If you do not specify a value for this field, the default value is BANK\_ACCOUNT

Values:

For channel\_code == MY\_DUITNOW:
MOBILE\_NO
NATIONAL\_ID
PASSPORT
BUSINESS\_REGISTRATION
BANK\_ACCOUNT

For currency == THB:
MOBILE\_NO
NATIONAL\_ID
BANK\_ACCOUNT

receipt\_notification

object (ReceiptNotification)

Object containing email addresses to receive payout details upon successful Payout.
Maximum of three email addresses each.

email\_to

Array of string

Direct email recipients

string

email\_cc

Array of string

CC-ed email recipients

string

email\_bcc

Array of string

BCC-ed email recipients

string

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

400DuplicateError

object (400DuplicateError)

error\_code

string

ExampleDUPLICATE\_ERROR

error\_message

string

ExampleA payout with this idempotency key already exists. If you meant to execute a different request, please use another idempotency key

400RequiredPropertyMissingError

object (400RequiredPropertyMissingError)

error\_code

string

ExampleAPI\_VALIDATION\_ERROR

error\_message

string

ExampleShould have required property “xxx”

400InvalidAmountError

object (400InvalidAmountError)

error\_code

string

ExampleAPI\_VALIDATION\_ERROR

error\_message

string

Example"amount" should have 2 decimal places or less

400InvalidExpiryDateError

object (400InvalidExpiryDateError)

error\_code

string

ExampleAPI\_VALIDATION\_ERROR

error\_message

string

Example"expires\_at" should be at least 2 days from now and not exceeding 90 days

400ChannelCodeNotSupportedError

object (400ChannelCodeNotSupportedError)

error\_code

string

ExampleCHANNEL\_CODE\_NOT\_SUPPORTED

error\_message

string

Example“channel\_code” is not supported. See list of supported channel codes at the URL below

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

Unauthorized

application/json

OneOf

401InvalidAPIKeyError

object (401InvalidAPIKeyError)

error\_code

string

ExampleINVALID\_API\_KEY

error\_message

string

ExampleAPI key format is invalid

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

Introduction

Next article

Payout Webhook

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

Idempotency-key \*

for-user-id

Body

application/json

application/json

createPayoutExample

createPayoutExample

 Reset to default

 

11

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
  "channel_code": "ID_BCA",
```

4

```
  "channel_properties": {
```

5

```
    "account_number": "000000000099",
```

6

```
    "account_holder_name": "Michael Chen"
```

7

```
  },
```

8

```
  "amount": 10000,
```

9

```
  "description": "July payout",
```

10

```
  "currency": "IDR"
```

11

```
}
```

 Try it & see response

Response

Available responses

application/json

application/json

200400401403500

 

```
 "business_id": "5785e6334d7b410667d355c4",
```