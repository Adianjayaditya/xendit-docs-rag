---
url: https://docs.xendit.co/apidocs/payout-webhook-notification
title: "Payout Webhook"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Payouts](/apidocs/payouts-introduction)
  - [Payout](/apidocs/create-payout)

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

# Payout Webhook

- Updated on Jul 31, 2025
- Published on Nov 29, 2024

 [Prev](/apidocs/create-payout "Create a Payout")  [Next](/apidocs/get-payout "Get payout by ID") 

Post

/payout\_webhook\_url

Xendit notifies your system upon failed and successful payouts via webhook. You need to provide an URL to receive webhook.
Please specify your URL in Webhook Settings in Xendit Dashboard.

The payment notification will be sent as POST request to the URL you set. Xendit attach x-callback-token header that you can validate against Verification Token in Webhook Settings to verify message authenticity.

Please response back with status 200 immediately. Xendit marks webhook event as failed if there is no response within 30s. When events failed, automatic retry will kick-off for the next 24h. Alternatively, you can resend any event in Webhook tab at anytime. You can also receive notification via email every 6h to check your webhook health.

Security

HTTP

Type basic

Responses

200

Show example

Payout Webhook

application/json

payoutWebhookExample

payoutWebhookExample

Code snippet

```
{
  "event": "payout.succeeded",
  "business_id": "5f27a14a9bf05c73dd040bc8",
  "created": "2025-01-01T23:55:59Z",
  "data": {
    "id": "disb-571f3644d2b4edf0745e9703",
    "amount": 10000,
    "channel_code": "ID_BCA",
    "currency": "IDR",
    "status": "SUCCEEDED",
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
}
```

JSON

Copy

Collapse all

object

event

string

Type of the event:

- `payout.succeeded` - A payout's status has already succeeded and partner bank has credited the funds to the beneficiary
- `payout.failed` - A payout's status has already failed and the partner bank rejected the transaction or there was an issue processing the transaction
- `payout.reversed` - A payout that was originally in succeeded status received a bounceback or reversal of funds from the partner bank. Funds have been refunded back to the merchant’s available balance.

Valid values[
"payout.succeeded",
"payout.failed",
"payout.reversed"
]

business\_id

string

Your Xendit Business ID

Example5785e6334d7b410667d355c4

created

string

Timestamp when the payout request was made (in ISO 8601 format)

Timezone UTC+0

data

object (StandardPayoutResponseSchema)

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

Was this article helpful?

Yes  No

Previous article

Create a Payout

Next article

Get payout by ID

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

 Try it & see response

Response

Available responses

application/json

application/json

200

 

```
  "business_id": "5785e6334d7b410667d355c4",
```