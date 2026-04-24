---
url: https://docs.xendit.co/docs/integration-setup-3
title: Pre-integration checklist
description: ''
section: docs
scraped_at: '2026-04-23T06:18:59.767048Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guide
- Documentation
- Accept payments
- Integration guide
---
# Pre-integration checklist

Before starting your integration with Xendit, ensure you’ve completed the following steps to avoid issues during testing or deployment.

## 1. Activate your payment channels

**Test Mode**

- All payment channels are available by default in test mode.
- However, some payment flows may be limited due to restrictions from partners (e.g., KYC requirements, regional constraints).
- If you encounter issues while testing, please contact our Customer Success team for assistance.

**Live Mode**

- Before going live, check that your desired payment channels are **activated** in the [Dashboard > Payment Channels](https://dashboard.xendit.co/payment-channels).
- If a payment channel is not activated, related API requests or payment links will fail in production.

## 2. Create a secret API key

Generate your API key from the Dashboard:\
**Settings > Developers > API Keys**

You can create different API keys for each environment or use case.

| Environment | Use case |
| --- | --- |
| **Test Mode** | for development and UAT testing. |
| **Live Mode** | for handling real transactions in production. |

**Best Practices**

- Set `Write` permissions if you’re using money-in features.
- Restrict your API key’s permissions to the minimum needed for its purpose.
- Store API keys securely using a secrets management tool.
- For more details, refer to our [API Key Guide](https://docs.xendit.co/xenplatform/settings/#api-key).

## 3. Set up your webhooks

To ensure your system receives real-time updates, **webhooks must be configured**, even if you use synchronous payment flows.

Why webhooks matter:

- They notify your system when a payment is completed (e.g., after 3DS or redirection flows).
- They help detect and reconcile late or previously unreported payments.

**How to register webhook endpoints:**

1. Go to [Settings > Webhooks in your Xendit Dashboard](https://dashboard.xendit.co/settings/developers#webhooks)
2. Enter your webhook **endpoint URLs**

   ![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/image(127).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A18%3A56Z&se=2026-04-23T06%3A29%3A56Z&sr=c&sp=r&sig=Gm0YfzTlsIkab5B0f9gVLj%2Fnl3pu1SmFJw1KN3I%2Bmtk%3D)
3. Click **Test & Save** to verify delivery
4. Confirm that your system receives the exact test notification payload

### Available webhook endpoints

| **Topic** | **Description** |
| --- | --- |
| Unified Refunds – Refund Request Succeeded | Triggered when a refund is successfully processed. |
| Unified Refunds – Refund Request Failed | Triggered when a refund request fails. |
| Payment Requests v3 – Payment Status | Triggered when there is a status update on a Payment object. |
| Payment Requests v3 – Payment Request Status | Triggered when there is a status update on a Payment Request object. |
| Payment Tokens v3 – Payment Token Status | Triggered when there is a status update on a Payment Token object. |
| Payment Session – Completed | Triggered when a payment session is marked as completed, meaning a successful payment attempt was made. |
| Payment Session – Expired | Triggered when a payment session reaches expiry without a successful payment. |
| Subscriptions | Triggered for subscription plan lifecycle events (e.g., created, renewed, canceled). |
| Payment Link | Triggered when a payment link is paid or expired. |
