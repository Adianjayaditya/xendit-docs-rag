---
url: https://docs.xendit.co/docs/qris
title: QRIS
description: ''
section: docs
scraped_at: '2026-04-23T06:28:55.811120Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsSupported payment channelsIndonesia
- Documentation
- Accept payments
- Supported payment channels
- Indonesia
---
# QRIS

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/qris-logo.svg?sv=2022-11-02&spr=https&st=2026-04-23T06%3A28%3A48Z&se=2026-04-23T06%3A39%3A48Z&sr=c&sp=r&sig=3b6nKO%2BYGFwTSgrXi7gPLwsvTI6K0mE96yQZHxNah%2Bg%3D)QR code payments in Indonesia uses QRIS (Quick Response Code Indonesian Standard), an Indonesian QR code standard developed by Bank Indonesia (BI) and Indonesian Payment System Association for cashless payments in Indonesia.

---

## Features

|  |  |
| --- | --- |
| **Channel Code** | QRIS |
| **Display Name** | QRIS |
| **Currency** | IDR |
| **Country** | ID |
| **Type** | QR CODE |
| **Min Amount** | 1 |
| **Max Amount** | 10,000,000.00 |
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
| **Display Merchant Name** | MERCHANT |
| **Display User Name** | - |
| **Set Expiry** | - |
| **Payment Request Expiry (hours)** | 48 |
| **Payment Token Validity (years)** | - |
| **Payment Processing Time (hours)** | INSTANT |
| **Settlement Time** | T+2 CALENDAR DAYS\* |
| **Installments** | - |
| **Refund** | ✓ |
| **Partial Refund** | ✓ |
| **Multiple Partial Refund** | ✓ |
| **Refund Validity (days)** | 7\* |
| **Payment Link** | ✓ |
| **Fund Flow** | AGGREGATOR |

## Payment flow

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/image(37).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A28%3A48Z&se=2026-04-23T06%3A39%3A48Z&sr=c&sp=r&sig=3b6nKO%2BYGFwTSgrXi7gPLwsvTI6K0mE96yQZHxNah%2Bg%3D "image(37).png")

1. On the checkout page, select **QRIS** as payment method
2. A QR code will appear on the screen
3. Open your mobile banking or e-wallet app, then find the **Scan QR Code** feature
4. Point your phone camera at the QR code
5. Make sure the payment amount and merchant is correct
6. Confirm payment

## Limitations

The QRIS refund process is limited to the following issuers:

| **Issuer** | **Refund full amount & within 24 hours of payment completion** | **Refund full amount & after 24 hours of payment completion** | **Partial refund** |
| --- | --- | --- | --- |
| DANA | ✅ | ✅ | ✅ |
| ShopeePay | ✅ | ✅ | ✅ |
| OVO | ✅ | ✅ | ✅ |
| Gopay | ✅ | ✅ | ✅ |
| CIMB | ❌ | ✅ | ✅ |
| Permata | ✅ | ✅ | ✅ |
| Jenius / SMBC | ✅ | ✅ | ✅ |
| BSI | ✅ | ✅ | ✅ |
