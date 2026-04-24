---
url: https://docs.xendit.co/docs/cards-virtual-credit-card-processing
title: Virtual Credit Card processing
description: ''
section: docs
scraped_at: '2026-04-23T06:19:58.513587Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guideCard Payments via API
- Documentation
- Accept payments
- Integration guide
- Card Payments via API
---
# Virtual Credit Card processing

Virtual Credit Cards are temporary, digital versions of traditional credit cards used primarily for online transactions. They offer enhanced security by generating a unique, temporary card number with a limited validity period. These cards help protect consumers’ real credit card details and reduce fraud risk, as they are often one-time-use or have predefined spending limits.

Virtual Credit Cards do not have authentication capabilities, therefore non-authenticated (non-3DS) transactions need to be allowed on your account. To enable this, please reach out to [help@xendit.co](mailto:help@xendit.co).

## Processing Virtual Credit Cards

Virtual Credit Cards can be processed by using our [Payment Links](/v1/docs/how-payment-links-work).

Alternatively, they can be processed by creating a custom payment page managed by you, where 3DS is not enabled. If you are creating your own page to process virtual credit cards, follow the default integration guide, using the [components integration.](/v1/docs/components-overview).
