---
url: https://docs.xendit.co/docs/cards-api-overview
title: Overview
description: ''
section: docs
scraped_at: '2026-04-23T06:19:34.049761Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guideCard Payments via API
- Documentation
- Accept payments
- Integration guide
- Card Payments via API
---
# Overview

Xendit empowers businesses in Southeast Asia to accept online card payments securely and reliably. With a growing number of shoppers in the region gaining access to bank accounts and cards, offering a seamless card payment experience is essential. We support major card networks like Visa, Mastercard, JCB, and American Express, along with regional options like BCA and GPN, across multiple countries.

## **Supported countries & card brands:**

- **Indonesia (🇮🇩):** Visa, Mastercard, JCB, American Express, BCA, GPN
- **Malaysia (🇲🇾):** Visa, Mastercard, JCB, American Express
- **Philippines (🇵🇭):** Visa, Mastercard, JCB
- **Singapore (🇸🇬):** Visa, Mastercard
- **Thailand (🇹🇭):** Visa, Mastercard, JCB, China UnionPay, American Express
- **Vietnam (🇻🇳):** Visa, Mastercard, JCB

## Supported functionality

|  | American express | China UnionPay | JCB | Mastercard | Visa | Other domestic cards |
| --- | --- | --- | --- | --- | --- | --- |
| [One-off payment](/docs/guest-checkout) (*Guest checkout*) | 🇮🇩 ID  🇲🇾MY (redirect only)  🇹🇭 TH (redirect only) | 🇹🇭TH (redirect only) | 🇮🇩 ID  🇲🇾MY  🇵🇭PH  🇹🇭TH (redirect only)  🇵🇭PH  🇹🇭TH  🇻🇳VN | 🇮🇩ID  🇲🇾MY  🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN | 🇮🇩ID  🇲🇾MY  🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN | BCA - 🇮🇩  GPN - 🇮🇩 |
| [Subscription/recurring](/v1/docs/subscription-and-merchant-initiated-transactions) | 🇮🇩ID |  | 🇮🇩 ID  🇵🇭PH | 🇮🇩ID  🇲🇾MY  🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN | 🇮🇩ID  🇲🇾MY  🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN |  |
| [Unscheduled card on file (merchant initiated transactions)](/v1/docs/subscription-and-merchant-initiated-transactions) | 🇮🇩ID |  | 🇮🇩 ID  🇵🇭PH  🇻🇳VN | 🇮🇩ID 🇲🇾MY 🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN | 🇮🇩ID 🇲🇾MY 🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN |  |
| [One-click (stored card)](/v1/docs/store-a-card-for-one-click) | 🇮🇩 ID |  | 🇮🇩 ID  🇵🇭PH | 🇮🇩ID  🇲🇾MY 🇵🇭PH **🇸🇬**SG 🇹🇭TH  🇻🇳VN | 🇮🇩ID  🇲🇾MY 🇵🇭PH **🇸🇬**SG 🇹🇭TH  🇻🇳VN |  |
| [Manual capture](/v1/docs/capturing-a-card-payment) | 🇮🇩 ID |  | 🇮🇩 ID  🇵🇭PH | 🇮🇩ID 🇲🇾MY 🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN | 🇮🇩ID 🇲🇾MY 🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN |  |
| [Refunds](/v1/docs/refund-a-card-payment) | 🇮🇩ID  🇹🇭TH | 🇹🇭TH | 🇮🇩 ID  🇹🇭TH  🇵🇭PH | 🇮🇩ID  🇲🇾MY  🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN | 🇮🇩ID  🇲🇾MY  🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN | BCA - 🇮🇩  GPN - 🇮🇩 |
| [Partial capture](/docs/cards-capturing-a-card-payment) | 🇮🇩 ID |  | 🇮🇩 ID | 🇮🇩ID 🇲🇾MY 🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN | 🇮🇩ID 🇲🇾MY 🇵🇭PH **🇸🇬**SG  🇹🇭TH  🇻🇳VN |  |

> To process in the most suitable way, make sure to choose the [correct integration](/docs/cards-choose-the-correct-integration).
