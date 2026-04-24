---
url: https://docs.xendit.co/docs/payment-channel-page-pull
title: Touch ‘n Go
description: ''
section: docs
scraped_at: '2026-04-23T06:31:50.104687Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsSupported payment channelsMalaysia
- Documentation
- Accept payments
- Supported payment channels
- Malaysia
---
# Touch ‘n Go

Touch 'n Go (TnG) started as a physical public transportation card in the 90s. In 2017, they entered the fintech space with Touch 'n Go Digital, a mobile digital wallet app facilitating investments and loans. The wallet balance is not interchangeable with the public transportation card, but can be used to top up the physical card.

The origin of TnG as a public service and its ease of use as a digital wallet has resulted in a large user base. Many merchants have also been onboarded to run promotional activities, leading to an increase in its popularity.

---

## Features

|  |  |
| --- | --- |
| **Channel Code** | TOUCHNGO |
| **Display Name** | Touch ‘n Go |
| **Currency** | MYR |
| **Country** | MY |
| **Type** | EWALLET |
| **Min Amount** | 1 |
| **Max Amount** | 25,000.00 |
| **User Approval Flow** | REDIRECT, SKIP |
| **Reusable Payment Code** | - |
| **Save** | ✓ |
| **Merchant Initiated Transaction** | ✓ |
| **Auth & Capture** | - |
| **Partial Capture** | - |
| **Multiple Partial Capture** | - |
| **Desktop Support** | WEB URL, QR CODE |
| **Mobile Support** | DEEPLINK URL |
| **Custom Payment Code** | - |
| **Display Merchant Name** | MERCHANT |
| **Display User Name** | - |
| **Set Expiry** | - |
| **Payment Request Expiry (hours)** | 1 |
| **Payment Token Validity (years)** | - |
| **Payment Processing Time (hours)** | INSTANT |
| **Settlement Time** | T+2 CALENDAR DAYS\* |
| **Installments** | - |
| **Refund** | ✓ |
| **Partial Refund** | ✓ |
| **Multiple Partial Refund** | ✓ |
| **Refund Validity (days)** | 180 |
| **Payment Link** | ✓ |
| **Fund Flow** | AGGREGATOR |

## Payment flow

For **desktop** payments, users are directed to a web browser displaying a QR code. They must scan this QR code using the Touch'n Go app on their device and confirm the payment within the app.

On **mobile**, users are sent directly to the Touch'n Go app to confirm their payment. After confirmation, they are rerouted back to the merchant's website.

If a mobile user doesn’t have the Touch'n Go app, they are directed to a mobile browser version where they can input their phone number and PIN to confirm the transaction, after which they are redirected back to the merchant’s website.

\

[](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Touchngo%20-%20mobile%20(1).mp4?sv=2022-11-02&spr=https&st=2026-04-23T06%3A31%3A45Z&se=2026-04-23T07%3A31%3A45Z&sr=c&sp=r&sig=4svUpDBM4BPwg%2FM8G3%2FUCRz16rTIxo%2BemQcCXPBCrO0%3D)
