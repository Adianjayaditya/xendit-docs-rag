---
url: https://docs.xendit.co/docs/how-payment-sessions-work
title: How payment sessions work
description: ''
section: docs
scraped_at: '2026-04-23T06:20:06.365365Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsPayment productsPayment Sessions
- Documentation
- Accept payments
- Payment products
- Payment Sessions
---
# How payment sessions work

A **Payment Session** is a streamlined, Xendit-hosted solution designed to simplify payment collection and payment method management with minimal integration effort. It acts as a secure, [PCI-compliant](https://docs.xendit.co/docs/pci-dss-compliance?highlight=saq) bridge that allows businesses to facilitate one-time payments, save customer payment details for future use, or perform both actions simultaneously through a single flow. See supported flow [here](https://docs.xendit.co/docs/supported-use-cases-1).

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/image(189).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A20%3A03Z&se=2026-04-23T06%3A31%3A03Z&sr=c&sp=r&sig=AbvPzcCIxFC5AJks7ZJYQVZ7H5HnUVd8D9kXoM496kY%3D)

Depending on the desired user experience and technical capacity, businesses can implement Payment Sessions either via a [**Payment Link**](/v1/docs/how-payment-sessions-work#payment-link), which redirects customers to a ready-to-use Xendit checkout page, or through [**Xendit Components**](/v1/docs/how-payment-sessions-work#xendit-components), which embeds secure payment fields directly into an existing website or app for a native, branded feel.

> See [Xendit Demo Store](https://demo-store.xendit.co/) to give you visualization of how it will interact with your store.

## Payment Link

Payment Link interfaces provide a ready-to-use checkout page hosted by Xendit.

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/image(188).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A20%3A03Z&se=2026-04-23T06%3A31%3A03Z&sr=c&sp=r&sig=AbvPzcCIxFC5AJks7ZJYQVZ7H5HnUVd8D9kXoM496kY%3D)

#### How it works

1. You create a Payment Session via the API or Xendit Dashboard (coming soon)
2. Xendit returns a unique Payment Link URL.
3. You redirect your customer to the hosted checkout page.
4. Xendit handles the full payment experience and processing.

#### User experience

- Customers are redirected to a **Xendit-hosted checkout page**
- No checkout UI needs to be designed or maintained by you
- Optimized for conversion and security by default

#### Why use Payment Link?

- Lowest development effort
- No UI or compliance burden - Xendit hosts and secures the entire checkout experience.
- Best for quick integration - Ideal if you want to accept payments without building a custom checkout.

Follow this link for more detailed [integration guide](/v1/docs/payment-sessions-overview)

## Xendit Components

Xendit Components lets you embed Xendit’s secure payment fields directly into your own website or mobile application.

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/image(187).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A20%3A03Z&se=2026-04-23T06%3A31%3A03Z&sr=c&sp=r&sig=AbvPzcCIxFC5AJks7ZJYQVZ7H5HnUVd8D9kXoM496kY%3D)

Components Mode uses Xendit Components SDK to render secure, PCI-compliant payment fields (such as card number, expiry date, and CVV) inside your existing checkout UI. Customers stay on your site throughout the payment flow.

#### How it works

1. You create a Payment Session via the API.
2. You integrate Xendit Components SDK.
3. You mount secure payment components into your checkout form.
4. Customers enter payment details and complete payment without leaving your site.

Xendit securely handles sensitive payment data and payment processing behind the scenes.

#### User experience

- Customers never leave your website or app
- Payment fields feel like a native part of your checkout
- Fully aligned with your brand and UI flow

#### Why use Xendit Components?

- You control layout, styling, and surrounding UI consistently with your branding
- Secure by default - Xendit manages tokenization, and compliance (e.g. PCI DSS).
