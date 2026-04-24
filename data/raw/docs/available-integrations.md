---
url: https://docs.xendit.co/docs/available-integrations
title: Available integrations
description: ''
section: docs
scraped_at: '2026-04-23T06:07:40.986197Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guideCard Payments via API
- Documentation
- Accept payments
- Integration guide
- Card Payments via API
---
# Available integrations

To best support the way you accept cards, it's essential to choose the correct integration. You can explore the different integration options available below, each designed to meet specific business needs and technical requirements.

## 1. Payments API & Components Integration

Ideal for: Businesses seeking full control over the payment experience and an embedded checkout flow within their web or mobile application, without redirecting users.

**Features:**

Embedded Checkout: Retain full control of the UI layout and your branding using [Xendit Components](/v1/docs/components-overview), a client-side integration model powered by Payment Sessions.

Reduced PCI Compliance Scope: Securely handle sensitive payment data using Xendit Components. It embeds a Xendit-managed, PCI-compliant payment UI directly into your application, meaning you don't need to process raw card data yourself.

[Full PAN integration](/v1/docs/create-a-token): Allows raw card details to be sent directly to Xendit (strictly requires PCI-DSS Level 2 registration or SAQ-D with a yearly assessment).

## 2. Payment Links

Ideal for: Businesses looking for a simple, [quick-to-deploy hosted solution](/v1/docs/how-payment-sessions-work).

Features:

- Xendit provides a secure, ready-to-use payment page.
- No need to handle sensitive card data or build a frontend UI.
- Requires SAQ-A for PCI DSS compliance.

## 3. Subscriptions or Recurring Transactions

Ideal for: Businesses with subscription models, memberships, or recurring billing needs.

Options:

[Xendit Managed Subscriptions](/v1/docs/how-subscriptions-work): Let Xendit handle all aspects of subscription management, including scheduling and retries.

[Self-Managed Subscriptions](/v1/docs/components-save-payment-method): Use the Payments API alongside Xendit Components (utilizing the Save Payment Method or Pay and Save session types) to securely tokenize cards and process recurring transactions on your own schedule.

[Unscheduled Card on File (Merchant-Initiated)](/v1/docs/cards-recurring-and-merchant-initiated-transactions): Use the Payments API and Xendit Components to securely store user card details for future, frictionless purchases without a predetermined billing schedule.

## 4. Accept Virtual Credit Cards through a Xendit Hosted Page

Ideal for: Businesses accepting virtual credit cards (VCCs), such as hotels, property managers, or online travel agencies (OTAs).

Features:

Securely process virtual cards through a dedicated Xendit-hosted payment link.

\*\*\* Tip: If you are building a custom checkout experience, we highly recommend using Xendit Components as it seamlessly bridges your backend Payment Sessions with a secure frontend SDK (xendit-components-web), keeping your integration secure and compliant with minimal effort.
