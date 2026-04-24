---
url: https://docs.xendit.co/docs/truemoney
title: TrueMoney E-Wallet
description: ''
section: docs
scraped_at: '2026-04-23T06:35:58.805640Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsSupported payment channelsThailand
- Documentation
- Accept payments
- Supported payment channels
- Thailand
---
# TrueMoney E-Wallet

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/TMN_Ver.svg?sv=2022-11-02&spr=https&st=2026-04-23T06%3A35%3A55Z&se=2026-04-23T06%3A46%3A55Z&sr=c&sp=r&sig=p9Pq9mym0BfITYnFNw6iYd0kmoXQDX1lm8Qt89AFkZQ%3D)

TrueMoney Wallet is Thailand's leading e-wallet that provides a convenient and secure way for customers to make payments online and in-store.

---

## Features & Requirements

|  |  |
| --- | --- |
| **Channel code** | `TRUEMONEY` |
| **Currency** | THB |
| **Minimum amount** | 1 |
| **Maximum amount** | 50,000 |
| **User approval flow** | REDIRECT |
| **Save** | ❌ |
| **Recurring** | ❌ |
| **Auth & capture** | ❌ |
| **Partial capture** | ❌ |
| **Multiple partial capture** | ❌ |
| **Payment request expiry** | 2 hours |
| **Payment token validity** | ❌ |
| **Settlement time** | Instant |
| **Refund** | ❌ |
| **Partial refund** | ❌ |
| **Multiple partial refund** | ❌ |
| **Refund validity** | ❌ |
| **Compatible integration** | Payment API, Payment Link |

## Payment Flow

[null](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/TH%20Payment%20Flow-TrueMoney.mp4?sv=2022-11-02&spr=https&st=2026-04-23T06%3A35%3A55Z&se=2026-04-23T07%3A35%3A55Z&sr=c&sp=r&sig=jljaDajHI6XJ%2Bwt2Mvk7AbdpJgzDDOk2uDvXeV%2BlrJY%3D)

1. On the checkout page, end customers select TrueMoney E-Wallet
2. Redirect end customers to web app & end customers need to input registered mobile phone with TrueMoney E-Wallet
3. End customer submit OTP verification
4. Once OTP verification is completed, the payment will be paid successfully
