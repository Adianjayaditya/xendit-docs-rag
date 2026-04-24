---
url: https://docs.xendit.co/docs/line-pay-e-wallet
title: LINE Pay E-Wallet
description: ''
section: docs
scraped_at: '2026-04-23T06:35:37.250181Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsSupported payment channelsThailand
- Documentation
- Accept payments
- Supported payment channels
- Thailand
---
# LINE Pay E-Wallet

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Line_Pay_Hor.svg?sv=2022-11-02&spr=https&st=2026-04-23T06%3A35%3A33Z&se=2026-04-23T06%3A46%3A33Z&sr=c&sp=r&sig=6XVCwUds4bHdMfUTo8%2Bx%2BxCShyf62wAxt19496QetLw%3D)

LINE Pay is Thailand's leading e-wallet that provides a convenient and secure way for customers to make payments online and in-store.

---

## Features & Requirements

|  |  |
| --- | --- |
| **Channel code** | `LINEPAY` |
| **Currency** | THB |
| **Minimum amount** | 1 |
| **Maximum amount** | 50,000 |
| **User approval flow** | REDIRECT |
| **Save** | ❌ |
| **Recurring** | ❌ |
| **Auth & capture** | ❌ |
| **Partial capture** | ❌ |
| **Multiple partial capture** | ❌ |
| **Expiry Time** | 20 minutes |
| **Payment token validity** | ❌ |
| **Settlement time** | T+1 Day |
| **Refund** | ❌ |
| **Partial refund** | ❌ |
| **Multiple partial refund** | ❌ |
| **Refund validity** | ❌ |
| **Compatible integration** | Payment API, Payment Link |

## Payment Flow

[null](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Payment%20Flow-LinePay.mp4?sv=2022-11-02&spr=https&st=2026-04-23T06%3A35%3A33Z&se=2026-04-23T07%3A35%3A33Z&sr=c&sp=r&sig=QhHcdeKTRcpZX%2FuNnNB3MxySc7w7q%2F8I8dUiJ33Qqf4%3D)

1. On the checkout page, end customers select LINE Pay E-Wallet
2. Redirect end customers to LINE Pay app to make the payment
3. End customers confirm the payment amount and merchant is correct
4. End customers click Pay to confirm the payment
