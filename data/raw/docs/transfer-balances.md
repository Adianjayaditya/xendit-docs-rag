---
url: https://docs.xendit.co/docs/transfer-balances
title: Transfer sub-account balances
description: ''
section: docs
scraped_at: '2026-04-23T06:17:54.094185Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationxenPlatformAccept & Route Payments
- Documentation
- xenPlatform
- Accept & Route Payments
---
# Transfer sub-account balances

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/accept-payment-for-eng(2).webp?sv=2022-11-02&spr=https&st=2026-04-23T06%3A17%3A50Z&se=2026-04-23T06%3A28%3A50Z&sr=c&sp=r&sig=sy%2BZ6XIF4KDC%2FBG2zEuXUlEzrRh0l8cYYzS76liNcF4%3D)

With xenPlatform, you have full control over your merchant’s balance. You can transfer any amount of funds from your Mater Account to sub-accounts, and vice-versa.

| Source | Destination | Use Cases |
| --- | --- | --- |
| Master-Account | Sub-Account | - Send bonuses - Send refunds - Top up merchant’s balance |
| Sub-Account | Master-Account | - Charge platform commission - Charge subscription fees - Charge management fees |
| Sub-Account | Sub-Account | - Facilitate reselling or drop shipping |

## Region Support for Global Accounts

Cross-border transfers and split payments (between accounts incorporated in different countries) are not supported for merchants incorporated in 🇮🇩 Indonesia. You may still transfer funds between accounts incorporated in the same country.

Additionally, transfers and split payments can only be made between balances of the same currency. You may use the conversion feature before or afterwards to convert currencies.

## How to create transfers

**Via dashboard:**

1. Navigate to the xenPlatform Accounts page
2. Click the **Create transfer** button
3. Fill in the required fields

   1. `From`: account ID or name where the funds are transferred from
   2. `To`: account ID or name where the funds are transferred to
   3. `Amounts to transfer`: the amount of funds of your choice
   4. `Reference`: a unique identifier of the transfer

**Via API:**

To create transfer via API, you will need to specify the required parameters:

- `reference`: a unique identifier of this transfer for reconciliation purposes
- `amount`: the amount you would like to transfer
- `source_user_id`: the account balance from which you would like to send the Transfer from
- `destination_user_id`: the account balance from which you would like to send the Transfer to

Custom

```
curl --request POST \
  --url POST https://api.xendit.co/transfers \
  --data '{
"reference":"2020-nov-subscription-fee",
"amount":10000,
"source_user_id":"5cafeb170a2b18519b1b8768",
"destination_user_id":"5f8d0c0603ffe06b7d4d9fcf"
}'
```

Bash

Copy

Notes on transfers:

- All transfers will be executed immediately
- Transfer amount should be less than the total balance of the sender’s account
- Transfer amount needs to be an absolute number
- You can only create transfers using the Master-Account's API key. Sub-Accounts that you manage through xenPlatform have no ability to create transfers through this endpoint.
