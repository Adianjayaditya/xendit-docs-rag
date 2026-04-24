---
url: https://docs.xendit.co/docs/bank-transfer
title: Bank Transfer
description: ''
section: docs
scraped_at: '2026-04-23T06:34:09.799847Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsSupported payment channelsPhilippines
- Documentation
- Accept payments
- Supported payment channels
- Philippines
---
# Bank Transfer

Bank transfers in the Philippines are typically made via InstaPay or PesoNet. To accept bank transfers from your customers, you can create unique virtual account numbers assigned to each of your users. They can easily make payments via bank transfer

Your customers can complete the transfer via mobile banking, internet banking, or ATM. Once the payment is made, you receive an instant confirmation, ensuring a seamless and secure payment experience for both you and your customers.

Note that the source of funds must be a bank or Electronic Money Issuer that’s part of the InstaPay / PesoNet networks.

---

## Features

|  |  |
| --- | --- |
| **Channel Code** | BANK\_TRANSFER |
| **Display Name** | Bank Transfer |
| **Currency** | PHP |
| **Country** | PH |
| **Type** | BANK TRANSFER |
| **Min Amount** | 1 |
| **Max Amount** | 200,000,000.00 |
| **User Approval Flow** | PRESENT TO CUSTOMER |
| **Reusable Payment Code** | ✓ |
| **Save** | - |
| **Merchant Initiated Transaction** | - |
| **Auth & Capture** | - |
| **Partial Capture** | - |
| **Multiple Partial Capture** | - |
| **Desktop Support** | - |
| **Mobile Support** | - |
| **Custom Payment Code** | ✓ |
| **Display Merchant Name** | MERCHANT |
| **Display User Name** | - |
| **Set Expiry** | - |
| **Payment Request Expiry (hours)** | - |
| **Payment Token Validity (years)** | - |
| **Payment Processing Time (hours)** | T+1 BUSINESS DAYS |
| **Settlement Time** | T+3 BUSINESS DAYS |
| **Installments** | - |
| **Refund** | - |
| **Partial Refund** | - |
| **Multiple Partial Refund** | - |
| **Refund Validity (days)** | - |
| **Payment Link** | - |
| **Fund Flow** | AGGREGATOR |

## Payment flow

Mobile banking

1. Log in to your banking or e-wallet app (must support InstaPay / PesoNet)
2. Select **Bank Transfer > InstaPay or PesoNet (some apps may not allow you to choose)**
3. Select **Asia United Bank (AUB)** as the recipient bank
4. Enter **merchant name**
5. Enter **virtual account number** (e.g. 7057601478328965)
6. Enter **amount to pay**
7. Enter **PIN**

Internet banking

1. Log in to your preferred internet banking portal (must support InstaPay / PesoNet)
2. Select **Bank Transfer > InstaPay or PesoNet (some apps may not allow you to choose)**
3. Select **Asia United Bank (AUB)** as the recipient bank
4. Enter **merchant name**
5. Enter **virtual account number** (e.g. 7057601478328965)
6. Enter **amount to pay**
7. Enter **PIN**

##

Examples of the payment interface on GCAsh and BPI
