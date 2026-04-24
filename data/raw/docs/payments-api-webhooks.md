---
url: https://docs.xendit.co/docs/payments-api-webhooks
title: Payments API webhooks
description: ''
section: docs
scraped_at: '2026-04-23T06:23:31.310980Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guidePayments via API
- Documentation
- Accept payments
- Integration guide
- Payments via API
---
# Payments API webhooks

This table shows the types of webhooks available for your system to subscribe to.

| Data resource object | Webhook event | Description |
| --- | --- | --- |
| Payment Request | payment\_request.expiry | Event occurs when payment request created has expired. An expired payment request will no longer receive new payments. Note that race conditions can happen due to limitations of real time messaging. |
| Payment Token | payment\_token.activation | Event occurs when payment token creation was successful authenticated and confirmed by the payment channel. |
| Payment Token | payment\_token.failure | Event occurs when payment token creation failed authentication and failed by the payment channel. |
| Payment Token | payment\_token.expiry | Event occurs when payment token has reached its natural expiry period or when a card has passed its expiry date. |
| Payment | payment.capture | Event occurs when payment has been successfully collected and confirmed by the payment channel. |
| Payment | payment.authorization | Event occurs when payment has been successfully reserved on the end user account and confirmed by the payment channel. |
| Payment | payment.expiry | Event occurs when a successful payment authorization has expired. |
| Payment | payment.failure | Event occurs when payment fails to be collected by payment channel. |
| Refund | refund.succeeded | Event occurs when refund was successful and  confirmed by the payment channel. |
| Refund | refund.failed | Event occurs when refund has failed and was  failed by the payment channel. |
