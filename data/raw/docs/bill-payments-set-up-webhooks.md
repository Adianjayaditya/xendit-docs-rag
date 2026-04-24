---
url: https://docs.xendit.co/docs/bill-payments-set-up-webhooks
title: Set up webhooks
description: ''
section: docs
scraped_at: '2026-04-23T06:18:27.719179Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationBill paymentsIntegration setup
- Documentation
- Bill payments
- Integration setup
---
# Set up webhooks

In our Bill Payments API flows, all payments events will have notifications that you can subscribe to. Your system should be set up to receive our webhooks even if you only use flows where we update the payment statuses synchronously.

In particular, being subscribed to our `Bill Payment` webhooks can help your system know whether a bill payment has happened in real time for payments where end users.

## Saving your webhook endpoints with Xendit

1. Click **Settings** on your sidebar
2. Click **Webhooks** on the sub menu
3. Update the webhook url fields shown in the screenshot below and click **Test and save**
4. Validate that you’ve received the exact test notification in your system

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/image(113).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A18%3A24Z&se=2026-04-23T06%3A29%3A24Z&sr=c&sp=r&sig=jeVvbUMh9AEh0q9xoMEb%2BN3xd2ZwkeZguAckJwbYqgk%3D)

## Available webhook endpoints

| Topic | Description |
| --- | --- |
| Bill Payments | Notification event when bill payment is succeeded or failed |
