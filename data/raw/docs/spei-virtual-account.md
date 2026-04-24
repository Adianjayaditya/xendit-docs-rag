---
url: https://docs.xendit.co/docs/spei-virtual-account
title: SPEI Virtual Account
description: ''
section: docs
scraped_at: '2026-04-23T06:33:47.814430Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsSupported payment channelsMexico
- Documentation
- Accept payments
- Supported payment channels
- Mexico
---
# SPEI Virtual Account

> Announcement:
>
> SPEI Virtual Account is now available to make payments simple in Mexico!

SPEI Virtual Account is a payment channel that will leverage Mexico's Sistema de Pagos Electrónicos Interbancarios (SPEI), the country's real-time interbank electronic payment system. This payment method will enable customers to pay conveniently using unique virtual account numbers assigned to each transaction.

SPEI is operated by Banco de México and connects Mexican financial institutions for electronic transfers. This established payment system will allow SPEI Virtual Account to provide a payment method that customers in Mexico already use.

When customers select SPEI Virtual Account at checkout, they are provided with a virtual account number. They can complete the payment through mobile banking, internet banking or ATMs. Once the payment is processed, you receive instant confirmation – ensuring a seamless and reliable transaction experience for you and your customers.

---

## Features

**SPEI Virtual Account availability coming soon**. For general information on how to integrate with our payment channels, see [How Payments API Works](https://docs.xendit.co/docs/how-payments-api-work).

|  |  |
| --- | --- |
| **Channel Code** | SPEI\_VIRTUAL\_ACCOUNT |
| **Display Name** | SPEI Virtual Account |
| **Currency** | MXN |
| **Country** | MX |
| **Type** | BANK TRANSFER |
| **Min Amount** | 0.01 |
| **Max Amount** | 50,000,000.00 |
| **User Approval Flow** | PRESENT TO CUSTOMER |
| **Reusable Payment Code** | ✓ |
| **Save** | - |
| **Merchant Initiated Transaction** | - |
| **Auth & Capture** | - |
| **Partial Capture** | - |
| **Multiple Partial Capture** | - |
| **Desktop Support** | - |
| **Mobile Support** | - |
| **Custom Payment Code** | - |
| **Display Merchant Name** | XENDIT |
| **Display User Name** | - |
| **Set Expiry** | - |
| **Payment Request Expiry (hours)** | - |
| **Payment Token Validity (years)** | - |
| **Payment Processing Time (hours)** | INSTANT |
| **Settlement Time** | INSTANT |
| **Installments** | - |
| **Refund** | - |
| **Partial Refund** | - |
| **Multiple Partial Refund** | - |
| **Refund Validity (days)** | - |
| **Payment Link** | - |
| **Fund Flow** | AGGREGATOR |

## Payment flow

When checking out with SPEI Virtual Account, customers will receive a unique CLABE (Clave Bancaria Estandarizada) virtual account number specific to their transaction. They can complete the payment through their bank's available channels:

- Mobile banking apps - Most Mexican banks offer SPEI transfers through their mobile applications
- Internet banking - Customers can log into their bank's website to make the transfer
- Bank branches - For those who prefer in-person transactions

Payment steps:

1. Customer select SPEI Virtual Account at checkout
2. Receive a unique 18-digit CLABE virtual account number
3. Access their bank (mobile app, website, or branch)
4. Make a SPEI transfer to the provided CLABE number
5. Enter the exact payment amount
6. Complete the transfer and receive confirmation

## Key benefits

- Real-time processing - SPEI operates 24/7 with immediate payment confirmation
- Bank coverage - Available at banks and financial institutions in Mexico
- Direct bank transfers - Customers pay from their bank accounts without cards
- Standard payment method - Uses CLABE numbers that Mexican customers recognize

## Limitations

- MXN only – SPEI cannot accept or convert other currencies
- CLABE cannot be updated once issued, only cancelled
- If a customer needs a refund, the workaround is to use Xendit Payouts to send the amount back to the customer’s bank account directly.
- No disputes – SPEI transfers are irrevocable by design, so the dispute flow doesn’t apply here.
- No subscriptions – SPEI VA doesn’t support recurring/merchant-initiated charges.
- Payment types supported:

  1. REUSABLE\_PAYMENT\_CODE - supported today
  2. PAY - coming soon
- SPEI virtual accounts on Payment Session support are coming in Phase 2 (after enabling PAY type)

## Demo

## Pilot Integration Guideline

See [guide on Reusable Payment Codes](https://docs.xendit.co/docs/reusable-payment-codes) to understand how you can integrate SPEI Virtual Account into your payment flow.

If you're interested in using SPEI Virtual Account for your business, contact [sales.latam@xendit.co](mailto:sales.latam@xendit.co) for more information.
