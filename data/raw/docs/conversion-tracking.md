---
url: https://docs.xendit.co/docs/conversion-tracking
title: Conversion Tracking
description: ''
section: docs
scraped_at: '2026-04-23T06:22:53.242025Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guidePayment Link (Legacy)
- Documentation
- Accept payments
- Integration guide
- Payment Link (Legacy)
---
# Conversion Tracking

Payment Links allow you to set up analytics tools to track your customer’s journey, from arriving at the checkout page to completing a payment. These tools include **Google Analytics** and **Facebook Pixel**, and you can track various events for better insights into customer behavior.

## **Trackable events and their triggers**

| **Event Name** | **Payload** | **Trigger** |
| --- | --- | --- |
| xendit\_begin\_checkout | None | When the checkout page loads. |
| xendit\_add\_payment\_info | Channel name | When a customer clicks or selects a payment channel. *(Note:* [*QRIS*](https://xendit-docs.document360.io/docs/qris) *channel selection is not tracked.)* |
| xendit\_checkout\_progress | None | - On clicking **Pay Now** (Card, Direct Debit, OVO) - On clicking **Continue** (PayLater) - When selecting channels without a **Pay Now** button (e.g., VA, eWallets, DD Mandiri) - *(QRIS confirmation is not tracked.)* |
| xendit\_purchase | Currency, amount | When the payment success page is displayed. |
| xendit\_view\_item | None | When a customer clicks the **View More** button on the V1 checkout web. |

## **Google Analytics**

1. Go to **analytics.google.com**
2. Fill in **your details**: account name, property name, timezone, currency, business size, etc. (some details are not mandatory)

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot 2025-07-22 at 15.00.30(1).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A22%3A49Z&se=2026-04-23T06%3A33%3A49Z&sr=c&sp=r&sig=Srt94tyOXx6EnZjv%2FBhtdIsYxWgRBB8gXGVK%2BwgYzyM%3D)

3. Accept the **Terms & Conditions**, then choose web platform

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot 2025-07-22 at 15.03.30(1).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A22%3A49Z&se=2026-04-23T06%3A33%3A49Z&sr=c&sp=r&sig=Srt94tyOXx6EnZjv%2FBhtdIsYxWgRBB8gXGVK%2BwgYzyM%3D)

4. On the next pop-up, enter **checkout.xendit.co** as the page url as and give it a name

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/image-1753172130449.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A22%3A49Z&se=2026-04-23T06%3A33%3A49Z&sr=c&sp=r&sig=Srt94tyOXx6EnZjv%2FBhtdIsYxWgRBB8gXGVK%2BwgYzyM%3D)

5. On the next page, your Google Analytics ID will be displayed

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/image-1753172086877.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A22%3A49Z&se=2026-04-23T06%3A33%3A49Z&sr=c&sp=r&sig=Srt94tyOXx6EnZjv%2FBhtdIsYxWgRBB8gXGVK%2BwgYzyM%3D)

## **Facebook Pixel**

1. Open **business.facebook.com**
2. Click on **Events Manager**

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot 2025-07-22 at 15.12.57(1).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A22%3A49Z&se=2026-04-23T06%3A33%3A49Z&sr=c&sp=r&sig=Srt94tyOXx6EnZjv%2FBhtdIsYxWgRBB8gXGVK%2BwgYzyM%3D)

3. Click **Connect Data**

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot 2025-07-22 at 15.20.28.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A22%3A49Z&se=2026-04-23T06%3A33%3A49Z&sr=c&sp=r&sig=Srt94tyOXx6EnZjv%2FBhtdIsYxWgRBB8gXGVK%2BwgYzyM%3D)

4. Select **Web**

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot 2025-07-22 at 15.23.39.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A22%3A49Z&se=2026-04-23T06%3A33%3A49Z&sr=c&sp=r&sig=Srt94tyOXx6EnZjv%2FBhtdIsYxWgRBB8gXGVK%2BwgYzyM%3D)

5. Enter a name for your analytics project

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot 2025-07-22 at 15.27.47.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A22%3A49Z&se=2026-04-23T06%3A33%3A49Z&sr=c&sp=r&sig=Srt94tyOXx6EnZjv%2FBhtdIsYxWgRBB8gXGVK%2BwgYzyM%3D)

6. You can ignore website name or simply enter **checkout.xendit.co**
7. Click **Close** (no need to proceed to the next section since we just need the ID, and integration is already implemented)
8. On the left panel, find the Pixel ID below the name of the project

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot 2025-07-22 at 15.28.31.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A22%3A49Z&se=2026-04-23T06%3A33%3A49Z&sr=c&sp=r&sig=Srt94tyOXx6EnZjv%2FBhtdIsYxWgRBB8gXGVK%2BwgYzyM%3D)
